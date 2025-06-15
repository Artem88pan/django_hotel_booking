# Django Hotel Booking

Простой проект на Django для управления бронированиями номеров в отеле.
Подходит для обучения. Реализован REST API для работы с номерами и бронированиями.

---

## 📋 Описание

Этот проект позволяет:

* Просматривать и создавать номера отеля через API (`/rooms/`).
* Просматривать и создавать бронирования через API (`/bookings/`).
* Фильтровать бронирования по `room_id`.

Проект написан на Python, использует Django и Django REST Framework. База данных — PostgreSQL (локально можно использовать SQLite).
Докер и Docker Compose помогают быстро поднять всё окружение.

---

## ⚙️ Требования (Prerequisites)

* Python 3.11+
* Poetry (для управления зависимостями)
* Docker и Docker Compose (опционально, для контейнеризации)

---

## 🚀 Установка и запуск локально

1. **Клонируйте репозиторий**

   ```bash
   git clone https://github.com/Artem88pan/django_hotel_booking.git
   cd django_hotel_booking
   ```

2. **Установите зависимости**

   Если у вас установлен Poetry:

   ```bash
   poetry install
   ```

3. **Создайте файл окружения `.env`** в корне проекта по примеру `.env.example` или так:

   ```ini
   SECRET_KEY=ваш_секретный_ключ
   DEBUG=1
   DATABASE_NAME=hotel_db
   DATABASE_USER=hotel_user
   DATABASE_PASSWORD=your_strong_password
   DATABASE_HOST_LOCAL=127.0.0.1
   DATABASE_PORT=5432
   ```

4. **Примените миграции**

   ```bash
   poetry run python manage.py migrate
   ```

5. **Запустите сервер разработки**

   ```bash
   poetry run python manage.py runserver
   ```

   Перейдите в браузере на `http://127.0.0.1:8000/`.

---

## 🐳 Запуск в Docker

1. **Переименуйте `.env.docker.example` в `.env.docker`** и заполните переменные:

   ```ini
   POSTGRES_DB=hotel_db
   POSTGRES_USER=hotel_user
   POSTGRES_PASSWORD=your_strong_password

   SECRET_KEY=django-insecure-...
   DEBUG=1
   RUNNING_IN_DOCKER=1
   DATABASE_NAME=hotel_db
   DATABASE_USER=hotel_user
   DATABASE_PASSWORD=your_strong_password
   DATABASE_HOST=db
   DATABASE_PORT=5432
   ```

2. **Соберите и запустите контейнеры**:

   ```bash
   docker compose up --build
   ```

3. **Проверьте логи**:

   ```bash
   docker compose logs -f web
   ```

   Если всё успешно, приложение будет доступно на `http://localhost:8000/`.

---

## ✅ Запуск тестов

В проекте есть тесты для проверки API.

```bash
# локально (SQLite в памяти)
poetry run pytest
```


## 🤝 Как участвовать

1. Форкайте репозиторий
2. Создавайте ветку `feature/ваша-ветка`
3. Вносите изменения и пишите тесты
4. Открывайте Pull Request
