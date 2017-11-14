def collatz(n):
    if (n % 2 == 0):
        n = n/2
        return n
    else:
        n = 3*n+1
        return n

while True:
    try:
        n = int(input("Enter number: "))
    except ValueError:
        print('Error: Entry must be an integer.')
        continue
    if n < 1:
        print('Error: Enter a POSITIVE integer!')
    else:
        print(n)
        while n != 1:
            n = int(collatz(int(n)))
            print(n)
    
    
        
