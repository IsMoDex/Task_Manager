import random

class VoiceTask:
    def __init__(self):
        self.tasks = []  # Список задач

    def add_task(self, task_name):
        """Добавление задачи"""
        task = {"name": task_name, "status": "не выполнена"}
        self.tasks.append(task)
        return f"Задача '{task_name}' добавлена."

    def complete_task(self, task_index):
        """Завершение задачи"""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['status'] = 'выполнена'
            return f"Задача '{self.tasks[task_index]['name']}' выполнена!"
        else:
            return "Задача не найдена."

    def view_tasks(self):
        """Просмотр всех задач"""
        if not self.tasks:
            return "У вас нет задач."
        task_list = "\n".join([f"{index+1}. {task['name']} - {task['status']}" for index, task in enumerate(self.tasks)])
        return task_list

    def execute_voice_command(self, command):
        """Исполнение голосовой команды"""
        command = command.lower()
        if "добавить задачу" in command:
            task_name = command.split("добавить задачу")[-1].strip()
            return self.add_task(task_name)
        elif "выполнить задачу" in command:
            try:
                task_index = int(command.split()[-1]) - 1
                return self.complete_task(task_index)
            except ValueError:
                return "Не указан номер задачи."
        elif "показать задачи" in command:
            return self.view_tasks()
        else:
            return "Команда не распознана."

# Пример использования
if __name__ == "__main__":
    voice_task_manager = VoiceTask()

    # Пример взаимодействия с голосовыми командами
    print(voice_task_manager.execute_voice_command("добавить задачу Закончить проект"))
    print(voice_task_manager.execute_voice_command("показать задачи"))
    print(voice_task_manager.execute_voice_command("выполнить задачу 1"))
    print(voice_task_manager.execute_voice_command("показать задачи"))
