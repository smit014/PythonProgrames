class Vehicle:
	def __init__(self,mileage,cost):
		self.mileage = mileage
		self.cost = cost


	def show_details(self):
		print("I am a vehical")
		print('My mileage is ',self.mileage)
		print('my cost is ',self.cost)


v1 =Vehicle(450,600)

v1.show_details()

class Car(Vehicle):
	def show_car(self):
		print("I am a car")

c1 =Car(200,1200)
c1.show_details()
c1.show_car()