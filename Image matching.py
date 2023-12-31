import numpy as np
import cv2

query_img = cv2.imread(r"C:\Users\nvisw\OneDrive\Pictures\Saved Pictures\book.jpg")
train_img = cv2.imread(r"C:\Users\nvisw\OneDrive\Pictures\Saved Pictures\book.jpg")

query_img_bw = cv2.cvtColor(query_img,cv2.COLOR_BGR2GRAY)
train_img_bw = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()


queryKeypoints, queryDescriptors = orb.detectAndCompute(query_img_bw,None)
trainKeypoints, trainDescriptors = orb.detectAndCompute(train_img_bw,None)


matcher = cv2.BFMatcher()
matches = matcher.match(queryDescriptors,trainDescriptors)

final_img = cv2.drawMatches(query_img, queryKeypoints,
train_img, trainKeypoints, matches[:20],None)

final_img = cv2.resize(final_img, (1000,650))

cv2.imshow("Matches", final_img)
cv2.waitKey(3000)
