import cv2 as cv
import face_detect
from save_img import save_image
import json


def save_face_through_capture(name):
    # get the capture
    cap = cv.VideoCapture(0)

    # number the faces saved
    num = 1

    while cap.isOpened():  # while capture is working
        #   read the capture
        flag, frame = cap.read()
        cv.imshow('capture test:', frame)

        #   constantly get the order
        key = cv.waitKey(1)

        #   save
        if ord('s') == key:
            faces = face_detect.FaceDetector.face_exist(frame)
            if len(faces):
                #   only one face in the picture
                if 1 == len(faces):

                    #   save image and then show the image rectangled
                    save_image(frame, '../faces_saved/' + str(name), str(name) + str(num) + '.jpg')
                    for x, y, w, h in faces:
                        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
                        cv.imshow('test', frame)
                        cv.waitKey(500)
                        cv.destroyAllWindows()

                    #   save the face data to face data dictionary
                    if num == 1:
                        face_data_dic = {}
                    else:
                        with open('../faces_saved/' + str(name) + '/face_data.json', 'r') as face_data_dic_file:
                            face_data_dic = json.load(face_data_dic_file)
                    with open('../faces_saved/' + str(name) + '/face_data.json', 'w') as face_data_dic_file:
                        face_data_dic[num] = faces.tolist()
                        json.dump(face_data_dic, face_data_dic_file)

                    print('succeed saving')
                    print('.....')
                    num += 1
                # more than one face detected
                else:
                    print('there can be only one face in the image')
            #   no face detected
            else:
                print('no face detected\n......')

        #   quit
        elif ord('q') == key:
            break

    # release
    cap.release()

    cv.destroyAllWindows()


if __name__ == '__main__':
    save_face_through_capture('test2')
