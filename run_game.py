with open('game', 'r') as file:
    code = file.read()
    exec(code)

file.close()