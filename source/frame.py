# pylint: disable=E1101
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

i = 0
while( i <= 1):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    input('Press Enter to capture')
    return_value, image = cap.read()
    cv2.imwrite('opencvgabs' + str(i) + '.png', image)
    i+=1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()