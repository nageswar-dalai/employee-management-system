import json
def load_data():
    try:
        with open("employees.json", "r") as file:
            return json.load(file)
    except:
        return []
    
employees = load_data()


def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    age = int(input("Enter Age: "))
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")
    city = input("Enter City: ")

    employee = {
        "id": emp_id,
        "name": name,
        "age": age,
        "salary": salary,
        "department": department,
        "city": city
    }

    employees.append(employee)
    save_data()
    print("Employee added successfully!")

def save_data():
    with open("employees.json", "w") as file:
        json.dump(employees, file, indent=4)

    print("Data saved successfully!")

def view_employees():
    for emp in employees:
        print("ID:", emp["id"])
        print("Name:", emp["name"])
        print("Age:", emp["age"])
        print("Salary:", emp["salary"])
        print("Department:", emp["department"])
        print("City:", emp["city"])
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

def update_employee():
    emp_id = int(input("Enter Employee ID: "))

    for emp in employees:
        if emp["id"] == emp_id:
            emp["name"] = input("Enter New Name: ")
            emp["age"] = int(input("Enter New Age: "))
            emp["salary"] = float(input("Enter New Salary: "))
            emp["department"] = input("Enter New Department: ")
            emp["city"] = input("Enter New City: ")

            print("Employee updated successfully!")
            return

    print("Employee not found!")

def delete_employee():
    emp_id = int(input("Enter Employee ID: "))

    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            save_data()
            print("Employee deleted successfully!")
            return

    print("Employee not found!")

def search_employee():
    emp_id = int(input("Enter Employee ID: "))

    for emp in employees:
        if emp["id"] == emp_id:
            print("ID:", emp["id"])
            print("Name:", emp["name"])
            print("Age:", emp["age"])
            print("Salary:", emp["salary"])
            print("Department:", emp["department"])
            print("City:", emp["city"])
            return

    print("Employee not found!")

def department_salary():
    departments = {}

    for emp in employees:
        dept = emp["department"]

        if dept not in departments:
            departments[dept] = []

        departments[dept].append(emp["salary"])

    for dept, salaries in departments.items():
        average = sum(salaries) / len(salaries)
        print(dept, "Average Salary:", average)

def city_employee_count():
    cities = {}

    for emp in employees:
        city = emp["city"]

        if city not in cities:
            cities[city] = 0

        cities[city] += 1

    for city, count in cities.items():
        print(city, "Employee Count:", count)

def city_average_salary():
    cities = {}

    for emp in employees:
        city = emp["city"]

        if city not in cities:
            cities[city] = []

        cities[city].append(emp["salary"])

    for city, salaries in cities.items():
        average = sum(salaries) / len(salaries)
        print(city, "Average Salary:", average)

print("===== Employee Management System V2 =====")
print("1. Add Employee")
print("2. View Employees")
print("3. Search Employee")
print("4. Average Salary")
print("5. Highest Salary")
print("6. Lowest Salary")
print("7. Employees Above Salary")
print("8. Update Employee")
print("9. Delete Employee")
print("10. Department-wise Average Salary")
print("11. City-wise Employee Count")
print("12. City-wise Average Salary")
print("13. Total Employees")
print("14. Exit")

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
        update_employee()

    elif choice == "9":
        delete_employee()

    elif choice == "10":
        department_salary()

    elif choice == "11":
        city_employee_count()

    elif choice == "12":
        city_average_salary()

    elif choice == "13":
        print("Total Employees:", len(employees))

    elif choice == "14":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")