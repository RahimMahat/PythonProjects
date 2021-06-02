from random import sample

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
digit = "1234567890"
symbol = "~!@#$%^&*()_+{}[]:";'<>,.?\/'

genrateor = upper + lower + digit + symbol
length = 17

password = "".join(sample(genrateor, length))

print(password)

