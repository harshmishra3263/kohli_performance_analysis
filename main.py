from Sensormodule import Sensor
from my_sensor import Accelerometer,Gyro,GPS
import numpy as np

acc=Accelerometer("Accelerometer",
                  "khagaria",
                 "2004-08-04"
                 )
gyro=Gyro(
    name="gyroscope",
    location="Kolkata",
    record_date="2023-01-10"
)

gps=GPS(
    name="GPS",
    location="Delhi",
    record_date="2023-01-05",
    brand="NIKE"
)
time=np.arange(10)
acc_data=np.random.randint(-20,20,10)
gyro_data=np.random.randint(-10,30,10)
gps_data=np.random.randint(-10,5,10)

acc.add_data(data=acc_data,time=time)
gyro.add_data(data=gyro_data,time=time)
gps.add_data(data=gps_data,time=time)

print("Accelerometer data:",acc.data)
print("Gyrometer data:",gyro.data)
print("GPS data:",gps.data)