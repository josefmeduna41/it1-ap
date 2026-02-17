x: float = float(input('x> '))
y: float = float(input('y> '))

relationship: str = '<'
if x > y:
    relationship = '>'
elif x == y:
    relationship = '='

print(f'{x} {relationship} {y}')