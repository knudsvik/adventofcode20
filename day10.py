#filename = 'day10_test.txt'
filename = 'day10_short.txt'
#filename = 'day10.txt'

data = open(filename, 'r')
adapters = data.readlines()
data.close()

jolts = []
for adapter in adapters:
    jolts.append(int(adapter.split()[0]))

jolts.sort()

count1 = 0
count3 = 1 # included last
output = 0

for i in range(0,len(jolts)):
    jolt = jolts[i]
    if jolt - output == 1:
        count1 += 1
    elif jolt - output == 3:
        count3 += 1
    output = jolts[i]

print('1 jolts:', count1)
print('3 jolts:', count3)
print('product:', count1*count3)

### B

output = 0
iteration = 0
sequences = [[jolts[0]]]
last_sequence = []

while True:

    for sequence in sequences:

        if sequence != last_sequence:

            while sequence[-1] < max(jolts):
                
                    last_jolt = sequence[-1]
                    
                    if last_jolt + 1 in jolts:
                        sequence.append(last_jolt + 1)
                    elif last_jolt + 2 in jolts:
                        sequence.append(last_jolt + 2)
                    elif last_jolt + 3 in jolts:
                        sequence.append(last_jolt + 3)
        
            sequences.append([jolts[0]])
            last_sequence = sequence
        
sequences = jolts

while True:
    for i in range(0, len(jolts):
        if jolts[i+1]

