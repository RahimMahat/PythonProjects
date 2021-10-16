txt = input('Text: ')
ptn = input('Pattern: ')
pos = txt.find(ptn)
while pos >= 0:
    print(f'Found pattern at: {pos}')
    pos = txt.find(ptn, pos + 1)