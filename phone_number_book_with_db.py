import mysql.connector
from mysql.connector import Error

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="testuser",
        passwd="Password1*",
        database="test_db"
    )

def add_contact(name, surname, phone_number):
    try:
        db = connect_to_db()
        mycursor = db.cursor()
        sql = "INSERT INTO phone_book (name, surname, phone_number) VALUES (%s, %s, %s)"
        val = (name, surname, phone_number)
        mycursor.execute(sql, val)
        db.commit()
        print(mycursor.rowcount, "record inserted.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        mycursor.close()
        db.close()

def remove_contact(criterion, value):
    try:
        db = connect_to_db()
        mycursor = db.cursor()
        sql = f"DELETE FROM phone_book WHERE {criterion} = %s"
        val = (value,)
        mycursor.execute(sql, val)
        db.commit()
        print(mycursor.rowcount, "record(s) deleted.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        mycursor.close()
        db.close()

def show_all_contacts():
    try:
        db = connect_to_db()
        mycursor = db.cursor()
        mycursor.execute("SELECT name, surname, phone_number FROM phone_book")
        results = mycursor.fetchall()
        if results:
            for (name, surname, phone_number) in results:
                print(f"Name: {name}, Surname: {surname}, Phone Number: {phone_number}")
        else:
            print("No contacts found.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        mycursor.close()
        db.close()

def main():
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Show All Contacts")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            name = input("Name: ")
            surname = input("Surname: ")
            while True:
                try:
                    phone_number = int(input("Phone Number: "))
                    break
                except ValueError:
                    print("Please enter a valid phone number.")
            add_contact(name, surname, phone_number)
        
        elif choice == '2':
            print("\nRemove by:")
            print("1. Name")
            print("2. Surname")
            print("3. Phone Number")
            remove_choice = input("Select an option (1-3): ")

            if remove_choice == '1':
                criterion = "name"
            elif remove_choice == '2':
                criterion = "surname"
            elif remove_choice == '3':
                criterion = "phone_number"
            else:
                print("Invalid option.")
                continue

            value = input(f"Enter the {criterion}: ")
            remove_contact(criterion, value)
        
        elif choice == '3':
            show_all_contacts()
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()
