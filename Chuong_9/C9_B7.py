with open('abc.txt', 'r') as file:
    content = file.read()

content_upper = content.upper()

with open('xyz.txt', 'w') as file:
    file.write(content_upper)
