from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Невский", "15", "3")

mailing_instance = Mailing(to_address, from_address, 250, "TRACK123456")

print(f"Отправление {mailing_instance.track} из {mailing_instance.from_address.index}, {mailing_instance.from_address.city}, {mailing_instance.from_address.street}, {mailing_instance.from_address.house} - {mailing_instance.from_address.apartment} в {mailing_instance.to_address.index}, {mailing_instance.to_address.city}, {mailing_instance.to_address.street}, {mailing_instance.to_address.house} - {mailing_instance.to_address.apartment}. Стоимость {mailing_instance.cost} рублей.")