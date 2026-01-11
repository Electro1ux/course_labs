# Использование официального образа Python версии 3.11 на базе slim
FROM python:3.11-slim

# Установка рабочей директории внутри контейнера
WORKDIR /hello

# Копирование файла зависимостей в контейнер
COPY requirements.txt .

# Установка зависимостей из файла requirements.txt без кэширования pip
RUN pip install --no-cache-dir -r requirements.txt

# Копирование основного Python-скрипта в контейнер
COPY screen.py .

# Команда запуска приложения при старте контейнера
CMD ["python", "screen.py"]
