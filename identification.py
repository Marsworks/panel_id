import cv2
import numpy as np
import math

img = cv2.imread('Panel_2.PNG', 1)
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

if len(centre_coordinates) is 4:
    pt_distance = []
    for i in range(4):
        pt_distance.append(math.sqrt(centre_coordinates[i][0]+centre_coordinates[i][1]))

    coordinate_ordered = zip(pt_distance, centre_coordinates)
    coordinate_ordered = sorted(coordinate_ordered)
    gradient_of_rotation = (coordinate_ordered[0][1][1]-coordinate_ordered[1][1][1]) / \
                           (coordinate_ordered[0][1][0]-coordinate_ordered[1][1][0])
    print(gradient_of_rotation)
    cv2.rectangle(img, coordinate_ordered[0][1], (coordinate_ordered[3][1][0]+w, coordinate_ordered[3][1][1]+h),
                  (0, 0, 255), 1)

cv2.imshow('res', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
