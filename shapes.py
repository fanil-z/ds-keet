class Polygon:
	def __init__(self, sides, name):
		self.sides = sides
		self.name = name

square = Polygon(4, "Square")
pentagon = Polygon(5, "Pentagon")

print(square.sides)
print(square.name)

