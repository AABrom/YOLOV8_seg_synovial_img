# YOLOv8 blood vessel instance segmentation on synovial tissues histology images
We used Synovial tissues histology from patients with end-stage osteoarthritis, soft tissue and traumatic injuries of the knee dataset. Scripts allow to create YAML-format dataset, to predict blood vessels area on synovial tissue histological images by Aperio CS2 Digital Pathology Scanner or identical.
vessel_seg_model metrics: Box: P = 0.656, R = 0.535, MaP50 = 0.57, Mask: P = 0.588, R = 0.464, MaP50 = 0.48
______________________________________________________________________________
### Run
1. Local clone:
```ruby
git clone https://github.com/AABrom/YOLOV8_seg_synovial_img
pip install -r requirements.txt
```
2. To use our data: download synovial_annots_json, synovial_images folders.

3. To create your own dataset:
- First of all, you have to convert annotations to YOLO-supported format. Save your annotations from QuPath to GeoJson format, annotation file names similar to image names, for example: Image1.tif, Image1.json. Use [QuPath documentation](https://qupath.readthedocs.io/en/stable/docs/advanced/exporting_annotations.html). All your images and annotations should be in one folder. 
- Download script GEOJSONTOYOLO.py. Create folder to save results. In Windows: run command line, change to the script directory. To run script choose your images and annotations folder as --path_to_folder and your results folder as --path_to_result_folder. For example:

```ruby
python GEOJSONTOYOLO.py --path_to_folder C:\Users\user\Desktop\folder --path_to_result_folder C:\Users\user\Desktop\txt_annots
```
If all done, your converted images are in result folder. 
______________________________________________________________________________
### [Dataset](https://data.mendeley.com/datasets/cz3xt8mbpn/1)
Jamal, Juliana; Roebuck, Margaret ; Wood, Amanda; Santini, Alasdair; Bou-Gharios, George; Wong, Pooi-Fong (2022), “Synovial tissues histology from patients with end-stage osteoarthritis, soft tissue and traumatic injuries of the knee ”, Mendeley Data, V1, doi: 10.17632/cz3xt8mbpn.1
______________________________________________________________________________
### Dataset review
Dataset contains 33 individual patient folders containing the H&E-stained synovial tissue section tiff images. All patients underwent knee surgery at the Liverpool University Hospitals NHS Foundation Trust, Liverpool. Histological microimages of each complete synovial tissue were captured at 20x and digitalised using an Aperio CS2 Digital Pathology Scanner.
______________________________________________________________________________
### [Ultralytics YOLO format](https://docs.ultralytics.com/datasets/segment/)
- One text file per image: Each image in the dataset has a corresponding text file with the same name as the image file and the ".txt" extension.
- One row per object: Each row in the text file corresponds to one object instance in the image.
- Object information per row: Each row contains the following information about the object instance:
- Object class index: An integer representing the class of the object (e.g., 0 for person, 1 for car, etc.).
- Object bounding coordinates: The bounding coordinates around the mask area, normalized to be between 0 and 1.
```
<class-index> <x1> <y1> <x2> <y2> ... <xn> <yn>
```
______________________________________________________________________________
### Annotations
All images annotated by QuPath-0.5.1 using «Brush». We used 300μm area sections. Polygon annotations were exported in GeoJson format with each json file name same to related image name.
______________________________________________________________________________
### Author: Anastasia Bromberg 
