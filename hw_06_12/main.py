import functions.persons as p

p = p.Person('a b c', 50, '0000 000000', 85.0)

print(p.fio, p.age, p.passport, p.weight)

p.fio = 'Lol Kek Cheburek'
p.age = 149
p.passport = '1122 333444'
p.weight = 1e999999999999999999

print(p.fio, p.age, p.passport, p.weight)
