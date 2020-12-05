































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




