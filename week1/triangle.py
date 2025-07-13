

from enum import Enum

class TriangleType(Enum):
	SCALENE = 'scalene'
	ISOSCELES = 'isosceles'
	EQUILATERAL = 'equilateral'

class Triangle:
	sides: list[int]


	def __init__(self, sides: list[int]) -> None:
		for side in sides:
			if not side:
				raise ValueError("A Triangle side cannot be zero")
			if side < 0:
				raise ValueError("Side lengths cannot be negative")
	
		self.sides = sides


	def determineType(self) -> TriangleType:
		s = set(self.sides)

		if len(s) == 1:
			return TriangleType.EQUILATERAL
		elif len(s) == 2:
			return TriangleType.ISOSCELES
		else:
			return TriangleType.SCALENE
		

class App:
	args: list[int]


	def parseInput(self, user_input: list[str]) -> None:
		if len(user_input) > 1:
			if len(user_input) != 4:
				raise NotImplementedError('If using CLI to pass the side lengths, there must be three arguments')
			
			self.args = [int(arg) for arg in user_input[1:] if arg.isdigit()]

			if len(self.args) != 3:
				raise ValueError('Side lengths must be integers')

		else:
			valid = False

			while not valid:
				user_input = input("Enter the side lengths:\n").split(sep=" ", maxsplit=3)
				self.args = [int(arg) for arg in user_input if arg.isdigit()]
				valid = len(self.args) == 3

			print('')

	def outputType(self) -> None:
		triangle = Triangle(self.args)
		triangle_type = triangle.determineType()

		print("The type of triangle with sides {}, {}, and {} is {}".format(*self.args, triangle_type.value))
