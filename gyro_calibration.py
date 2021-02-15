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

measurements = 100
counter = 0
sum_x = 0
sum_y = 0
sum_z = 0

while counter < measurements:
    lcd.fill(0)
    lcd.text("Measuring", 0, 0, 1)
    lcd.text(str(counter), 0, 8, 1)
    lcd.show()
    
    gyro_x, gyro_y, gyro_z = mpu.get_gyro_data(i2c)
    sum_x += gyro_x
    sum_y += gyro_y
    sum_z += gyro_z
    
    sleep(0.01)
    counter += 1

corr_x = sum_x / measurements
corr_y = sum_y / measurements
corr_z = sum_z / measurements

lcd.fill(0)
lcd.text(" Results", 0, 0, 1)
lcd.text("gyro", 0, 8, 1)
lcd.text("x:%s%.3f" % ("" if corr_x < 0 else " ", corr_x), 0, 16, 1)
lcd.text("y:%s%.3f" % ("" if corr_y < 0 else " ", corr_y), 0, 24, 1)
lcd.text("z:%s%.3f" % ("" if corr_z < 0 else " ", corr_z), 0, 32, 1)
lcd.show()