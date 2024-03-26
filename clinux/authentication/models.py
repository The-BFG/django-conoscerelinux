from django.contrib.auth.models import AbstractUser

# NOTE: A good practice in Django is to create a custom User class ass soon as possible
#       This is caused by the fact that creating a custom user after creation of
#       migrations couse CircularDependency errors
#       For more info: https://docs.djangoproject.com/en/5.0/topics/auth/customizing/


class User(AbstractUser):
    pass
