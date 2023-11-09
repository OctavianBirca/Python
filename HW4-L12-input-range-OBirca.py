


start = int(input('Input the first value: '))
end = int(input('Input the second value: '))

if start < end:
    while start <= end:
        print(start)
        start += 1

else:
    while end <= start:
        print(start)
        start -= 1
        
