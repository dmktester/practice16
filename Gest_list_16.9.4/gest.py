'''
Команда проекта «Дом питомца» планирует большой
 корпоратив для своих волонтеров. Вам необходимо
  написать программу, которая позволяла бы составлять
   список нескольких гостей. Решите задачу с помощью
    метода конструктора и примените один из принципов
     наследования.

При выводе в консоль вы должны получить:  
“Иван Петров, г.Москва, статус "Наставник"

P.S. Если одной головой тяжело решается, 
позовите сокурсников. Вместе ведь всегда легче,
 веселее, интереснее. И еще у нас есть отзывчивые
  менторы  ;)
'''
class Gest:
    def __init__(self, name='', city='', status='') -> None:
        self.name = name
        self.city = city
        self.status = status

# get data user amount
    def get_gest_list(self, gest_dict):
        self.name = gest_dict.get('name')
        self.city = gest_dict.get('city')
        self.status = gest_dict.get('status')