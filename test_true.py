
def test(a):
    if a == '1':
        return True
    else:
        return False

user_input = input('\n\nWhat?\n\n')

print ('\n',bool(test(user_input)),'\n\n')

