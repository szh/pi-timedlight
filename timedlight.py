import datetime
import time

from gpiozero import LED, Device
from gpiozero.pins.pigpio import PiGPIOFactory

Device.pin_factory = PiGPIOFactory()

# NOTE: Change this to match the GPIO pin you're connecting the LED to
led = LED(18)
# NOTE: Change these values to set the time you want the light to turn on and off at
weekday_on_time = datetime.time(hour=7, minute=0, second=0)
weekday_off_time = datetime.time(hour=17, minute=0, second=0)
weekend_on_time = datetime.time(hour=7, minute=30, second=0)
weekend_off_time = datetime.time(hour=17, minute=0, second=0)

while True:
    dayOfWeek = datetime.datetime.now().weekday()
    currentTime = datetime.datetime.now().time()
    on_time = weekday_on_time if dayOfWeek < 5 else weekend_on_time
    off_time = weekday_off_time if dayOfWeek < 5 else weekend_off_time
    if currentTime > on_time and currentTime < off_time:
        led.on()
    else:
        led.off()

    time.sleep(60)
