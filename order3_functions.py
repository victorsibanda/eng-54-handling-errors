#make some functions


def open_and_print(file_name):
#Open using with:
    try:
        with open(file_name, 'r') as file:
            lines_list = file.readlines()
            for line in lines_list:
                print(line.rstrip('\n'))
    except FileNotFoundError as err:
        print('check your file')
        print(err)
    finally:
        print('////// Program Closing ///////')



def open_and_write(file_name,text):
#Open using with:
    try:
        with open(file_name, 'w') as file_to_write:
            file_to_write.write(text+'\n')
    except FileNotFoundError as err:
        print('Do not panic but check your file')
        print(err)
    finally:
        print('////// Finished Truncating --> Program Closing ///////')

def open_and_append(file_name,text):
#Open using with:
    try:
        with open(file_name, 'a') as file_to_write:
            file_to_write.write(text +'\n')
    except FileNotFoundError as err:
        print('Do not panic but check your file')
        print(err)
    finally:
        print('////// Finished Appending --> Program Closing ///////')


