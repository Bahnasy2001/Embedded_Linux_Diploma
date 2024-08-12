#Write python code to generate Init function of GPIO for AVR

#Open File in read write operation
File = open('init.c','w+')
File.write('void init_PORTA_DIR (void)\n{\n\t')
i = 0
DDRA = ''
while i < 8:
    while 1:
        Value = input("Please enter Bit " + str(i) + ' mode: ')
        Value = Value.lower()
        if Value == 'in':
            DDRA = '0'+DDRA
            break
        elif Value == 'out':
            DDRA = '1'+DDRA
            break
        else:
            print("Wrong Option, Please try again")
    i = i+1

DDRA = '0b'+DDRA
File.write("DDRA = "+DDRA)
File.write(';\n}')

File.close()