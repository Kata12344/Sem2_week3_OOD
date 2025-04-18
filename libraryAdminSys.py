#Library Administration System

members = []
books = []

class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.myBooks = []

    def __str__(self):
        return f"{self.name}, {self.age}"

    def add_book(self, book):
        self.myBooks.append(book)

    def return_book(self, book):
        myBooks_list = list(self.myBooks)
        for i in myBooks_list:
            if myBooks_list.index(i) == book:
                myBooks_list.remove(i)

        new_tuple = tuple(myBooks_list)
        for i in new_tuple:
            message = i.__str__() + "\n"
            print(message)

    def print_mybooks(self):
        message = self.name + "\n"
        message += "-----------------\n"
        for i in self.myBooks:
            message += i.__str__() + "\n"
            print(message)
            # print(self.name, i.__str__())



member1 = Member("Lucy",11)
member2 = Member("Ryan",24)
member3 = Member("Mike",65)

members.append(member1)
members.append(member2)
members.append(member3)


class Book:
    def __init__(self, type, title, author):
        self.type = type
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.type}, {self.title}, {self.author}"




book1 = Book("magazine","Nok Lapja","God")
book2 = Book("book","Love","Micheal Jackson")
book3 = Book("magazine","Boss","Bob Ross")
book4 = Book("book","Rock & Roll","Justin Timberlake")
book5 = Book("book","Valami","Hannah Montana")

books.append(book1)
books.append(book2)
books.append(book3)
books.append(book4)
books.append(book5)

def main():
    print("Welcome to the Library Administration System")

    while True:
        print("\nWhat would you like to do?")
        print("1. Add Member")
        print("2. Add a book to a member")
        print("3. Return a book from a member")
        print("4. Exit\n")

        choice = int(input("Choose between 1-4: "))

        #Add new member
        if choice == 1:
            name = input("\nEnter the new member's name: ")
            age = int(input("Enter the new member age: "))
            member = Member(name, age)
            members.append(member)
            print("\nCurrent members:")
            print_list(members)

        #Add a book to a member
        elif choice == 2:
            print("\nCurrent books: ")
            print_list(books)
            chosenBook = validate_chosenNumber(books, "book")

            print("\nCurrent members: ")
            print_list(members)
            chosenMember = validate_chosenNumber(members, "member")

            for i in members:
                if chosenMember == members.index(i):
                    book = find_book(chosenBook)
                    i.add_book(book)
                    i.print_mybooks()

        #Return a book from a member
        elif choice == 3:
            print_list(members)
            returnMember = int(input("Choose a member number: "))
            returnBook = int(input("Which book do you want to return?: "))

            for i in members:
                if members.index(i) == returnMember:
                    print("\n"+i.name+"'s current books:")
                    i.return_book(returnBook)
            
        #Exit from the program
        elif choice == 4:
            break

        else:
            print("\nInvalid number!")

        


def find_book(chosenBook):
    for i in books:
        if chosenBook == books.index(i):
            return i

def print_list(list):
    counter = 0
    for i in list:
        print("ID:",counter, i.__str__())
        counter+=1

def validate_chosenNumber(list, text):
    while True:
        chosenNumber = int(input(f"\nChoose a {text} number: "))
        if 0 <= chosenNumber < len(list):
            print("You choose:", list[chosenNumber])
            return chosenNumber
            break
        else:
            print(f"Invalid choice! Please enter a number between 0 and", len(list)-1)


main()