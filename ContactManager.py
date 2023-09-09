"""Contact Book: Develop a contact book application
to store and manage contact information."""
import sqlite3


# con = sqlite3.connect("E:\\rejoice\\contacts.db")
# cur = con.cursor()
# cur.execute("DROP table contacts;")
def ConnectDatabase():
    global con
    global cur
    con = sqlite3.connect("E:\\rejoice\\contacts.db")
    cur = con.cursor()


def CreateContactDatabase(con, cur):
    cur.execute(
        """CREATE TABLE contacts (
        Name text NOT NULL,
        LastName text NOT NULL,
        PhoneNumber int(10) primary key,
        Address text NOT NULL);"""
    )
    con.close()


def AddContact(con, cur):
    name = input("Enter the Name of the Contact: ")
    last_name = input("Enter the Last Name of the Contact: ")
    phone_number = int(input("Enter the Phone Number of the Contact: "))
    address = input("Enter the Address of the Contact: ")
    cur.execute(
        "INSERT INTO contacts (Name, LastName,PhoneNumber,Address) VALUES (?, ?, ?, ?)",
        (name, last_name, phone_number, address),
    )
    con.commit()


def ViewContact(cur):
    cur.execute("SELECT * FROM contacts  ORDER BY Name")
    rows = cur.fetchall()
    print("| Name | LastName |  PhoneNO | Address |")
    print("|------|----------|----------|---------|")
    for row in rows:
        print("| {} | {} | {} | {} |".format(row[0], row[1], row[2], row[3]))


def DeleteContact(cur):
    Dname = input("Enter the name of the contact want to delete: ")
    DlastName = input("Enter the last name of the contact want to delete: ")
    cur.execute(
        "DELETE FROM contacts WHERE Name = ? AND LastName = ?", (Dname, DlastName)
    )
    print(f"{Dname} {DlastName} is deleted successfully")
    con.commit()


def FindContact(cur, SearchType):
    if SearchType == "n" or SearchType == "N":
        Sname = input("Enter the Name of the Contact want to Search: ")

        def FindContactByName(cur, Sname):
            cur.execute("SELECT * FROM contacts WHERE Name = ?", (Sname,))
            rows = cur.fetchall()
            print("| Name | LastName |   PhoneNO  | Address |")
            print("|------|----------|------------|---------|")
            for row in rows:
                print("| {} | {} | {} | {} |".format(row[0], row[1], row[2], row[3]))

        FindContactByName(cur, Sname)

    elif SearchType == "l" or SearchType == "L":
        SlastName = input("Enter the LastName of thcurtact want to Search: ")

        def FindContactByLastName(cur, SlastName):
            cur.execute("SELECT * FROM contacts WHERE LastName = ?", (SlastName,))
            rows = cur.fetchall()
            print("| Name | LastName |   PhoneNO  | Address |")
            print("|------|----------|------------|---------|")
            for row in rows:
                print("| {} | {} | {} | {} |".format(row[0], row[1], row[2], row[3]))

        FindContactByLastName(cur, SlastName)
    elif SearchType == "p" or SearchType == "P":
        Sphone = input("Enter the PhoneNumber of the Contact want to Search: ")

        def FindContactByPhoneNumber(cur, Sphone):
            cur.execute("SELECT * FROM contacts WHERE PhoneNumber = ?", (Sphone,))
            rows = cur.fetchall()
            print("| Name | LastName |   PhoneNO  | Address |")
            print("|------|----------|------------|---------|")
            for row in rows:
                print("| {} | {} | {} | {} |".format(row[0], row[1], row[2], row[3]))

        FindContactByPhoneNumber(cur, Sphone)
    elif SearchType == "a" or SearchType == "A":
        Saddress = input("Enter the Adress of the Contact want to Search: ")

        def FindContactByAddress(cur, Saddress):
            cur.execute("SELECT * FROM contacts WHERE Address = ?", (Saddress,))
            rows = cur.fetchall()
            print("| Name | LastName |   PhoneNo  | Address |")
            print("|------|----------|------------|---------|")
            for row in rows:
                print("| {} | {} | {} | {} |".format(row[0], row[1], row[2], row[3]))

        FindContactByAddress(cur, Saddress)


def main():
    ConnectDatabase()
    print("\t ***** Contact Manager *****")
    print(" 1.AddContact")
    print(" 2.DeleteContact")
    print(" 3.FindContact")
    print(" 4.ViewContacts")
    print(" 5.Exit")
    while True:
        Choice = int(input("Enter your Choice:"))
        if Choice == 1:
            AddContact(con, cur)

        elif Choice == 2:
            DeleteContact(cur)

        elif Choice == 3:
            SearchType = input(
                "Enter the Search Type of the Contact(n:name,l:LastName,p:PhoneNO,a:Address): "
            )
            FindContact(cur, SearchType)

        elif Choice == 4:
            ViewContact(cur)

        elif Choice == 5:
            break
        else:
            print("Invalid Choice..!!")


if __name__ == "__main__":
    main()
