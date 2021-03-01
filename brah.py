namn = input('Filens namn? ')
f = open(namn, 'r')
for rad in f:
    print(rad, end='')
    f.close()