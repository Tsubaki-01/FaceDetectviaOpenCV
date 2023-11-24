import cv2 as cv
from face_dic_operation import FaceDicOperator
from warning import warning


class FaceDetector:

    def __init__(self):
        self.warntime = 0

    # detect whether there is a face
    @staticmethod
    def face_exist(img):  # img should be already opened

        gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        face_detector = cv.CascadeClassifier('../haarcascade_frontalface_default.xml')
        faces = face_detector.detectMultiScale(gray_img, 1.1, 5, 0, (200, 200))
        # faces = face_detector.detectMultiScale(gray_img)

        # rectangle the faces
        # for x, y, w, h in faces:
        #     cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=5)

        return faces

    #   detect face by trained recognizer
    def face_detect(self, img):  # img should be already opened
        #   init the recognizer
        recognizer = cv.face.LBPHFaceRecognizer.create()
        recognizer.read('../trainer/trainer.yml')

        #   get the faces list
        gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = FaceDetector.face_exist(img)

        #   recognize the face
        for x, y, w, h in faces:
            cv.rectangle(img, (x, y), (x + w, y + h), color=(0.0, 255), thickness=5)
            label, uncertainty = recognizer.predict(gray_img[y:y + h, x:x + w])
            #   face not be recorded
            if uncertainty > 60:
                self.warntime += 1
                if self.warntime >= 100:
                    warning()
                    self.warntime = 0
                cv.putText(img, 'unknown', (x + 10, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            #   face be recorded
            else:
                cv.putText(img, str(FaceDicOperator.search_face_in_the_dic_by_key(str(label))), (x + 10, y - 10),
                           cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
        cv.imshow('result:', img)

        # cv.waitKey(0)    #   test
        # cv.destroyAllWindows()    #   test


if __name__ == '__main__':
    face_detector1 = FaceDetector()
    # face_detector1.face_detect(cv.imread('../faces_saved/test/test4.jpg'))
    cap = cv.VideoCapture(0)
    while cap.isOpened():
        flag, frame = cap.read()
        face_detector1.face_detect(frame)

        key = cv.waitKey(1)
        if ord('q') == key:
            break

    cv.destroyAllWindows()
