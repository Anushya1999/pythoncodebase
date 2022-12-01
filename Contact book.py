Contact_book = {}
def display_contact():
       print("Name\t\contact number")
       for key in Contact_book:
              print("{}\t\t{}".format(key, Contact_book.get(key)))

while True:
       choice = int(input(" 1.Add new contact\n 2.Search contact\n 3.Display contact\n 4.Edit contact\n 5.Delete contact\n 6.Exit Enter your choice: "))
       if choice == 1:
              name = input("Enter your name: ")
              phone_num = input("Enter your phone_num: ")
              Contact_book[name] =  phone_num
       elif choice == 2:
              Search_name = input("Enter the contact name: ")
              if Search_name in Contact_book:
                     print(Search_name,"'s contact number is ",Contact_book[Search_name])
              else:
                     print("Name is not fount in contact book")
       elif choice == 3:
              if not Contact_book:
                     print("Empty contact book")
              else:
                     display_contact()
       elif choice == 4:
              edit_contact = input("Enter the contact to edited: ")
              if edit_contact in Contact_book:
                     phone_num = input("Enter mobile num: ")
                     Contact_book[edit_contact] = phone_num
                     print("Contact updated")
                     display_contact()
              else:
                     print("Name is not found in contact book")
       elif choice == 5:
              del_contact = input("Enter the contact to be deleted")

              if del_contact in Contact_book:
                     confirm = input("Do you want to del this contact y/n?")
                     if confirm == 'y' or 'Y':
                            Contact_book.pop(del_contact)
       else:
              break










