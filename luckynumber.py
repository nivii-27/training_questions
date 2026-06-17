car_num_str = input("Enter the car no:")
if not car_num_str.isdigit() or len(car_num_str) != 4 or int(car_num_str) <= 0:
    print(f"{car_num_str} is not a valid car number")
else:
    car_num = int(car_num_str)
    digit_sum = sum(int(digit) for digit in car_num_str)
    if digit_sum % 3 == 0 or digit_sum % 5 == 0 or digit_sum % 7 == 0:
        print("Lucky Number")
    else:
        print("Sorry its not my lucky number")
