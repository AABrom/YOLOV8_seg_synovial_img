Часть данных Synovial tissues histology from patients with end-stage osteoarthritis, soft tissue and traumatic injuries of the knee преобразованы в YAML-формат для сегментации, поддерживаемый нейросетями группы YOLO. Обучение YOLOv8-seg.
______________________________________________________________________________
### Структура данных
Аннотации представлены 
Изображения представлены

______________________________________________________________________________
### Источник данных https://data.mendeley.com/datasets/cz3xt8mbpn/1
Jamal, Juliana; Roebuck, Margaret ; Wood, Amanda; Santini, Alasdair; Bou-Gharios, George; Wong, Pooi-Fong (2022), “Synovial tissues histology from patients with end-stage osteoarthritis, soft tissue and traumatic injuries of the knee ”, Mendeley Data, V1, doi: 10.17632/cz3xt8mbpn.1
______________________________________________________________________________
### Обзор набора данных
Набор данных содержит гистологические изображения интраоперационного материала и биоптатов синовиальной оболочки от 33 пациентов. Все образцы окрашены гематоксилин-эозином. Каждое изображение разделено сеткой на несколько образцов, образцы  представлено в формате tiff. Данные пациентов представлены Liverpool University Hospitals NHS Foundation Trust, Liverpool. Подготовка препаратов проводилась в этой же клинике. Для создания цифровых 
изображений использован Aperio CS2 Digital Pathology Scanner.
______________________________________________________________________________
### О формате YAML для YOLO
Формат аннотаций набора данных YAML, используемый для обучения моделей сегментации YOLO, выглядит следующим образом: каждое изображение в наборе данных имеет соответствующий текстовый файл с тем же именем, что и файл изображения, и расширением ".txt". Каждая строка в текстовом файле соответствует одному объекту на изображении. Строка представлена в виде: <class-index> <x1> <y1> <x2> <y2> ... <xn> <yn>, где <class-index> - это индекс класса для данного объекта, а <x1> <y1> <x2> <y2> ... <xn> <yn> - пограничные координаты маски сегментации объекта, нормализованные в диапазоне от 0 до 1. Координаты разделены пробелами. 
______________________________________________________________________________
### Аннотирование 
Аннотирование изображений выполнено в программе QuPath-0.5.1. Для аннотации использованы 207 изображений препаратов синовиальной оболочки масштабом 300 нм из набора данных о синовиальной оболочке Объединённого Ливерпульского траста Университетских больниц. Исключены полноразмерные изображения и изображения с сеткой. Разметка изображений производилась с применением элемента «Brush». Полученные таким образом аннотации представлены полигонами. Аннотации последовательно выгружены в формате GeoJson в виде отдельных файлов для каждого изображения с названием, идентичным изображению.
______________________________________________________________________________
### Описание проекта
С помощью написанных функций на языке Python удалены специальные символы, вспомогательная информация о типе объектов, формате аннотаций, применена нормализация координат масок по формулам: x = x/image_width, y = y/image_height, где image_width – ширина изображения, image_height – высота изображения, добавлены метки единственного класса, аннотации сохранены в отдельные текстовые файлы для каждого изображения в поддерживаемом формате YAML. 
______________________________________________________________________________
### Автор: Анастасия Бромберг 
