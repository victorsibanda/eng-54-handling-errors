# this will break because there is no orders
# file = open('order.txt')

# Introducing try: and except: blocks

try:
    file = open('order.txt', 'r')
    file_line_list = file.readlines()
    print(file_line_list)

    for line in file_line_list:
        print (line.rstrip('\n'))

    file.close()

except FileNotFoundError as error_message:
    # print('THERE HAS BEEN AN ERROR! PANIC NOW!')
    print('Sorry, please check the file exists')
    print(error_message)
    print()