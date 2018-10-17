students = []


class Student:

	school_name = "Springfield Elementary"

	def __init__(self, name, student_id=332, last_name="NA"):
		"""
		Adds the student to the student list
		:param name: string - student name
		:param student_id: integer - optional student ID
		:param last_name: string - optional student last name
		"""
		self.name = name
		self.student_id = student_id
		self.last_name = last_name
		students.append(self)

	def __str__(self):
		return "Student " + self.name

	def get_name_capitalize(self):
		return self.name.capitalize()

	def get_school_name(self):
		return self.school_name
