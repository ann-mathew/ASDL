TICKETS_NUMBER = [('A1', 'A1'),]
for pre in range(ord('A'), ord('Z')+1):
    for fix in range(100):
        val = str(chr(pre)+ "-" + str(fix))
        TICKETS_NUMBER.append((val, val))
TICKETS_NUMBER = tuple(TICKETS_NUMBER)

COACH_CLASS = Class_Choices =  [
    ('Sleeper Class', 'Sleeper Class'),
    ('Third AC', 'Third AC'),
    ('First AC', 'First AC'),
    ('Second AC', 'Second AC'),
    ('Second Seating', 'Second Seating'),
    ('AC Chair Car', 'AC Chair Car'),
    ('First Class', 'First Class'),
]