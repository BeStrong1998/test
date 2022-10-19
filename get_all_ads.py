from webapp import db, create_app
from webapp.model import RealEstateAds

app = create_app()
with app.app_context(): # Контекст нам нужен если мы обращаемся к приложению или к каким-то его компонентам если мы находимя вне модуля приложения например create_db и wrbapp у тебя на одном уровне, поэтому нужен контекст, если мы из модуля приложения будем, вызывать, то контекст скорее всего не понадобится
    advertisement = RealEstateAds(title='Продажа 3 комнт кв', url='www', price=77, square=51, adress='г. Одинцово',  number_of_rooms=2)  # Добавлякм значения в колонки нашей таблицы
    db.session.add(advertisement) # Зафиксировали изменения 
    db.session.commit() # Добавили изменения в таблицу
    
    #RealEstateAds.query.all()


    