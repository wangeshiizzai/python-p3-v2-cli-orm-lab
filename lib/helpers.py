from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()


# ------------------- Department Functions -------------------

def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ").strip()
    department = Department.find_by_name(name)
    print(department) if department else print(f'Department {name} not found')


def find_department_by_id():
    id_ = input("Enter the department's id: ").strip()
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ").strip()
    location = input("Enter the department's location: ").strip()
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ").strip()
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ").strip()
            department.name = name
            location = input("Enter the department's new location: ").strip()
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ").strip()
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# ------------------- Employee Functions -------------------

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter the employee's name: ").strip()
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(f"Employee {name} not found")


def find_employee_by_id():
    try:
        id_ = int(input("Enter the employee's id: ").strip())
    except ValueError:
        print("Invalid ID")
        return

    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f"Employee {id_} not found")


def create_employee():
    try:
        name = input("Enter the employee's name: ").strip()
        job_title = input("Enter the employee's job title: ").strip()
        department_id = int(input("Enter the employee's department id: ").strip())

        employee = Employee(name=name, job_title=job_title, department_id=department_id)
        employee.create()  # or save() depending on your ORM
        print(f"Success: {employee}")
    except Exception as exc:
        print(f"Error creating employee: {exc}")


def update_employee():
    try:
        id_ = int(input("Enter the employee's id: ").strip())
    except ValueError:
        print("Invalid ID")
        return

    if employee := Employee.find_by_id(id_):
        try:
            new_name = input("Enter the employee's new name: ").strip()
            employee.name = new_name
            new_job_title = input("Enter the employee's new job title: ").strip()
            employee.job_title = new_job_title
            new_department_id = int(input("Enter the employee's new department id: ").strip())
            employee.department_id = new_department_id

            employee.update()
            print(f"Success: {employee}")
        except Exception as exc:
            print(f"Error updating employee: {exc}")
    else:
        print
