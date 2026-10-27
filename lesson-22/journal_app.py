from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / "journal.txt"
print(file_path)

# Journal Application

def read_journal(file_path):
    """Reads the journal from a file path"""

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            entries = file.readlines()
        return [entry.strip() for entry in entries if entry.strip()]
    except FileNotFoundError:
        print("Can't read, file not found!")
        return []

def write_journal(file_path, entry):
    """Write a journal entry to the file"""

    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f"{entry}\n")
    except FileNotFoundError:
        print("Can't write, file not found!")

def main():
    while True:

        action = input("(R)ead, (W)rite or (Q)uit?").lower()

        if action == 'r':
            journal_entries = read_journal(file_path)

            for entry in journal_entries:
                print(entry)
        elif action == 'w':
            new_entry = input("Enter your new journal entry:")
            write_journal(file_path, new_entry)
        elif action == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()