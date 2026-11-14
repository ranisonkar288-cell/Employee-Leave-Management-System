from datetime import datetime

employees = {
    "E101": {
        "name": "Amit",
        "balance": {"Casual": 12, "Sick": 10, "Earned": 15}
    }
}


def parse_date(text):
    try:
        return datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        return None


def count_days(from_date, to_date):
    return (to_date - from_date).days + 1


def get_employee(emp_id):
    return employees.get(emp_id)


def get_leave_type(text):
    leave_type = text.strip().capitalize()
    if leave_type in ("Casual", "Sick", "Earned"):
        return leave_type
    return None


def apply_leave():
    emp_id = input("Enter Employee ID: ").strip().upper()
    employee = get_employee(emp_id)
    if employee is None:
        print("Invalid employee ID.")
        return

    leave_type = get_leave_type(input("Enter Leave Type (Casual/Sick/Earned): "))
    if leave_type is None:
        print("Invalid leave type. Choose Casual, Sick or Earned.")
        return

    from_date = parse_date(input("From (YYYY-MM-DD): ").strip())
    to_date = parse_date(input("To (YYYY-MM-DD): ").strip())
    if from_date is None or to_date is None:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    if to_date < from_date:
        print("Invalid dates. To-date cannot be before from-date.")
        return

    days = count_days(from_date, to_date)
    available = employee["balance"][leave_type]

    if days > available:
        print(f"Leave rejected. Requested: {days} days | Available: {available} days")
        return

    employee["balance"][leave_type] -= days
    print(f"Leave approved: {days} days {leave_type} | Balance {leave_type}: {employee['balance'][leave_type]}")


def view_balance():
    emp_id = input("Enter Employee ID: ").strip().upper()
    employee = get_employee(emp_id)
    if employee is None:
        print("Invalid employee ID.")
        return

    balance = employee["balance"]
    print(f"Casual: {balance['Casual']} | Sick: {balance['Sick']} | Earned: {balance['Earned']}")


def show_menu():
    print()
    print("===== Employee Leave Management System =====")
    print("1. Apply Leave")
    print("2. View Balance")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            apply_leave()
        elif choice == "2":
            view_balance()
        elif choice == "3":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


main()