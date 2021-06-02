import os

with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Some random text in the file\nMore text in the file")

with open("mydata.txt", encoding="utf-8") as my_file:
    print(my_file.read())

with open("mydata.txt", encoding="utf-8") as my_file:
    print(my_file.readlines())

with open("mydata.txt", encoding="utf-8") as my_file:
    line_num = 1
    while True:
        line = my_file.readline()
        if not line:
            break
        print(line, end="")
        words = len(line.split())
        print("Number of words: ", words)
        total = 0
        for word in line.split():
            total = total + len(word)
        print("Average Word Length: ", round(total/words, 2))

        line_num += 1

print(my_file.closed)

print(my_file.name)
print(my_file.mode)

