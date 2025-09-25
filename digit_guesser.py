start = int(input(f'start is: '))
end = int(input(f'end is: '))

while True:
    if (start < 0 and end > 0) or (start > 0 and end > 0):
        middle = (end + start) //  2
        check = input(f"your digit <>= {middle}? ")
        if check == "=":
            print(f"your digit is {middle}")
            break
        elif check == "exit":
            break
        elif check == "<":
            end = middle - 1
        elif check == ">":
            start = middle + 1
    else:
        middle_special = int((end + start) / 2)
        check = input(f"your digit <>= {middle_special}? ")
        if check == "=":
            print(f"your digit is {middle_special}")
            break
        elif check == "exit":
            break
        elif check == "<":
            end = middle_special - 1
        elif check == ">":
            start = middle_special + 1

# работает с диапазонами вида [-x, y], [x, y], [-x, -y]