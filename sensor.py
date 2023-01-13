class Sensor():
    def __init__(self,name,location,record_date):
        self.name=name
        self.location=location
        self.record_date=record_date
        self.data={}

    def add_data(self,time,data):
            self.data["data"]=data
            self.data["time"]=time
            print(f"Received {len(data)} point")



    def clear_data(self):
            self.data={}
            print("Data cleared!!")
            
import numpy as np

Sensor1=Sensor(
        name="sensor1",
        location="Haldia",
        record_date="2023-01-09"
)
print(Sensor1.name,Sensor1.location,Sensor1.record_date)

data=np.random.randint(-10,10,10)
time=np.arange(10)

print(data)
print(time)
Sensor1.add_data(
    time=time,
    data=data
)
print(Sensor1.add_data)


# print(-------------------------)
class Accelerometer(Sensor):
    def show_type(self):
        print(f"I am an {self.name}")
acc=Accelerometer("Accelerometer",
                  "khagaria",
                 "2004-08-04")
acc.show_type()                 
acc_data=np.random.randint(-10,10,10)
acc_time=np.arange(10)
acc.add_data(data=acc_data,time=acc_time)
print(acc.data)


print("--------------------------------------------")

class Gyro(Accelerometer):
    def show_type(self):
        print(f"This is {self.name} and location is {self.location}")
gyro=Gyro(
    name="gyroscope",
    location="Kolkata",
    record_date="2023-01-10"
)
gyro_data=np.random.randint(-25,5,10)
gyro_time=np.arange(10)
gyro.add_data(
    data=gyro_data,
    time=gyro_time
)        
gyro.show_type()

class GPS(Sensor):
    def __init__(self,name,location,record_date,brand):
        super().__init__(
            name,location,record_date
        )
        self.brand=brand
print("#################################")
gps=GPS(name="GPS",
        location="Delhi",
        record_date="2023-01-05",
        brand="NIKE"
)
print(gps.name,gps.location,gps.record_date)
print(gps.brand)