class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        if phone not in self.contacts:
            self.contacts[phone] = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
            print(f"Contact '{name}' added successfully.")
        else:
            print("Contact with this phone number already exists. Use a different number.")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for contact in self.contacts.values():
                print(f"{contact['Name']} - {contact['Phone']}")

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts.values():
            if keyword.lower() in contact['Name'].lower() or keyword in contact['Phone']:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, phone, new_name, new_phone, new_email, new_address):
        if phone in self.contacts:
            self.contacts[phone] = {'Name': new_name, 'Phone': new_phone, 'Email': new_email, 'Address': new_address}
            print(f"Contact updated successfully.")
        else:
            print("Contact not found. Unable to update.")

    def delete_contact(self, phone):
        if phone in self.contacts:
            del self.contacts[phone]
            print("Contact deleted successfully.")
        else:
            print("Contact not found. Unable to delete.")


def display_contact(contact):
    print("\nContact Details:")
    print(f"Name: {contact['Name']}")
    print(f"Phone: {contact['Phone']}")
    print(f"Email: {contact['Email']}")
    print(f"Address: {contact['Address']}")


def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contact_manager.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_manager.view_contact_list()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            found_contacts = contact_manager.search_contact(keyword)
            if found_contacts:
                for contact in found_contacts:
                    display_contact(contact)
            else:
                print("No matching contacts found.")

        elif choice == '4':
            phone = input("Enter the phone number of the contact to update: ")
            if phone in contact_manager.contacts:
                new_name = input("Enter new Name: ")
                new_phone = input("Enter new Phone: ")
                new_email = input("Enter new Email: ")
                new_address = input("Enter new Address: ")
                contact_manager.update_contact(phone, new_name, new_phone, new_email, new_address)
            else:
                print("Contact not found. Unable to update.")

        elif choice == '5':
            phone = input("Enter the phone number of the contact to delete: ")
            contact_manager.delete_contact(phone)

        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()

