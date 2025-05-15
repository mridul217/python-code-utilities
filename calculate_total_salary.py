#Problem: Write a function that calculates the total salary of employees, including bonuses. The function takes a list of dictionaries, where each dictionary represents an employee with base_salary and bonus.



def calculate_total_salary(employees):
    total=0
    for emp in employees:
        total += emp["base_salary"] + emp["bonus"]
    return total

employees = [
        {'base_salary':50000, 'bonus': 6000},
        {'base_salary':55000,'bonus':5000}
        ]

print(calculate_total_salary(employees))
