from .models import Menu, MenuCategory
from cryptography.fernet import Fernet


def get_or_create_menu(obj, hotel):
    menu, created = Menu.objects.get_or_create(name=obj.get("menu"), hotel=hotel)
    return menu


def get_or_create_menu_category(obj, menu):
    menu_category, created = MenuCategory.objects.get_or_create(name=obj.get("menu_category"), menu=menu)
    return menu_category


def encrypt_data(data):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    # encMessage = fernet.encrypt(data.encode()).decode()
    encMessage = fernet.encrypt(data.encode())
    return encMessage
    # print("original string: ", data)
    # print("encrypted string: ", encMessage)
    # decMessage = fernet.decrypt(encMessage).decode()
