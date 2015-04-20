def reduce_file_path(s):
    while '//' in s:
        s = s.replace("//", "/")
    dirList = s.split('/')
    dirList.pop(0)
    if s[len(s) - 1] == '/':
        dirList.pop()
    output = '/'
    current = ''
    for x in dirList:
        print (output)
        if x.isalpha():
            output += x + '/'
            current = x
            print(current)
        if x == '..':
            output=output[:-(len(current)+1)]
    print(dirList)
    return output


a = (input("Enter path: "))

print(reduce_file_path(a))

