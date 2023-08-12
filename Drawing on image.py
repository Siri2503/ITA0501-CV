import numpy as np  
import cv2  
img = cv2.imread(r"C:\Users\nvisw\OneDrive\Pictures\Saved Pictures\dora.jpeg",1)  
cv2.circle(img,(80,80), 55, (0,255,0), -1)  
cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  
