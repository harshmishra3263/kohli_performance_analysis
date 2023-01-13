# class Student(object){
#     def __init__(self,para1,para2)
#         self.para1=para1
#         self.para2=para2
#     def get_marks(para1):
#         return 


# # }
# class SuperHeroes():
#     def __init__(self,name,superpower):
#         self.name=name
#         self.superpower=superpower

#     def get_superpower(self):
#         print(f"\nI am {self.name} and my power is {self.superpower}")

# super_heroes=SuperHeroes(name="Ironman",superpower="Suit")
# super_heroes.get_superpower()    
# Ironman=SuperHeroes(name="Ironman",superpower="Suit")
# print(Ironman.name)
# print(Ironman.superpower)
# Ironman.get_superpower()


# thor=SuperHeroes(name="thor",superpower="Hammar")
# print(thor.name)
# print(thor.superpower)
#thor.get_superpower()
#Inheritance
class Sensor():
    def __init__(self,name,purpose):
        self.name=name
        self.purpose=purpose
    def get_version(self,version):
        print(f"{self.name} is of  {version}")
class Accelator(Sensor):
    def show_sensor(self):
        print(f"I am {self.name}")
        
    accel=Accelator(name="Accelometer",purpose="Get away errors")


