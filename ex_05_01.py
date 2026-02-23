count = 0
total = 0

while True:
    sval = input('Enter a number: ')

    if sval == 'done':
        break

    try:
        ival = int(sval)
    except ValueError:
        print('Invalid input')
        continue

    count += 1
    total += ival

if count > 0:
    avg = total / count
else:
    avg = None

print(total, count, avg)
