import datetime
import random


class Task:
    """
    Представляет задачу с оценочным временем выполнения и приоритетом.

    Attributes:
        title (str): Название задачи.
        estimated_time (float): Оценочное время выполнения задачи в часах.
        priority (int): Приоритет задачи (1 - низкий, 5 - высокий).
        completion_times (list): Список времени выполнения задачи в часах.
    """

    def __init__(self, title, estimated_time, priority, completion_times=None):
        """
        Инициализирует объект Task.

        Args:
            title (str): Название задачи.
            estimated_time (float): Оценочное время выполнения задачи в часах.
            priority (int): Приоритет задачи (1 - низкий, 5 - высокий).
            completion_times (list, optional): Список времени выполнения задачи в часах. По умолчанию None.
        """
        self.title = title
        self.estimated_time = estimated_time
        self.priority = priority
        self.completion_times = completion_times if completion_times else []

    def add_completion_time(self, time_spent):
        """Добавляет время выполнения в историю.

        Args:
            time_spent (float): Время, затраченное на выполнение задачи в часах.
        """
        self.completion_times.append(time_spent)

    def predict_completion_time(self):
        """Прогнозирует время выполнения на основе истории.

        Returns:
            float: Прогнозируемое время выполнения задачи в часах.
        """
        if not self.completion_times:
            return self.estimated_time  # Если истории нет, возвращаем оценку пользователя
        avg_time = sum(self.completion_times) / len(self.completion_times)
        return round(avg_time, 2)

    def recommend_priority(self):
        """Рекомендует приоритет на основе срочности и важности.

        Returns:
            int: Рекомендуемый приоритет задачи (1 - низкий, 5 - высокий).
        """
        urgency = random.randint(1, 5)  # Имитируем срочность (1 - не срочно, 5 - очень срочно)
        importance = self.priority
        recommended_priority = min(5, urgency + importance)  # Ограничение приоритета до 5
        return recommended_priority

    def display_forecast(self):
        """Выводит прогноз и рекомендации по задаче."""
        predicted_time = self.predict_completion_time()
        recommended_priority = self.recommend_priority()
        print(f"Задача: {self.title}")
        print(f"Прогнозируемое время выполнения: {predicted_time} часов")
        print(f"Рекомендуемый приоритет: {recommended_priority}\n")


# Пример использования
if __name__ == "__main__":
    task1 = Task("Разработка интерфейса", estimated_time=8, priority=3, completion_times=[7, 9, 8])
    task2 = Task("Настройка базы данных", estimated_time=5, priority=4, completion_times=[4.5, 5.5, 6])

    task1.display_forecast()
    task2.display_forecast()
