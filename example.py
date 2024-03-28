import cv2

img = cv2.imread("aerial-landscape.png")
crop = img[100:200,100:300]
print(type(img), type(crop))

img = cv2.resize(img, (0,0), fx=1.5, fy=1.5)
crop = cv2.resize(crop, (0,0),fx=2.5, fy=2.5)

rows, cols = crop.shape[:2]
for i in range(rows*cols):
    crop[i//cols][i%cols] = crop[i//cols][i%cols]*1.8

cv2.imshow("Original-image", img)
cv2.imshow("Crop-image", crop)

cv2.waitKey(0)
cv2.destroyAllWindows()