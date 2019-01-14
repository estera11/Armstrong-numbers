def is_armstrong(number):
    num = 0 
    number_as_string = str(number)
    for x in range (0,len(number_as_string)):
        num = num + (int(number_as_string[x]) ** len(number_as_string))
    return True if (num == number) else False
