# convert_bounding_box

convert object detection segmentation format by YOLO to normal point<br/>
label file is object detection and segmentation.
This code convert the label file into normal points and then draws bounding box on the image.

yolo label file format(.txt)

```
class_index x1 y1 x2 y2 ...
```
x1, y1 data is between 0~1
```
0 0.24266661250000002 0.5240919921875 0.2579943859375 0.547824446875 ...
```

**CAUTION**<br/>
change image and label directory path.
