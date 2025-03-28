from itertools import permutations
def solve():
    letters=set('CROSSROADSDANGER')
    if len(letters)>10:
        print("it is more than 10 unique numbers so it is not possible")
        return
    for prem in permutations(range(10),len(letters)):
        char_to_digit=dict(zip(letters,prem))
        if any(char_to_digit[c] == 0 for c in 'CRD'): continue
        cross=int(''.join(str(char_to_digit[c]) for c in 'CROSS'))
        roads=int(''.join(str(char_to_digit[c]) for c in 'ROADS'))
        danger=int(''.join(str(char_to_digit[c]) for c in 'DANGER'))
        if cross+roads == danger:
            print("Solution found:",char_to_digit)
            return
    print("No solution found")
solve()
