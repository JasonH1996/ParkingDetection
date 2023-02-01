import cv2
import RPi.GPIO as GPIO
import time
import matplotlib
GPIO.setmode(GPIO.BCM)
data_input_pin = 18
GPIO.setup(data_input_pin,GPIO.IN)

icount=0
icount_signal = 0
input_save = 0

cam = cv2.VideoCapture(0)
time.sleep(2)

print("ok go")
def laserCapture():
    icount=0
    icount_signal = 0
    input_save = 0
    while icount_signal < 1:
        result,image = cam.read()
        if GPIO.input(data_input_pin):
            icount += 1
            input_save=1
        else:
            if input_save==1:
                #print(icount_signal)
                icount_signal += 1
    input_save=0
    return image

def capture(num,image):
    #print("press enter")
    #input()
    #result,image = cam.read()
    cv2.imshow("test",image)
    cv2.waitKey(1000)

    cv2.imwrite(f"/home/pi/Desktop/Tests/cars_normal/image{num}.jpg",image)
    
for i in range(1,100):


    print("go again")

    image = laserCapture()
    capture(i,image)
cv2.destroyAllWindows()
print('\n -- end --\n') 
