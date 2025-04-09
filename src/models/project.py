class Project:
    def __init__(self, project_id, project_name):
        self.project_id = project_id
        self.project_name = project_name

    def __str__(self):
        return f"Project ID: {self.project_id}, Project Name: {self.project_name}"