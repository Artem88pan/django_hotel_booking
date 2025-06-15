FROM python:3.11-slim

# 1) Системные зависимости для сборки
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*
# 2) Отключаем .pyc и буферизацию вывода
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3) Рабочая директория
WORKDIR /app

# 4) Копируем метаданные проекта + исходники пакетов
COPY pyproject.toml poetry.lock README.md /app/
COPY src/ /app/src/

# 5) Ставим Poetry и зависимости
RUN pip install --no-cache-dir poetry \
 && poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi

# 6) Копируем остальной код (миграции, настройки, тесты и т.д.)
COPY . /app

EXPOSE 8000

CMD ["gunicorn", "booking_hotel.wsgi:application", "--bind", "0.0.0.0:8000"]
