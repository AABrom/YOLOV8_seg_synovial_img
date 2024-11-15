import os
import argparse
from pathlib import Path 
import cv2
import json
from itertools import chain

def get_text_annotation(path_to_folder, path_to_result_folder):

  
  """Create a txt file with normalized coordinates of single-class polygon annotations from geojson (exported from QuPath)
    path_to_file: path to geojson/json file with img annotations
    path_to_result_folder: folder to save output"""
  
  #resistance to incorrect input data
  path_to_folder = Path(path_to_folder) 
  path_to_result_folder = Path(path_to_result_folder)

  # image extensions available
  ext = ('.bmp', '.jpg', '.jpeg', '.png', '.tif', '.tiff')
  img_counter = 0
 
  # scanning the directory to get image files
  for file in os.scandir(path_to_folder):
        if file.path.endswith(ext):
            # open image
            img = cv2.imread(file.path)  
            img_counter+=1          
            max_dim = max(img.shape[0], img.shape[1]) #get coords range
            # create txt file for output YOLO annotations
            txt_filename = Path(file.path).stem + '.txt'
            f = open((path_to_result_folder/txt_filename),'w')

            #open geojson file with annotations
            annot_name = Path(file.path).stem + '.json'            
            try: 
              with open(path_to_folder/annot_name) as file:
                    j_file = json.load(file)
                    for dict_ in j_file:
                      coords_list = [0]
                      coords = dict_['geometry']['coordinates']
                      coords_list.extend(round(elem/max_dim, 6) for item in chain(*coords) for elem in item)
                      str_a = ' '.join(map(str, coords_list))
                      f.write(str_a + "\n")
            except:
                    print(f'Warning: No annotations named {annot_name} found. Empty annotation file created.\n Your annotations should have same names as images, for example: Image1.tif, Image1.json')
                    continue
  if img_counter:
    print(f'Conversion completed. {img_counter} images found.')
  else: print(f'No images found in this folder. Your images should be: {ext}')


def main():
    parser = argparse.ArgumentParser(
        description=r"Converter from geojson polygon annotations to YOLO txt format")

    
    parser.add_argument("--path_to_folder", type=str, required=True,
                        help=r"Absolute (full) path to images and annotations folder, for example: --photo_path 'C:\Users\user\Desktop\folder'")
    parser.add_argument("--path_to_result_folder", type=str, required=True,
                        help=r"Absolute (full) path to results folder, for example: --path_to_result_folder 'C:\Users\user\Desktop\txt_annots'")

    args = parser.parse_args()

    get_text_annotation(args.path_to_folder, args.path_to_result_folder)


if __name__ == '__main__':
    main()


