
filename = 'day13.txt'

input = open(filename, 'r')
start = int(input.readline().split('\n')[0])
buses = input.readline().split(',')

while 'x' in buses:
    buses.remove('x')
buses = [int(i) for i in buses] 

timestamp = 0
history = {}
history[timestamp] = buses
next_buses = buses.copy()

while timestamp <= start + 100:
    timestamp += 1
    history[timestamp] = []
    i = 0
    for bus in next_buses:
        if timestamp == bus:
            history[timestamp].append(buses[i])
            next_buses[i] = bus + buses[i]
        i += 1

not_found = True
timestamp = start

while not_found:
    if history[timestamp] != []:
        print('The bus is leaving at', timestamp)
        wait = timestamp - start
        print('You had to wait', wait)
        bus = min(history[timestamp])
        print('The bus ID is', bus)
        print('The answer is', bus * wait)
        not_found = False
    timestamp += 1