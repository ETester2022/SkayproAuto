from smartphone import Smartphone

instance1 = ('q1', 'x1', '111'),
instance2 = ('q2', 'x2', '222'),
instance3 = ('q3', 'x3', '333'),
instance4 = ('q4', 'x4', '444'),
instance5 = ('q5', 'x5', '555')

catalog = Smartphone [ 
    instance1,
    instance2,
    instance3,
    instance4,
    instance5
]

for x in catalog:
    print(x)