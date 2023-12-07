collect_tmp = ''
sum = 0
# Open file, read each line
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        first_digit_found = False
        # Find first digit starting from first character in the string
        for char in line:
            if char.isdigit():
                print(f'First: {char}')
                collect_tmp = collect_tmp + char
                # End for loop, we found it.
                break
        # Find last digit, start from last character in the string
        # Note: in string(3fiveone), it would be First(3), Last(3), final number is 33
        for char in reversed(line):
            if char.isdigit():
                print(f'Last: {char}')
                # Combine the numbers
                collect_tmp = collect_tmp + char
                # Convert to an interger then add it to the total sum
                sum += int(collect_tmp)
                collect_tmp = ''
                # End for loop, we found it.
                break 
# Print Total Sum
print(f'SUM: {sum}')
