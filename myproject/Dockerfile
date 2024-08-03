# Используем официальный образ Python
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем переменную окружения для Django
ENV PYTHONUNBUFFERED 1

# Команда для запуска приложения
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
