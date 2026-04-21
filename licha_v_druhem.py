def is_even(n): return n % 2 == 0
def is_odd(n): return not is_even(n)

all = range(1, 21)
odd = map(str, filter(is_odd, all))
even = map(str, filter(is_even, all))

print('odd:', '; '.join(odd))
print('even:', '; '.join(even))