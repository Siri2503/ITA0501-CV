import cv2
import numpy as np
  
img = cv2.imread(r"C:\Users\nvisw\OneDrive\Pictures\Saved Pictures\anime.jpg")
  
height, width, c = img.shape
  
i = 0
  
while True:
    i += 1
    l = img[:, :(i % width)]
    r = img[:, (i % width):]
  
    img1 = np.hstack((r, l))
      
    cv2.imshow('animation', img1)
  
    if cv2.waitKey(1) == ord('q'):
        
        cv2.destroyAllWindows()
        break
