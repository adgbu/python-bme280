from mpu6050 import mpu6050
from time import sleep

sensor = mpu6050(0x68)
#accelerometer_data = sensor.get_accel_data()
while True:
    #acc = sensor.get_accel_data()
    #print(f"\rX: {acc['x']:.03f} Y: {acc['y']:.03f} Z: {acc['z']:.03f}", end='')
    [acc, gyro, temp] = sensor.get_all_data()
    print("\racc: %.03f %.03f %.03f, gyro %.03f %.03f %.03f, temp %.01f°C          " % (acc['x'], acc['y'], acc['z'], gyro['x'], gyro['y'], gyro['z'], temp),  end='')
    sleep(0.33)
