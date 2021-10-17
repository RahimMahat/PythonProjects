

def TOH(n, A, B, C):
    if n == 1:
        print(f'Move 1 from {A} to {C}')
    else:
        TOH(n-1, A, C, B)
        print(f'Move {n} from {A} to {C}')
        TOH(n-1, B, A, C)
    # time complexity: theta(2^n)

TOH(3,'A','B','C')