def biggest(num1, num2, num3):
    
    
    if num1 > num2 and num2 <num3:
        print(" Biggest is:  ", num1)
    elif num2 > num1 and num1 >num3:
        print("Biggest is", num2)
    elif num3 > num1 and num1 <num2:
        print("Biggest is", num3)
    else:
        print("all of them are =")
    return

biggest(1, 2, 3)
