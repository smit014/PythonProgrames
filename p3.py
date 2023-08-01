class Employee:

	def  __init__(self,name,age,salary,gender):
		self.name = name
		self.age = age
		self.salary = salary
		self.gender = gender


	def employee_details(self):
		print("emloyee name is ",self.name)
		print("emloyee age is ",self.age)
		print("emloyee salary is ",self.salary)
		print("emloyee gender is ",self.gender)


e1 =Employee("raj",20,25000,'male')
e2 = Employee("smith",18,40000,'male')
e1.employee_details()
e2.employee_details()	