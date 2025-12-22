FROM python:3.11-slim AS builder # Использование Python образа с ОС slim как базового для этапа сборки
WORKDIR /hello # Установка рабочей директории внутри контейнера
COPY requirements.txt . # Копирование файла зависимостей из локальной директории в контейнер
RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt # Обновление pip и создание wheel-пакетов зависимостей в отдельной директории

FROM python:3.11-slim # Начало нового этапа сборки с Python образа
WORKDIR /hello # Установка рабочей директории для финального образа
COPY --from=builder /wheels /wheels # Копирование собранных wheel-пакетов из этапа builder
COPY requirements.txt . # Копирование файла зависимостей для установки
RUN pip install --no-index --find-links=/wheels -r requirements.txt # Установка зависимостей из локальных wheel-пакетов
COPY hello.py . # Копирование основного файла приложения в контейнер

ENV PYTHONUNBUFFERED=1 # Настройка переменной окружения для вывода логов Python
CMD ["python", "hello.py"] # Команда запуска приложения при старте контейнера
