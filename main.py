import os
from calculator.operations import add, subtract, multiply, divide
from calculator.history import add_history, get_history
from calculator.file_manager import save_txt, save_csv, ensure_folder

count = 5

while count > 0:
    print("\n===== CALCULATOR APP =====")
    print(f"Attempts left: {count}\n")

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Save History")
    print("7. Exit")

    choice = input("Choose option: ")

    if choice not in ["1","2","3","4","5","6","7"]:
        count -= 1
        print("Invalid choice.")
        continue

    if choice == "7":
        break

    if choice == "5":
        for i, h in enumerate(get_history(), 1):
            print(f"{i}) {h}")
        continue

    if choice == "6":
        folder = input("Enter folder (or press enter for Desktop): ")
        if folder.strip() == "":
            folder = os.path.join(os.path.expanduser("~"), "Desktop")

        ensure_folder(folder)

        filename = input("Filename: ")
        file_type = input("1 TXT / 2 CSV: ")

        if file_type == "1":
            save_txt(f"{folder}/{filename}.txt", get_history())
        else:
            save_csv(f"{folder}/{filename}.csv", get_history())

        print("Saved successfully!")
        continue

    # Input handling
    while True:
        num1 = input("First number (b to back): ")
        if num1 == "b":
            break

        num2 = input("Second number (b to back): ")
        if num2 == "b":
            break

        try:
            num1 = float(num1)
            num2 = float(num2)
        except:
            print("Invalid numbers, try again.")
            continue

        if choice == "1":
            result = add(num1, num2)
            op = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            op = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            op = "*"
        else:
            result = divide(num1, num2)
            op = "/"

        entry = f"{num1} {op} {num2} = {result}"
        print("Result:", result)

        add_history(entry)
        count -= 1
        break

if count == 0:
    print("No attempts left.")
