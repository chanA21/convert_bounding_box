
import numpy as np
import cv2
import os
import glob


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")


def readDirPath(img_dir_path, label_dir_path):
    # image save path : ./bbox
    bbox_path = os.path.abspath(os.path.join(img_dir_path, os.pardir))
    bbox_path = os.path.join(bbox_path, "bbox")
    createDirectory(bbox_path)

    # file read to list
    label_file_path_list = glob.glob(os.path.join(label_dir_path, "*.txt"))
    image_file_path_list = glob.glob(os.path.join(img_dir_path, "*.JPG"))

    if len(label_file_path_list) == len(image_file_path_list):
        for i in range(0, len(label_file_path_list)):
            convert_bbox(image_file_path_list[i], label_file_path_list[i], bbox_path)
    else:
        print("Error : image file and label file number are not same")


def convert_bbox(img_path, label_path, bbox_path):
    # image save path : ./bbox
    bbox_image = os.path.basename(img_path)     # 처리할 파일명 가져오기
    bbox_image_path = os.path.join(bbox_path, bbox_image)

    # set color
    color = (0, 0, 255)     # red

    # read image with opencv
    img = cv2.imread(img_path)
    h, w, _ = img.shape

    # read file
    f = open(label_path, "r")
    label = f.read()

    # class split
    class_list = label.split("\n")
    class_len = len(class_list)

    # label split & reshape [[[x1, y1], [x2, y2] ...], [[x1, y2], ...]]
    for i in range(0, class_len):
        class_list[i] = class_list[i].split()
        class_list[i].pop(0)    # class data pop
        class_list[i] = np.reshape(class_list[i], (-1, 2))  # reshape
        class_list[i] = np.asarray(class_list[i], dtype='float64')

        label_len = len(class_list[i])

        # remove YOLO point format
        for j in range(0, label_len):
            class_list[i][j][0] *= w
            class_list[i][j][1] *= h

        class_list[i] = np.asarray(class_list[i], dtype='int32')
        # draw bounding box
        img = cv2.polylines(img, [class_list[i]], True, color, 2)


    cv2.imwrite(bbox_image_path, img)
    # cv2.imshow("polylines", img)
    # cv2.waitKey(0)


if __name__ == '__main__':
    # init file path
    path = os.getcwd()

    # change the directory name
    label_dir_path = os.path.join(path, "label")
    img_dir_path = os.path.join(path, "image")


    readDirPath(img_dir_path, label_dir_path)
