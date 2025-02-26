class Car:
    """자동차 클래스 """
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading= 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.make}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"이 차의 주행거리는 {self.odometer_reading}")

    def update_odometer(self,mileage):
        if mileage >=self.odometer_reading:
            self.odormeter_reading = mileage
        else : 
            print("주행기록계를 줄일 수 없다")
    
    def increment_odometer(self,miles):
        self.odometer_reading += miles

my_new_car = Car('audi','a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reding= 33
my_new_car.read_odometer()
my_new_car.update_odometer(11)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

class Battery:
    """배터리"""
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"차량 배터리 크기는 {self.battery_size}")

class ElectricCar(Car):
    """전기차"""
    def __init__(self,make,model,year, large_battery=Battery): #디폴트 파라미터
        super().__init__(make,model,year)
        self.battery = large_battery

    def describe_battery(self):
       return(f"이 차 배터리 용량은 {self.battery.battery_size}")
    
    def get_descriptive_name(self):
        print(super().get_descriptive_name())
        print(f"차량 배터리 크기는 {self.battery_size}")

my_leaf= ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
print(f"배터리 크기는 {my_leaf.describe_battery}")
my_leaf.get_descriptive_name()
my_car = Car('Bentz','E200',2023)
print(f"차 제원은{my_car.get_descriptive_name()}")
my_leaf.battery.describe_battery()  #하위 구성 객체 사용

large_battery = Battery(80)
large_battery_car= ElectricCar('nissan','leaf',2024,large_battery)

