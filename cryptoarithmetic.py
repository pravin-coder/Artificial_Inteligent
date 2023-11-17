from itertools import permutations
def is_valid(mapping, puzzle):
    # Check if the current mapping is valid for the puzzle
    send = mapping['S'] * 1000 + mapping['E'] * 100 + mapping['N'] * 10 + mapping['D']
    more = mapping['M'] * 1000 + mapping['O'] * 100 + mapping['R'] * 10 + mapping['E']
    money = mapping['M'] * 10000 + mapping['O'] * 1000 + mapping['N'] * 100 + mapping['E'] * 10 + mapping['Y']
    return send + more == money

def solve_cryptoarithmetic():
    puzzle = ['SEND', 'MORE', 'MONEY']
    letters = set(''.join(puzzle))
    print(letters)
    # Generate all possible permutations of digits 0 to 9 for the unique letters
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        # Check if the current mapping is valid
        if is_valid(mapping, puzzle):
            return mapping
    return None


solution = solve_cryptoarithmetic()    
if solution:
    print("Solution found:")
    for word in ['SEND', 'MORE', 'MONEY']:
        for char in word:
            print(solution[char], end=" ")
        print()
else:
    print("No solution found.")
