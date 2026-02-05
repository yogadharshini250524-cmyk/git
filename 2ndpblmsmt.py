def count_above_avg(input_string):
    numbers_str = input_string.split()
    numbers = []
    for num_str in numbers_str:
        numbers.append(int(num_str))
    total = 0
    for num in numbers:
        total = total + num
    average = total / len(numbers)
    count = 0
    for num in numbers:
        if num > average:
            count = count + 1
    print(count)
   
input_string = input("enter the readings")
count_above_avg(input_string)