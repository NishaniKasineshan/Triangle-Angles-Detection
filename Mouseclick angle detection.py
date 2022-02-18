# importing the module
import cv2
import numpy as np
# function to display the coordinates of the points clicked on the image
lst=[]
def next(s,x,y):
	s= np.array([x,y])
	lst.append(s)
	print(lst)
	print('s=',s)
def calc_angle(a,b,c):
	# lst[0]=a
	# lst[1]=b
	# lst[2]=c
	ba = a - b
	bc = c - b

	cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
	angle = np.arccos(cosine_angle)

	print(round(np.degrees(angle)))
	
def click_event(event, x, y, flags, params):

	# checking for left mouse clicks
	if event == cv2.EVENT_LBUTTONDOWN:
		next('s',x,y)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, str(x) + ',' +
					str(y), (x,y), font,
					1, (255, 0, 0), 2)
		cv2.imshow('image', img)
		
	# checking for right mouse clicks	
	if event==cv2.EVENT_RBUTTONDOWN:
		font = cv2.FONT_HERSHEY_SIMPLEX
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		cv2.putText(img, str(b) + ',' +str(g) + ',' + str(r),(x,y), font, 1,(255, 255, 0), 2)
		cv2.imshow('image', img)

# driver function
if __name__=="__main__":

	# reading the image
	img = cv2.imread('assets/q3.png', 1)

	# displaying the image
	cv2.imshow('image',img)

	# setting mouse hadler for the image
	# and calling the click_event() function
	
	cv2.setMouseCallback('image', click_event)
	# wait for a key to be pressed to exit
	cv2.waitKey(0)
	calc_angle(lst[0],lst[1],lst[2])
	# close the window
	cv2.destroyAllWindows()
