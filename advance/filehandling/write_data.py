file = open("example.txt", "w")
# data = input("Enter something: ")
# file.write(data)

lines = ['this is a line number - 1\n', 'this is a line number - 2\n', 'this is a line number - 3\n', 'this is a line number - 4\n', 'this is a line number - 5\n' , "This is a new line."]

file.writelines(lines)
file.close()