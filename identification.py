import cv2
import numpy as np

template = cv2.imread('corner_identifier.PNG', 0)
# template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
img = cv2.imread('Panel_3.PNG', 0)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

cv2.imshow('res.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
