from address import Address
from mailing import Mailing

to_address = Address(123, 'Ekat', 'Roshinskaya', 21, 56)
from_address = Address(321, 'Ekat', 'Ryabynina', 49, 44)
cost = 100
track = '123qwerty'

mailing = Mailing(to_address, from_address, cost, track)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
