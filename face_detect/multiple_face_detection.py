import dlib
import cv2



detector = dlib.get_frontal_face_detector()
img = cv2.imread('./test_img/test.png')
im = img
# img = cv2.resize(img ,(int(img.shape[0]/1.25) ,int(img.shape[1]/1.25)))
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
faces = detector(img)

for d in faces:
    print "left,top,right,bottom:", d.left(), d.top(), d.right(), d.bottom()
    cv2.rectangle(im, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0,255), 2)

cv2.imwrite('./results/result.png',im)
win = dlib.image_window()
win.set_image(img)
win.add_overlay(faces)

win.wait_until_closed()