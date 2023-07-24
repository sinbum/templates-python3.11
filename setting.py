# mysite/settings.py
from decouple import config
from urllib.parse import quote

DB_USERNAME = config('DB_USERNAME')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')
DB_NAME = config('DB_NAME')

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')


def get_mysql_url():
    return f"mysql+pymysql://{DB_USERNAME}:{quote(DB_PASSWORD)}@{DB_HOST}/{DB_NAME}"
