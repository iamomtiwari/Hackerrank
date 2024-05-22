def mutate_string(string, position, character):
    string = string[:5] + "k" + string[6:]
    return string

if __name__ == '__main__':
