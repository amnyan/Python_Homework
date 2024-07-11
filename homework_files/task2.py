def create_exclusive_file():
    try:
        fd =  open('exclusive_mode.txt', 'x')
        fd.write('This is some  text.')
        fd.close()
    except FileExistsError:
        print('Error: The file "exclusive_mode.txt" already exists.')


create_exclusive_file()
