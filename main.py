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

while True:
    accel_data = mpu.get_accel_data(i2c)
    
    lcd.fill(0)
    lcd.text("MPU6050:", 0, 0, 1)
    lcd.text("x:%s%.3f" % ("" if accel_data[0] < 0 else " ",
                           accel_data[0]), 0, 8, 1)
    lcd.text("y:%s%.3f" % ("" if accel_data[1] < 0 else " ",
                           accel_data[1]), 0, 16, 1)
    lcd.text("z:%s%.3f" % ("" if accel_data[2] < 0 else " ",
                           accel_data[2]), 0, 24, 1)
    lcd.show()
    
    sleep(0.5)
