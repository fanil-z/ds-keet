class Math:

	@staticmethod
	def add5(x):
		return x+5

	@staticmethod
	def mult2(x):
		return x*2

print(Math.mult2(22))



# class Person:
# 	number_of_people = 0

# 	def __init__(self, name):
# 		self.name = name
# 		Person.add_person()

# 	@classmethod
# 	def number_of_people_(cls):
# 		return cls.number_of_people

# 	@classmethod
# 	def add_person(cls):
# 		cls.number_of_people += 1


# p1 = Person('Joelle')
# p2 = Person('Ortho')
# p3 = Person('Remy')

# print(Person.number_of_people_())




# # Upper-level parent class
# class Pet:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def show(self):
# 		print(f'I am {self.name} and I am {self.age} years old')

# #Child classes that inherit from Pet class
# class Cat(Pet):
# 	def __init__(self, name, age, color):
# 		super().__init__(name, age)  # inherit other attributes from the super class
# 		self.color = color

# 	def speak(self):
# 		print('Meow')

# 	def show(self):
# 		print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')

# class Dog(Pet):
# 	def speak(self):
# 		print('Woof')
 

# p = Pet('Bill', 19)
# p.show()
# c=Cat('Sue', 5, 'green')
# c.show()
# d = Dog('Wahren', 2)










# class Student:
# 	def __init__(self, name, age, grade):
# 		self.name = name
# 		self.age = age
# 		self.grade = grade

# 	def get_grade(self):
# 		return self.grade

# # class to add students to the course
# class Course:
# 	def __init__(self, name, max_students):
# 		self.name = name
# 		self.max_students = max_students
# 		self.students = []

# 	def add_student(self, student):
# 		if len(self.students) < self.max_students:
# 			self.students.append(student)
# 			return True
# 		return False

# 	def get_average_grade(self):
# 		value = 0
# 		for student in self.students:
# 			value += student.get_grade()

# 		return value/len(self.students)

# s1 = Student('Orin', 17, 95)
# s2 = Student('Hal', 15, 74)
# s3 = Student('Pemulis', 16, 45)

# course = Course('Science', 2)
# course.add_student(s1)
# course.add_student(s2)
# course.add_student(s3)

# print(course.get_average_grade())








# class Dog:
	
# 	def __init__(self, name, age):
# 		self.name = name         # attribute of the class dog
# 		self.age = age

# 	def get_name(self):
# 		return self.name

# 	def get_age(self):
# 		return self.age

# 	def set_age(self, age):
# 		self.age = age

# 	def bark(self):
# 		print('woof')

# d = Dog('OStice', 15)
# # print(d.add_one(5))
# d.set_age(22)
# print(d.get_age())




