from flask import Flask, request, jsonify
from src.models.role import Role
from src.models.project import Project
from src.services.employee_service import EmployeeService

app = Flask(__name__)
employee_service = EmployeeService()

@app.route('/add_employee', methods=['POST'])
def add_employee():
    data = request.json
    role = Role(data['role']['role_id'], data['role']['role_name'])
    project_assignments = [Project(p['project_id'], p['project_name']) for p in data['project_assignments']]
    employee_service.add_employee(data['employee_id'], data['name'], data['contact_details'], role, project_assignments)
    return jsonify({'message': 'Employee added successfully'}), 201

@app.route('/update_employee_role/<employee_id>', methods=['PUT'])
def update_employee_role(employee_id):
    data = request.json
    new_role = Role(data['role_id'], data['role_name'])
    employee_service.update_employee_role(employee_id, new_role)
    return jsonify({'message': 'Employee role updated successfully'}), 200

@app.route('/assign_projects_to_employee/<employee_id>', methods=['PUT'])
def assign_projects_to_employee(employee_id):
    data = request.json
    new_project_assignments = [Project(p['project_id'], p['project_name']) for p in data['project_assignments']]
    employee_service.assign_projects_to_employee(employee_id, new_project_assignments)
    return jsonify({'message': 'Project assignments updated successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)