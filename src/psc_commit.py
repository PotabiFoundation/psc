def commit(readmod,args):
    command_list=[]
    for commands in readmod:
        for command in commands:
            print("*", command)
            if command[0] == "commit":
                command_list.append(command[1].replace("[arg]", args[1]))
            if command[0] == "add":
                command_list.append(command[1].replace("[arg]", args[0]))
            return command_list
    