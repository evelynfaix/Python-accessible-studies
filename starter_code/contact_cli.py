# contact_cli.py - minimal contact manager using JSON persistence
import json
import os

FILENAME = 'contacts.json'

def load_contacts(filename=FILENAME):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_contacts(contacts, filename=FILENAME):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)

def add_contact(contacts, name, phone):
    contacts[name] = phone
    return contacts

def list_contacts(contacts):
    for name, phone in contacts.items():
        print(f'{name}: {phone}')

def main():
    contacts = load_contacts()
    while True:
        print('\nContact CLI: (a)dd (l)ist (s)earch (q)uit')
        choice = input('Choose: ').strip().lower()
        if choice == 'a':
            name = input('Name: ').strip()
            phone = input('Phone: ').strip()
            if name:
                add_contact(contacts, name, phone)
                save_contacts(contacts)
                print('Added.')
            else:
                print('Name required.')
        elif choice == 'l':
            list_contacts(contacts)
        elif choice == 's':
            q = input('Search name: ').strip()
            for name in contacts:
                if q.lower() in name.lower():
                    print(f'{name}: {contacts[name]}')
        elif choice == 'q':
            break
        else:
            print('Unknown option')

if __name__ == '__main__':
    main()
