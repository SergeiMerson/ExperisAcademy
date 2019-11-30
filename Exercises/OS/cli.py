import execution


root_name = ''
root_info = {}

exit = False

while not exit:
    user_input = input('Enter your command [or print "exit"]:').split(' ', maxsplit=1)
    command = user_input[0].lower().strip()
    if command == 'scan':
        path = user_input[1].lower().strip()
        root_name, root_info = execution.scan(path)
    elif command == 'dup':
        csv_file = user_input[1].lower().strip()
        execution.dup(csv_file, root_info)
    elif command == 'dirsize':
        depth = int(user_input[1].lower().strip()) if len(user_input) > 0 else False
        execution.dirsize(root_info, root_name, depth)
    elif command == 'exit':
        exit = True
    else:
        print('Couldn\'t interpret your command')
