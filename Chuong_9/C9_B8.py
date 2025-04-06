with open('abc.txt', 'r') as file:
    content = file.read()
    content.split()
    numlist =[]

    for string in content:
        if string.isnumeric():
            numlist.append(string)
    
            
with open('xyz.txt', 'w') as file:
    for num in numlist:
        file.write(num + '\n')


