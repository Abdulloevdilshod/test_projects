def is_pangram():
    text = input('Enter the text: ')
    return not set('abcdefghijklmnopqrstuvwxyz') - set(text.lower())


print(is_pangram())
