import execution


root_name = ''
root_info = {}

exit = False

while not exit:
    user_input = input('Enter your command [or print "exit"]:')
    command, arg = user_input.split(' ', maxsplit=1)
    command, arg = command.lower().strip(), arg.lower().strip()
    if command == 'scan':
        root_name, root_info = execution.scan(arg)
    elif command == 'dup':
        execution.dup(arg, root_info)
    elif command == 'dirsize':
        depth = int(arg) if len(arg) > 0 else False
        execution.dirsize(root_info, root_name, depth)
    elif command == 'exit':
        exit = True
    else:
        print('Couldn\'t interpret your command')
