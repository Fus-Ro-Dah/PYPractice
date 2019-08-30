def printMove(fr, to):
    print(fr+'-->'+to)

def printStep(n):
    print('There are ' + str(2**n-1) + ' steps in total.')
    
def Hanoi(n, fr, to, spare):
    if n == 1:
        printMove(fr,to)
    else:
        Hanoi(n-1,fr,spare,to)
        Hanoi(1,fr,to,spare)
        Hanoi(n-1,spare,to,fr)

    


while True:
    n = int(input('Please enter the amount of the plates:'))
    Hanoi(n,'A','C','B')
    printStep(n)
    quit_or_not = input('If you want to quit, type "quit":')
    if quit_or_not.lower() == 'quit':
        break
