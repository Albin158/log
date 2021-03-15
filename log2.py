fileHandle ='log.txt'

while True:
    val = input('[1] Läs logg\n[2] Skriv logg\n[3] Rensa logg\n[4] Avsluta\nVälj: ')

    if val == "1":
        print('alla loggar'
        

        with open(fileHandle,'r', encoding='utf-8' ) as logFile:
            for line in logFile:
                log = line.split('')

                print(f'författare: {log[0]}')
                print(f'Datum: {log[1]}')
                print(f'Titel: {log[2]}')
                print(f'Text: {log[3]}')

            logFile.close()

        elif val == "2":
            print('------------------------')
            log = []
            log.append(input('Författare: '))
            log.append(input('Datum: '))
            log.append(input('Titel: '))
            log.append(input('Text: '))

            pipe = ''
            longstring = pipe.join(log)
            with open(fileHandle, 'a', encoding='utf-8') as logFile:
                logFile.write(logstring +'\n')
                logFile.close()

            elif val == "3":
                print('rensa')
                elif val == "4":
                    break
                else:
                    print('Felaktigt val')


