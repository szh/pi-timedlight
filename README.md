# pi-timedlight
A simple Raspberry Pi project to turn a LED on and off on a schedule.

Example use case: Put in a toddler's room and set to turn on in the morning and off in the evening.
Toddler can be instructed to go back to bed if they wake up and the light is still off.

Developed for the Pi Zero. Uses 1 LED.

# Installing
On your Pi:
```bash
sudo apt-get update
sudo apt-get install python3-pip python-dev pigpio
sudo pip3 install gpiozero pigpio

nano /etc/rc.local
```
Now add the following text before `exit 0`:

```bash
pigpiod
python3 /home/pi/timedlight.py > /home/pi/log.txt &
```

Run `sudo raspi-config`, go into "Localization Options" and set your timezone.

**Important:** You must make sure that your Pi will sync with a time server on a regular basis.
```bash
sudo timedatectl set-ntp true
sudo nano /etc/systemd/timesyncd.conf
# Uncomment the last two lines:
PollIntervalMinSec=32
PollIntervalMaxSec=2048
# Save the file.
```

Exit and reboot (`sudo reboot`).

Check out comments in the code for configuration options.
