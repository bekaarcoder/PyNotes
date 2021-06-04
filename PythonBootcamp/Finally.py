try:
    my_file = open("mydata2.txt", encoding="utf-8")
    print(my_file.read())
    my_file.close()
except FileNotFoundError as ex:
    print("File was not found:", ex.args[1])
finally:
    "Finished working with file"
