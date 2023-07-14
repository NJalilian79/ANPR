import cv2 
#برای بینایی کامپیوتر و پردازش تصویر
from matplotlib import pyplot as plt
#برای ایجاد تجسم های ثابت، متحرک و تعاملی
import numpy as np
import imutils 
#برای ترجمه، چرخش، تغییر اندازه، اسکلت سازی، مرتب سازی خطوط، تشخیص لبه ها 
img = cv2.imread('image5.jpg')
#عکس میخونه داخل برنامه
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#رنگ عکس به طوسی تغییر میده
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
#با استفاده از متپلاتلیب عکس نشون مید, دوباره رنگ دادیم چون انتظارشو داشت
bfilter = cv2.bilateralFilter(gray, 11, 17, 17) 
#نویز کاهش میده
edged = cv2.Canny(bfilter, 30, 200) 
#با استفاده از الگوریتم کنی میتونیم لبه های قاب پلاک تشخیص بدیم ک معلوم بشه پلاک کجای ماشین
plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
#از متد سی وی کالر استفاده میکنیم تا هنگام استفاده از متپلاتلیب عکس درست نشون بده
keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#داخل عکس شکل پیدا میکنه, میاد نتیجه به شکل درخت نمایش میده و بعد با استفاده از الگوریتم اپراکس یک نسخته ساده شده از کانتور با 4 نقطه برای قسمت پلاک میده
contours = imutils.grab_contours(keypoints)
#قستمی ک چجوری قراره کانتور بهمون برگرده سادی سازی میکنه
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
#میاد 10 تا کانتور تاپ مرتب سازی میکنه
#کد پایین میاد بین کانتور ها لوپ میکنه تا ببینه کدومشون یک مربع یا پلاک نشون میدن
location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break
    location
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0,255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)
cnt = contour[0]
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img,[box],0,(0,0,255),2)
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
Orientation=90
if(x!=0) :
      Orientation = np.arctan(x/y) *180/3.14
print('Orientation=',Orientation)
(x,y) = np.where(mask==255)
#هر قسمتی ک مشکی نیست پیدا میکنه و در نتیجه یه سری مختصات از تمام قسمت های اون پلاک میگیریم
(x1, y1) = (np.min(x), np.min(y))
#نقطه ی بالا گوشه سمت چپ پلاک میگیره
(x2, y2) = (np.max(x), np.max(y))
#نقطه ی پایین سمت راست میگیره
cropped_image = gray[x1:x2+1, y1:y2+1]
height, width = cropped_image.shape[:2]
#دوباره یکم فیلتر میکنیم و پلاک از تو عکس کراپ میکنیم
cv2.imshow("mask pic2", cropped_image)
plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)) 
cv2.waitKey(0)
plt.waitforbuttonpress()
plt.close('all')