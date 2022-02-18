import cv2
import numpy as np
import math

def calculateDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def checkDistance(x,y,z):
    if x==y==z:
        print("Angle between any two lines =60")
        print("Equilateral triangle")
    elif x==y or y==z or z==x:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
angle_ans=[]
def calc_angle(x,y,z):
    X=np.degrees(np.arccos((y**2+z**2-x**2)/(2*y*z)))
    Y=np.degrees(np.arccos((x**2+z**2-y**2)/(2*x*z)))
    Z=np.degrees(np.arccos((x**2+y**2-z**2)/(2*x*y)))
    angle_ans.append(round(X))
    angle_ans.append(round(Y))
    angle_ans.append(round(Z))
    print("Angle opposite x: ",round(X))
    print("Angle opposite y: ",round(Y))
    print("Angle opposite z: ",round(Z))    

image_obj = cv2.imread('assets/q3.png')

gray = cv2.cvtColor(image_obj, cv2.COLOR_BGR2GRAY)

kernel = np.ones((4, 4), np.uint8)
dilation = cv2.dilate(gray, kernel, iterations=1)

blur = cv2.GaussianBlur(dilation, (5, 5), 0)


thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

# Finding Contours         
contours,hier= cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
coordinates = []
c = max(contours, key=cv2.contourArea)
for cnt in contours:
    # [point_x, point_y, width, height] = cv2.boundingRect(cnt)
    approx = cv2.approxPolyDP(cnt, 0.05 * cv2.arcLength(cnt, True), True)
    if len(approx) == 3:
        print("Triangle")
        coordinates.append([cnt])
        cv2.drawContours(image_obj, [cnt], 0, (0, 0, 255), 3)
# Obtain outer coordinates
#left = tuple(c[c[:, :, 0].argmax()][0])
right = tuple(c[c[:, :, 0].argmax()][0])
top = tuple(c[c[:, :, 1].argmin()][0])
bottom = tuple(c[c[:, :, 1].argmax()][0])

# Draw dots onto image
cv2.drawContours(image_obj, [c], -1, (36, 255, 12), 2)
#cv2.circle(image_obj, left, 8, (0, 255, 255), -1)
cv2.circle(image_obj, right, 8, (0, 255, 255), -1)
cv2.circle(image_obj, top, 8, (255, 50, 0), -1)
cv2.circle(image_obj, bottom, 8, (255, 255, 0), -1)

#print('left: {}'.format(left))
print('right: {}'.format(right))
print('top: {}'.format(top))
print('bottom: {}'.format(bottom))

x=calculateDistance(right[0],right[1],top[0],top[1])
y=calculateDistance(right[0],right[1],bottom[0],bottom[1])
z=calculateDistance(top[0],top[1],bottom[0],bottom[1])
print("x(distance between right and top) :",int(x))
print("y(distance between right and bottom) :",int(y))
print("z(distance between top and bottom) :",int(z))

checkDistance(int(x),int(y),int(z))
calc_angle(x,y,z)
print(angle_ans)

cv2.imshow("result.png", image_obj)
