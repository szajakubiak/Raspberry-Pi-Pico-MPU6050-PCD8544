from machine import Pin, SPI, I2C
import pcd8544_fb
from mpu6050 import MPU6050
from time import sleep

spi = SPI(1, 2000_000, polarity=0, phase=0)
i2c = I2C(0, scl=Pin(17), sda=Pin(16))

cs = Pin(13)
dc = Pin(19)
rst = Pin(15)

lcd = pcd8544_fb.PCD8544_FB(spi, cs, dc, rst)
lcd.contrast(0x2f, pcd8544_fb.BIAS_1_40, pcd8544_fb.TEMP_COEFF_0)

mpu = MPU6050(i2c)

# Accelerometer correction factors from the calibration script:
a_corr_x = 0.020
a_corr_y = 0.002
a_corr_z = -0.043

# Gyro correction factors from the calibration script:
g_corr_x = -2.333
g_corr_y = 0.188
g_corr_z = -1.141

counter = 0
while True:
    if counter < 20:
        data = mpu.get_accel_data(i2c)   # in g
        data[0] -= a_corr_x
        data[1] -= a_corr_y
        data[2] -= a_corr_z
    else:
        data = mpu.get_gyro_data(i2c)   # in deg./s
        data[0] -= g_corr_x
        data[1] -= g_corr_y
        data[2] -= g_corr_z
    
    lcd.fill(0)
    lcd.text(" MPU6050", 0, 0, 1)
    lcd.text("accel.:" if counter < 20 else "gyro:", 0, 8, 1)
    lcd.text("x:%s%.3f" % ("" if data[0] < 0 else " ",
                           data[0]), 0, 16, 1)
    lcd.text("y:%s%.3f" % ("" if data[1] < 0 else " ",
                           data[1]), 0, 24, 1)
    lcd.text("z:%s%.3f" % ("" if data[2] < 0 else " ",
                           data[2]), 0, 32, 1)
    lcd.show()
    
    sleep(0.25)
    
    counter += 1
    if counter >= 40:
        counter = 0
