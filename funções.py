def texto(txt='', color='\033[m', end='\033[m'):
    print(f'{color}-=' * 21)
    print(txt.center(42))
    print(f'{color}-={end}' * 21)