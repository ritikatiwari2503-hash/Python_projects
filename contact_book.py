contacts = {}

while True:
    print("\n1. Add | 2. View | 3. Search | 4. Remove | 5. Quit")
    ch = input("Select (1-5): ")

    if ch == "1":
        name = input("Name: ")
        contacts[name] = input("Phone: ")
        print("Saved!")
    elif ch == "2":
        for k, v in contacts.items(): print(f"{k}: {v}")
    elif ch == "3":
        name = input("Search Name: ")
        print(contacts.get(name, "Not found!"))
    elif ch == "4":
        name = input("Delete Name: ")
        if contacts.pop(name, None): print("Deleted!")
        else: print("Not found!")
    elif ch == "5":
        print("Bye!")
        break