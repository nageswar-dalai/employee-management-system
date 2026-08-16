employees = [
    {"id": 1, "name": "Rahul", "age": 25, "salary": 30000},
    {"id": 2, "name": "Amit", "age": 28, "salary": 40000},
    {"id": 3, "name": "Priya", "age": 24, "salary": 35000}
]


def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    age = int(input("Enter Age: "))
    salary = float(input("Enter Salary: "))

    employee = {
        "id": emp_id,
        "name": name,
        "age": age,
        "salary": salary
    }

    employees.append(employee)

    print("Employee added successfully!")

def view_employees():
    for emp in employees:
        print("ID:", emp["id"])
        print("Name:", emp["name"])
        print("Age:", emp["age"])
        print("Salary:", emp["salary"])
        print("--------------------")

def search_employee():
    name = input("Enter Employee Name: ")

    found = False

    for emp in employees:
        if emp["name"].lower() == name.lower():
            print("ID:", emp["id"])
            print("Name:", emp["name"])
            print("Age:", emp["age"])
            print("Salary:", emp["salary"])
            found = True

    if not found:
        print("Employee not found!")

def average_salary():
    total = 0

    for emp in employees:
        total = total + emp["salary"]

    average = total / len(employees)

    print("Average Salary:", average)

def highest_salary():
    highest = employees[0]

    for emp in employees:
        if emp["salary"] > highest["salary"]:
            highest = emp

    print("Highest Salary Employee:")
    print("ID:", highest["id"])
    print("Name:", highest["name"])
    print("Age:", highest["age"])
    print("Salary:", highest["salary"])

def lowest_salary():
    lowest = employees[0]

    for emp in employees:
        if emp["salary"] < lowest["salary"]:
            lowest = emp

    print("Lowest Salary Employee:")
    print("ID:", lowest["id"])
    print("Name:", lowest["name"])
    print("Age:", lowest["age"])
    print("Salary:", lowest["salary"])

def employees_above_salary():
    amount = float(input("Enter salary amount: "))

    found = False

    for emp in employees:
        if emp["salary"] > amount:
            print("ID:", emp["id"])
            print("Name:", emp["name"])
            print("Age:", emp["age"])
            print("Salary:", emp["salary"])
            print("--------------------")
            found = True

    if not found:
        print("No employee found!")

print("===== Employee Management System =====")
print("1. Add Employee")
print("2. View Employees")
print("3. Search Employee")
print("4. Average Salary")
print("5. Highest Salary")
print("6. Lowest Salary")
print("7. Employees Above Salary")
print("8. Exit")

while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        average_salary()

    elif choice == "5":
        highest_salary()

    elif choice == "6":
        lowest_salary()

    elif choice == "7":
        employees_above_salary()

    elif choice == "8":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")