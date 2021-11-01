from time import sleep
from picamera import PiCamera
from gpiozero import Button

button = Button(26)

while True:
    if button.is_pressed:
        print("pic taken in 3")
        sleep(2)
        print("pic taken in 2")
        sleep(2)
        print("pic taken in 1")
        sleep(2)
        print("pic taken")

        camera = PiCamera()
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        sleep(2)
        camera.capture('buttontest3sectimer.jpg', resize=(320, 240))

