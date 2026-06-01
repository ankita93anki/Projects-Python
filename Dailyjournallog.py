#Day 16 Project: Daily Journal Logger
#Step 1:Define the journal file
JOURNAL_FILE = "daily_journal.txt"

#Step 2: Add anew entry
def add_entry():
    entry = input("Write your journal entry: ")
    with open(JOURNAL_FILE, 'a') as file:
        file.write(entry + "\n")
    print("Entry added successfully!")

# Step 3: View All entries
def view_entries():
    try:
        with open(JOURNAL_FILE, 'r') as file:
            content = file.read()
            if content:
                print("\n--- Your Journal Entries:---")
                print(content)
            else:
                print("No entries found.... Start Writing today")
    except FileNotFoundError:
        print("No journal file found. Add an entry first!")

#Step 4: Search entries by keyword 
def search_entries():
    keyword = input("Enter a keyword to search for: ").lower()
    try:
        with open(JOURNAL_FILE, 'r') as file:
            content = file.readlines()
            found = False
            print("\n--- Search Results ----")
            for entry in content:
                if keyword in entry.lower():
                    print(entry.strip())
                    found = True 
            if not found:
                print("No matching entries found.")
    except:
        print("No journal file found, Add an entry first!")

#Step 5: Display Menu
def show_menu():
    print("\n---- Daily Journal Logger ---")
    print("1. Add a new  entry")
    print("2. View all entry")
    print("3. Search entry by keyword")
    print("4. Exit")

#Step 6: Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ").strip()
    if choice == '1':
        add_entry()
    elif choice == '2':
        view_entries()
    elif choice == '3':
        search_entries()
    elif choice == '4':
        print("Exiting the program. Good bye!")
        break
    else:
        print("Invalid choice. Please eneter a number between 1 AND 4")