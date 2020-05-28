import sys
class Library:
	def __init__(self,listofbooks):
		self.availablebooks = listofbooks
	def displayAvailablebook(self):
		print("The books we have in our library are: ")
		for book in self.availablebooks:
			print(book)
	def lendbook(self,requestedbook):
		if requestedbook in self.availablebooks:
			print("Thanks for choosing the book")
		else:
			print("sorry, This book is out of stock")
	def addBook(self,returnbook):
		self.availablebooks.append(returnbook)
		print("Thanks for returning your borrowed book")
			

class Student:
	def requestedbook(self):
		print("Enter the name of the book you would like to lend: ")
		self.book=input()
		return self.book

	def returnbook(self):
		print("Enter the book you would like to return: ")
		self.book=input()
		return self.book

def main():
	library=Library(["The middle march","Mahabharata","Wings of fire","The race of my life"])
	student=Student()
	print("""************LIBRARY MENU********** 
	 		1. Display all availbale books
	 		2. Request a book
	 		3. Return a book
	 		4. Exit 
	 		""")
	choice=int(input("Enter choice:"))
	if choice==1:
		library.displayAvailablebook()
	elif choice==2:
		library.lendbook(student.requestedbook())
	elif choice==3:
	    library.addBook(student.returnbook())
	elif choice==4:
	    sys.exit()

main()	


        	
        	
        	



		

			
			