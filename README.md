# Pico with Nokia screen and MPU6050 accelerometer and gyro
MicroPython script to display the accelerometer and gyroscope data on the screen from Nokia phone using Raspberry Pi Pico microcontroller.

![Project image](img/project_img.jpg?raw=true)

## Detailed description
Schematic of the connections can be found in the connections.pdf file. Calibration scripts can be used to calculate correction factors for both accelerometer and gyroscope. In case of the accelerometer each correction factor needs to be calculated separately by placing MPU6050 module in a position where calibrated axis is facing upwards. Documentation on how to use MicroPython on the Raspberry Pi Pico can be found [here](https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf).

## Dependencies
You need two libraries to run this script:

[PCD8544](https://github.com/mcauser/micropython-pcd8544)

[MPU6050](https://github.com/mytechnotalent/MicroPython_MPU6050)

pcd8544_fb.py and mpu6050.py files should be copied into the /lib directory crated in the main directory of the microcontroller.
