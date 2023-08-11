import cv2
img = cv2.imread(r"C:\Users\nvisw\OneDrive\Pictures\Saved Pictures\dog.jpg")
wm = cv2.imread(r"C:\Users\nvisw\OneDrive\Pictures\Saved Pictures\girl.jpg")
h_wm, w_wm = wm.shape[:2]
h_img, w_img = img.shape[:2]
top_y = 10
left_x = 10
if top_y + h_wm > h_img or left_x + w_wm > w_img:
    raise ValueError("Watermark dimensions exceed image dimensions")
roi = img[top_y:top_y + h_wm, left_x:left_x + w_wm]
for c in range(0, 3):
    img[top_y:top_y + h_wm, left_x:left_x + w_wm, c] = (
        wm[:, :, c] + roi[:, :, c]
    )
output_path =r"C:\Users\nvisw\OneDrive\Desktop\watermark_img.jpg"
cv2.imwrite(output_path, img)
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
