#Note Taking APP

#Step 1: Define file name
File_NAME = "myNotes.txt"

#Step 2: Display menu Options
def show_menu():
    print("\n---Note-Taking App Menu---")
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Delete all notes")
    print("4. Exit")

#Step 3: Add a new note
def add_note():
    note = input("Enter your note:")
    with open(File_NAME, "a") as file:
        file.write(note + "\n")
    print("Not added successfully!")

#Step 4: View all notes
def view_notes():
    try:
        with open(File_NAME, "r") as file:
            content = file.read()
            if content:
                print("\n--- All Notes ---")
                print(content)
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes found.")

#Step5:Delete all notes
def delete_notes():
    confirm = input("Are you sure you want to delete all notes? (Yes/n):")
    if confirm.lower() == "yes":
        with open(File_NAME, "w") as file:
            pass 
        print("All notes have been deleted")
    else:
        print("Deleted cancelled")

#step 6:Main Loop

while True:
    show_menu()
    choice = input("Enter your choice(1-4): ")

    if choice == "1":
        add_note()
    
    elif choice == "2":
        view_notes()
    
    elif choice == "3":
        delete_notes()
    
    elif choice == "4":
        print("Eisting Note-Taking App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
