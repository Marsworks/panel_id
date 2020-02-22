import cv2
import numpy as np

img = cv2.imread('Panel.PNG', 1)
template_1 = cv2.imread('corner_identifier.PNG', cv2.IMREAD_GRAYSCALE)
template_2 = cv2.imread('corner_identifier_inverse.PNG', cv2.IMREAD_GRAYSCALE)
w, h = template_1.shape[::-1]

resolution = 0.7
limit = 7


def check_point(point, pre_point):
    return True if pre_point[0]+limit < point[0] or pre_point[1]+limit < point[1] else False


gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
res_1 = cv2.matchTemplate(gray_img, template_1, cv2.TM_CCOEFF_NORMED)
# res_2 = cv2.matchTemplate(gray_img, template_2, cv2.TM_CCOEFF_NORMED)
centre_coordinates = []

loc = np.where(res_1 >= resolution)
# np.append(loc, np.where(res_2 >= resolution))
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)
    if centre_coordinates:
        if check_point(pt, centre_coordinates[-1]):
            centre_coordinates.append(pt)
    else:
        centre_coordinates.append(pt)

print(centre_coordinates)
if len(centre_coordinates) is 4:
    cv2.rectangle(img, centre_coordinates[0], (centre_coordinates[3][0]+w, centre_coordinates[3][1]+h),
                  (0, 0, 255), 1)

cv2.imshow('res', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
