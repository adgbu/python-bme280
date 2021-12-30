#!/usr/bin/env python

import bme280
from mpu6050 import mpu6050
from time import sleep


def main():
    mpu = mpu6050(0x68)
    bme = bme280.Bme280()

    while True:
        bme.set_mode(bme280.MODE_FORCED)
        t_bme, baro, hygro = bme.get_data()
        #acc = sensor.get_accel_data()
        [acc, gyro, t_mpu] = mpu.get_all_data()

        #print(f"Temperature: {t:.01f} °C")
        #print(f"Pressure: {0.001*p:.03f} kP")
        #print(f"Humidity: {h:.01f}%")
        #print(f"\r{t:.01f}°C {h:.01f}%RH {0.001*p:.03f}kP", end='')

        print("\r %.03fkP %.01f%%RH %.01f°C %.01f°C, acc: %.03f %.03f %.03f, gyro %.03f %.03f %.03f        " %
            (0.001*baro, hygro, t_bme, t_mpu, acc['x'], acc['y'], acc['z'], gyro['x'], gyro['y'], gyro['z']),  end='')

        sleep(0.33)


if __name__ == '__main__':
    main()
