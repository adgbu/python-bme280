#!/usr/bin/env python

import bme280
from mpu6050 import mpu6050
from time import sleep
from datetime import datetime
import anvil.server
import anvil.tz
import json

def main():
	# Don't commmit Anvil key to repository!
	anvil_key = ""

    # Connect to my dummy app "Material Design 1"
    anvil.server.connect(anvil_key)

    mpu = mpu6050(0x68)
    bme = bme280.Bme280()
    minute = -1

    while True:
        bme.set_mode(bme280.MODE_FORCED)
        t_bme, baro, hygro = bme.get_data()
        #acc = sensor.get_accel_data()
        [acc, gyro, t_mpu] = mpu.get_all_data()

        #print(f"Temperature: {t:.01f} °C")
        #print(f"Pressure: {0.001*p:.03f} kP")
        #print(f"Humidity: {h:.01f}%")
        #print(f"\r{t:.01f}°C {h:.01f}%RH {0.001*p:.03f}kP", end='')

        print("\r %.03fkP %.02f%%RH %.02f°C %.02f°C, acc: %.03f %.03f %.03f, gyro %.03f %.03f %.03f        " %
            (0.001*baro, hygro, t_bme, t_mpu, acc['x'], acc['y'], acc['z'], gyro['x'], gyro['y'], gyro['z']),  end='')

        # Limit server write to once per minute
        now_tz = datetime.now(anvil.tz.tzlocal())
        if now_tz.minute != minute:
            minute = now_tz.minute
            datetime_str = now_tz.strftime('%Y-%m-%dT%H:%M:%S.%f')
            #json = '{ "datetime": "%s", "temp": %.02f, "hygro": %.0f, "baro": %.0f }' % (datetime_str, t_bme, hygro, baro)
            json = f'{{ "datetime": "{datetime_str}", "temp": {t_bme:.02f}, "hygro": {hygro:.02f}, "baro": {baro:.01f} }}'
            print(json)
            anvil.server.call("insert_sensor_sample", json)

        sleep(0.33)


if __name__ == '__main__':
    main()
