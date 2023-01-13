class Sensor():
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self._record_date="2023-01-10"
        self._version="0.001"
        self.data={}

    def add_data(self,time,data):
            self.data["data"]=data
            self.data["time"]=time
            print(f"Received {len(data)} point")
    def get_record_date(self):
             print(f"The record date for{self.name} is {self._record_date}")
    def get_version(self):
            print(f"The version for{self.name} is {self._version}")
    def set_vesion(self,version):
        self._version=version
        print(f"The version for {self.name} is {self._version}")
    def add_data(self,time,data):
        self.data["data"]=data
        self.data["time"]=time
        print(
            f"Received{len(data)} point"
        )


    def clear_data(self):
            self.data={}
            print("Data cleared!!")
 
sensor1=Sensor(
    name="Sensor1",
    location="Kolkata"

 )
print(sensor1.name)
print(sensor1.location)

sensor1.get_record_date()
sensor1.get_version()
sensor1.set_vesion("0.009")
sensor1.get_version()