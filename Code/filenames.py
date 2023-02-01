from time import sleep
from picamera import PiCamera
from pathlib import Path

base_folder = Path(__file__).parent.resolve()

camera = PiCamera()
camera.start_preview()
sleep(2)
for filename in camera.capture_continuous(f"{base_folder}/image_{counter:03d}.jpg"):
    print(f'Captured {filename}')
    sleep(300) # wait 5 minutes