import math

# Get the size of the list from the user
while True:
    try:
        list_size = int(input('\n Enter size of the list you would like to sort: '))
        if list_size <= 1:
            raise ValueError("\nInvalid input! Size must be a positive integer.")
    except ValueError:
        print("\nInvalid input data type! You must enter an integer.")
    else:
        break

# Get the sorting order from the user
while True:
    try:
        sort_type = input("\n Enter 'a' to sort ascendingly || 'd' to sort descendingly:").lower()
        if sort_type not in ('a', 'd'):
            raise ValueError("\nNot allowed! You must enter 'a' or 'd'.")
    except ValueError as error:
        print(error)
    else:
        break

# Get the numbering type (int or float) from the user
while True:
    try:
        numbering_type = input("\n If you would like to sort it as int enter 'i' || float and enter 'f' :").lower()
        if numbering_type != 'i' and numbering_type != 'f':
            raise ValueError("\nNot allowed! You must enter 'i' or 'f'.")
    except ValueError as error:
        print(error)
    else:
        break

number_list = []

# Collect and process numbers based on user input
for _ in range(list_size):
    while True:
        try:
            number = float(input('\n Enter a number:'))
            if isinstance(number, (int, float)):
                print('\n                   Number is either int or float')
                if numbering_type == 'i':
                    number = math.ceil(number) if number - math.floor(number) > 0.5 else math.floor(number)
                number_list.append(number)
                break
        except ValueError:
            print("\n                   Invalid input. Please enter an integer or float.")

# Sort the list based on user preference
if sort_type == 'a':
    number_list.sort()
else:
    number_list.sort(reverse=True)

# Display the sorted list
print('\nresult =', number_list, end="\n\n")