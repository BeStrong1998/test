from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy() #Создаём объект на основе класса SQLAlchemy и передаём туда объект app созданный на основе класса Flask

class RealEstateAds(db.Model): #Создаём класс и говорим что наследуем всё от объекта db, который является объектом SQLAlchemy
    id = db.Column(db.Integer, primary_key=True) #Уникальный индификатор объявления это наш внутренний индефикатор
    title = db.Column(db.String, nullable=False) #Название объявления, нельзя установить пустое название
    url = db.Column(db.String, unique=True, nullable=False) #Ссылка на объявление, нельзя установить пустое название
    date = db.Column(db.DateTime, default=datetime.utcnow) #выводится дата и время, виводим значение по умолчанию - это то время когда была создана наша статья, при условии если дата небыла установленна
    ads = db.Column(db.Text, nullable=True) #Полный текст объявления, может не иметь текста
    price = db.Column(db.Float, nullable=False) #Стоимостть указанная на объявлении
    square = db.Column(db.Float, nullable=False) # Площадь квартиры указанная в объявлении
    adress = db.Column(db.String, nullable=False) # Адрес квартиры
    number_of_rooms = db.Column(db.Integer, nullable=False) #Колличество комнат в квартире

    def __repr__(self):  #Вызываем метод питона, self означает что мы обращаемся к объекту класса который сейчас активен тоесть News
        return '<RealEstateAds {} {}>'.format(self.title, self.url, self.data, self.ads, self.price, self.square, self.adress, self.number_of_rooms) #Позволит опознать каждую из новостей выведет tatle-название объявления и url-адрес объявления

