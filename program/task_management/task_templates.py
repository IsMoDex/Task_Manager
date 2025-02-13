class TaskTemplate:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def create_task(self):
        print(f"Task Template: {self.title}, Description: {self.description}")
