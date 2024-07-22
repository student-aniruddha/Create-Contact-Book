#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Contact Book

# Simple Contact Book Application

# Initialize an empty contact book
contact_book = {}

def add_contact():
    """Add a new contact to the contact book."""
    name = input("Enter contact name: ").strip()
    phone_number = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contact_book[name] = {
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    """Display all contacts."""
    if not contact_book:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone Number: {details['phone_number']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("")

def search_contact():
    """Search for a contact by name or phone number."""
    search_term = input("Enter name or phone number to search: ").strip()
    found = False
    for name, details in contact_book.items():
        if search_term.lower() in name.lower() or search_term in details['phone_number']:
            print(f"\nFound Contact:")
            print(f"Name: {name}")
            print(f"Phone Number: {details['phone_number']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("")
            found = True
    if not found:
        print("No contact found.")

def update_contact():
    """Update an existing contact."""
    name = input("Enter the name of the contact to update: ").strip()
    if name in contact_book:
        print(f"Updating contact '{name}'")
        phone_number = input("Enter new phone number: ").strip()
        email = input("Enter new email: ").strip()
        address = input("Enter new address: ").strip()
        contact_book[name] = {
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        print(f"Contact '{name}' updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    """Delete a contact from the contact book."""
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

def menu():
    """Display the menu and handle user choices."""
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

# Run the contact book application
menu()

