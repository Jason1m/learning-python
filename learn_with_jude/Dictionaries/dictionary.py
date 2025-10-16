# print("Python Dictionay : key -> value ")
# print()
# #creating dictionaries
# student = {
#     "name" : "Olamide",
#     "age" : 22 ,
#     "grade" : "A"
# }
# print(f"\nStudent info : {student}")
# #Accessing values
# print(f"\nStudent name : {student ['name']}")
# print(f"Student age : {student ['age']}")

# #adding values
# student["course"] = "python"
# student["email"] = "olamide@gmail.com"
# print(f"\nAfter adding data : {student}")

# #change existing data

# student["age"] = "25"
# student["grade"] = "A+"
# print(f"\nAfter udating : {student}")

# #Dictionary method
# print(f"\nAll keys : {list(student.keys())}")
# print(f"All values : {list(student.values())}")
# print(f"All items : {list(student.items())}")

# #access with get()
# print(f"Safe access : {student.get('phone', 'Not provided')}")

# #check if keys exist
# if "email" in student:
#     print(f"Email : {student['email']}")
# if "course" in student:
#     print(f"Course : {student['course']}")

# #Remove items
# remove = student.pop('course')
# print(f"Removed : {remove}")
# print(f"Updated dict : {student}")

#Contact manager project
print("CONTACT MANAGER")
print("=" * 50)

contacts = {}

def show_menu():
    print("\n1. Add contact")
    print("2. View contact")
    print("3. View all contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

def add_contact():
    name = input("Name: ").strip()
    if name in contacts:
        print("Name already exists!")
        return
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print(f"Added {name} to contacts!")

def view_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        contact = contacts[name]
        print(f"\n{name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['emaill']}")
    else:
        print(f"Contact not found!")

        #view all session
def view_all():
    if not contacts:
        print("No contacts saved!")
        return
        print(f"\nAll contacts({len(contacts)}):")
        for name, info in contacts.items():
            print(f"{name} : {info['phone']}")
    
    def update_contact():
        name = input(f"Enter name: ").strip()
        if name not in contacts:
            print("Contact not found!")
            return
        print("Leave blank to keeep current value")
        phone = input(f"Phone ({contacts[name]['phone']}): ").strip()
        email = input(f"Email ({contacts[name]['email']}): ").strip()

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
            print("Contact updated!")

        def delete_contact():
            name = input(f"Enter name: ").strip()
            if name in contacts:
                del contacts[name]
                print(f"Deleted {name}")
            else:
                print(f"Contact not found!")

