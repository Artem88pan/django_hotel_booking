from booking_hotel.settings import *  # noqa: F403

SECRET_KEY = "test-secret-key-for-ci"


DEBUG = True


ALLOWED_HOSTS = ["*"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
