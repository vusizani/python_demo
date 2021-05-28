class Person:
	def __init__(self, firstName, lastName, age, email, middleName=None):
		self.firstName = firstName
		self.lastName = lastName
		self.age = age
		self.email = email
		self.middleName = middleName

	def personDetails(self):
		person = f"Name: {self.firstName} \nMiddle Name: {self.middleName} \nSurname: {self.lastName} \nAge: {self.age} \nEmail: {self.email}\n"
		return person


heino = Person("Heino","du Plisses",26,"heino@gmail.com")
lesedi = Person("Lesedi","Tumelo", 20, "lesedi@gmail.com", "Mbali")

print(heino.personDetails())
print(lesedi.personDetails())