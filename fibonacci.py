# Program to print Fibonacci series up to n terms

n = int(input("Enter number of terms: "))

first = 0
second = 1

if n <= 0:
    print("Please enter a positive number")
elif n == 1:
    print("Fibonacci series:")
    print(first)
else:
    print("Fibonacci series:")
    print(first, second, end=" ")
    
    for i in range(2, n):
        next_term = first + second
        print(next_term, end=" ")
        first = second
        second = next_term
