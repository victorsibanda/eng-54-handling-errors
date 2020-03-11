#Opening files using `with`

# try:
#     file = open('order.txt','r')
#
# except FileNotFoundError as err:
#     print('Check your files')
#     print(err)
#     raise  #Breaks the code anyway


###Open () USING `with`
#helps with open and closing
try:
    with open('order.txt','r') as file:
        lines_list = file.readlines()
        for line in lines_list:
            print (line.rstrip('\n'))
except FileNotFoundError as err:
    print ('check your file')
    print (err)
finally:
    print ('////// Program Closing ///////')

