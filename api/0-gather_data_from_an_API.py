#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 2:
    print("Uso: python todo_progress.py <ID_empleado>")
    sys.exit(1)
    
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Obtener información del empleado
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data.get("name")
    
    # Obtener la lista de tareas TODO del empleado
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()
    
    # Calcular el progreso de la lista de tareas TODO
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo.get("completed"))
    
    # Mostrar información del progreso en el formato especificado
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for todo in todos_data:
        if todo.get("completed"):
            print(f"\t{todo.get('title')}")
            
