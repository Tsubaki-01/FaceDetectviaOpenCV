import cv2 as cv
import os
from PIL import Image
import numpy as np
import re
import face_dic_operation
import json
import fnmatch


#   get face datas and label of a face
def get_face_datas_and_labels(top_path):
    #   init
    face_datas = []
    labels = []
    img_paths = []

    face_dic_operator = face_dic_operation.FaceDicOperator()
    face_detector = cv.CascadeClassifier('../haarcascade_frontalface_alt.xml')

    for path in os.listdir(top_path):
        if os.path.isdir(os.path.join(top_path, path)):
            path = os.path.join(top_path, path)
            #   get the image paths
            img_paths = [os.path.join(path, filename) for filename in fnmatch.filter(os.listdir(path), '*.jpg')]
            #   get label from face dictionary by face name
            file_path = os.path.basename(path)
            face_name = file_path
            # re.sub(r'\d+$', '', file_path)
            found_key = face_dic_operator.search_face_in_the_dic_by_value(face_name)

            if int(found_key) < 0:
                if face_dic_operator.add_face_to_the_dic(face_name):
                    found_key = face_dic_operator.search_face_in_the_dic_by_value(face_name)

            label = found_key

            #   loop
            for img_path in img_paths:
                # img = Image.open(img_path)
                # gray_img = img.convert('L')
                img = cv.imread(img_path)
                gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                # img_numpy = np.array(gray_img, 'uint8')    # test
                # faces = face_detector.detectMultiScale(img_numpy)
                # print(faces)  # test

                #   get face data from a certain index
                with open(path + '/face_data.json', 'r') as face_data_dic_file:
                    face_data_dic = json.load(face_data_dic_file)
                face_name_without_extension, _ = os.path.splitext(os.path.split(img_path)[1])
                face_index = re.sub(face_name, '', face_name_without_extension)
                # face_index = re.search(r'\d+$', face_name_without_extension).group(0)
                face = face_data_dic[str(face_index)]

                #   save the face data and the label
                for x, y, w, h in face:
                    labels.append(label)
                    face_datas.append(gray_img[y:y + h, x:x + w])

                    #   test
                    cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=5)  # test
                    cv.imshow('test', img)  # test
                    cv.waitKey(0)  # test
                    cv.destroyAllWindows()  # test

    print('labels,', labels)
    print('fs:', face_datas)
    return face_datas, labels


def train(data_path, save_path):
    #   get face datas and labels
    face_datas, labels = get_face_datas_and_labels(data_path)

    #   init recognizer
    recognizer = cv.face.LBPHFaceRecognizer.create()

    #   train the recognizer
    recognizer.train(np.array(face_datas, dtype=object), np.array(labels, dtype=np.int32))

    #   save the recognizer
    # if not os.path.exists(save_path):
    #     os.makedirs(save_path)
    #
    # full_path = os.path.join(save_path, os.path.basename(save_path) + '.yml')
    recognizer.write(save_path + '/trainer.yml')


if __name__ == '__main__':
    data_path = '../faces_saved'
    save_path = '../trainer'
    train(data_path, save_path)
