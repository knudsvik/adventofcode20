#filename = 'day9_test.txt'
filename = 'day9.txt'

data = open(filename, 'r')
lines = data.readlines()
data.close()

#preamble = 5
preamble = 25
working = True
numbers = []

for line in lines:
    numbers.append(int(line.split()[0]))

while working:
    for i in range(0, len(numbers) - preamble):
        num_to_check_success = False
        num_to_check = numbers[preamble + i]
        for x in range(i, i + preamble -1):
            for y in range(x + 1, i + preamble):
                if numbers[x] + numbers[y] == num_to_check:
                    num_to_check_success = True
        if not num_to_check_success:
            print(num_to_check, ' is not working')
            working = False
            
            for j in range(0, len(numbers) - preamble):
                list_of_tries = [numbers[j]]
                for k in range(j + 1, len(numbers)):
                    list_of_tries.append(numbers[k])
                    if sum(list_of_tries) == num_to_check:
                        print('Fant en løsning!')
                        print('Listen:', list_of_tries)
                        print('Svar:', min(list_of_tries) + max(list_of_tries))