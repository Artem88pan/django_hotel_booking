
# Переопределяем DATABASES для тестов
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # Используем RAM для ускорения
        # Или так, если хотите файловую БД:
        # 'NAME': BASE_DIR / 'test_db.sqlite3',
    }
}
