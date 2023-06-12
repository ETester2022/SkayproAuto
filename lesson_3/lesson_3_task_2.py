from smartphone import Smartphone

instance1 = Smartphone('q1', 'x1', '111')
instance2 = Smartphone('q2', 'x2', '222')
instance3 = Smartphone('q3', 'x3', '333')
instance4 = Smartphone('q4', 'x4', '444')
instance5 = Smartphone('q5', 'x5', '555')

catalog = [ 
    instance1,
    instance2,
    instance3,
    instance4,
    instance5
]

for phone in catalog:
    print(f"{phone.marka} - {phone.model}. {phone.number}")
