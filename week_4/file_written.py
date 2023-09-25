numbers = ["one", "two", "three", "four", "five", "six"]


try:
    with open("data.txt", "w") as data_file:
        for number in numbers:
            data_file.write(number + "\n ")
except OSError:
    print("can't write to file")