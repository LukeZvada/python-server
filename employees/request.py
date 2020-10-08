EMPLOYEES = [
    {
        "id": 1,
        "name": "Emily Lemmon",
        "locationId": 1
    },
    {
        "id": 2,
        "name": "Jordan Castelloe",
        "locationId": 2
    },
    {
        "id": 3,
        "name": "Ryan Tanay",
        "locationId": 2
    },
    {
        "id": 4,
        "name": "Jenna Solis",
        "locationId": 1
    }
]


def get_all_employees():
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def delete_employee(id):
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):

        if employee["id"] == id:
            employee_index = index
            
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break