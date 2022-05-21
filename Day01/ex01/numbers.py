def my_numbers():
    f = open("numbers.txt")
    for line in f:
        num_list = line.split(",")
    for num in num_list:
        print(num.strip())
    f.close()

if __name__ == '__main__':
    my_numbers();
