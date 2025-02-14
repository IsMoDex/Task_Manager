import random

class ChatBot:
    def __init__(self, name="TaskBot"):
        self.name = name
        self.tasks = []  # Список задач

    def greet_user(self):
        """Приветствие пользователя"""
        greetings = ["Привет! Как я могу помочь?", "Здравствуйте! Чем могу помочь?", "Привет! Чем могу быть полезен?"]
        return random.choice(greetings)

    def add_task(self, task_name):
        """Добавление задачи в список"""
        task = {"name": task_name, "status": "не выполнена"}
        self.tasks.append(task)
        return f"Задача '{task_name}' добавлена."

    def view_tasks(self):
        """Просмотр всех задач"""
        if not self.tasks:
            return "У вас нет задач."
        task_list = "\n".join([f"{index+1}. {task['name']} - {task['status']}" for index, task in enumerate(self.tasks)])
        return task_list

    def complete_task(self, task_index):
        """Помечаем задачу как выполненную"""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['status'] = 'выполнена'
            return f"Задача '{self.tasks[task_index]['name']}' выполнена!"
        else:
            return "Задача не найдена."

    def handle_command(self, command):
        """Обрабатывает команды пользователя"""
        if "привет" in command.lower():
            return self.greet_user()
        elif "добавить задачу" in command.lower():
            task_name = command.split("добавить задачу")[-1].strip()
            return self.add_task(task_name)
        elif "посмотреть задачи" in command.lower():
            return self.view_tasks()
        elif "выполнить задачу" in command.lower():
            try:
                task_index = int(command.split()[-1]) - 1
                return self.complete_task(task_index)
            except ValueError:
                return "Не указано номер задачи."
        else:
            return "Извините, я не понял команду."

# Пример использования
if __name__ == "__main__":
    bot = ChatBot()

    # Пример взаимодействия с ботом
    print(bot.handle_command("привет"))
    print(bot.handle_command("добавить задачу Сделать отчет"))
    print(bot.handle_command("посмотреть задачи"))
    print(bot.handle_command("выполнить задачу 1"))
    print(bot.handle_command("посмотреть задачи"))
