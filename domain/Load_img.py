# load img
import cv2 as cv

img = cv.imread('../imgs/img1.jpg')


# bgr to gray
gray_img = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)

# save the gray img
cv.imwrite('../imgs/gray_img1.jpg', gray_img)

#
# # resize the img
# resize_img = cv.resize(img, dsize=(200, 200))
# cv.imwrite('../imgs/resize_img1.jpg',resize_img)
#
# # show the resized img
# if resize_img is not None and resize_img.shape[0] > 0 and resize_img.shape[1] > 0:
#     cv.imshow('resized img1', resize_img)
# else:
#     print("图像加载失败或尺寸无效")
#
# # show the size
# print('original:', img.shape)
# print('resized:', resize_img.shape)
#
# # draw detective box
# cv.rectangle(img, rec=(0, 0, 30, 30), color=(0, 0, 255), thickness=2)
# cv.circle(img, center=(20, 20), radius=20, color=(0, 255, 0), thickness=4)
#
# face_detect(img)

# show the img
if img is not None and img.shape[0] > 0 and img.shape[1] > 0:
    cv.imshow('img1', img)
else:
    print("图像加载失败或尺寸无效")

# get the video
# cap=cv.VideoCapture('../videos/video2.mp4')
# cap = cv.VideoCapture(0)
#
# # wait
# while True:
#     flag, frame = cap.read()
#     if not flag:
#         break
#     face_exist(frame)
#     if ord('q') == cv.waitKey(1):
#         break
#
# # release
# cv.destroyAllWindows()
#
# cap.release()
