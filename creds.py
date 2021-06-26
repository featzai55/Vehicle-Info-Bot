import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class cred():
    BOT_TOKEN = os.getenv("1813651489:AAEaFf4SmyS61j8PksiTdSdVtX54l74OKzM") #From botfather
    API_ID = os.getenv("2995136")       #"Get this value from my.telegram.org! Please do not steal"
    API_HASH = os.getenv("3c3766c8df153afb9e5ebfe7314af305")   #"Get this value from my.telegram.org! Please do not steal"
