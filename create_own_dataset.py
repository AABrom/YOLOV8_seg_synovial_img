import json
import re
import numpy as np
import os
import glob
import sklearn as sk
from sklearn.model_selection import train_test_split
import shutil


# create YAML-format dirs
os.mkdir("txt_annots")
os.makedirs("yolo_v8/valid/labels")
os.makedirs("yolo_v8/train/labels")
os.makedirs("yolo_v8/valid/images")
os.makedirs("yolo_v8/train/images")



def get_txt_annotation(path_to_file, path_to_txt_folder, filename):

  '''
    Create a txt file with normalized coordinates of single-class polygon annotations from geojson
    Создаёт текстовый файл с нормализованными координатами полигональных аннотаций единственного класса из файл формата geojson

    path_to_file: path to geojson/json file with img annotations
    filename: name of existing/new txt file used as final txt file with img annotations
  '''
  coords_list = []
  str_coords_list = []
  f = open(os.path.join(path_to_txt_folder, filename),'w')
  with open(path_to_file) as file:
        j_file = json.load(file)

  for dict_ in j_file:
        geometry = dict_['geometry']
        coords = geometry['coordinates']
        coords_list.append(coords)

  for coord in coords_list:
        coord = str(coord)
        str_coord = re.sub('[^\d\.]',' ', coord)
        str_coords_list.append(str_coord)

  for s in str_coords_list:
        # получить списки с координатами масок на изображении внутри цикла for
        a = [float(x) for x in s.split()]
        # создадим список с нормализованными значениями
        norm_list = []
        for coord in a:
            if a.index(coord) % 2:
                norm_list.append(coord/942)
            else:
                norm_list.append(coord/1716)

        # удалить символы запятых и квадратных скобок
        str_a = ' '.join(map(str,norm_list))
        # добавить метку единственного класса 0
        str_a = '0 ' + str_a
        #записать в txt файл каждую строку с новой строки
        f.write(str_a + "\n")


path_to_folder = 'synovial_annots_json/*'
path_to_txt_folder = 'txt_annots'

for path_to_file in glob.glob(path_to_folder):
    txt_filename = os.path.basename(path_to_file).rstrip('json') + 'txt'
    try:
        get_txt_annotation(path_to_file, path_to_txt_folder, txt_filename)
        pass
    except:
        continue


img_names = [] # create a list of file names

for file in glob.glob(path_to_txt_folder + '/*'):
    file_name = os.path.basename(file)
    img_names.append(file_name)


X_train, X_val, y_train, y_val = sk.model_selection.train_test_split(img_names, img_names, train_size=0.8, random_state=42)

path_to_img = 'synovial_images'

#val_labels, images
for txt_id in X_val:
    shutil.move(os.path.join(path_to_txt_folder, txt_id), 'yolo_v8/valid/labels')
    shutil.move(os.path.join(path_to_img, txt_id.rstrip('.txt') + '.tif'), 'yolo_v8/valid/images')


#train_labels, images
for txt_id in X_train:
    shutil.move(os.path.join(path_to_txt_folder, txt_id), 'yolo_v8/train/labels')
    shutil.move(os.path.join(path_to_img, txt_id.rstrip('.txt') + '.tif'), 'yolo_v8/train/images')
