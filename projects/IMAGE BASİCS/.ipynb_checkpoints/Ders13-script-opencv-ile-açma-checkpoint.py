import cv2

img = cv2.imread('../DATA/00-puppy.jpg')

while True:
    cv2.imshow("Başlık mı bu ",img)
    
    # İf we have waited at least 1 ms AND if we have pressed "esc" button
    if(cv2.waitKey(1) & 0xFF == 27):
        break
        
cv2.destroyAllWindows()