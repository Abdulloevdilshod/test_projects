def find_str():
    string = input('Enter the string: ').split(' ')
    sub_str = input('Input the substring to search : ')
    dict_str = {}
    for i in range(len(string)):
        dict_str[string[i]] = i+1

    if sub_str in dict_str:
        return('The substring exist in the string')
    else:
        return('The substring not exist in the string')


print(find_str())
