🔢 Fibonacci Series in Python (Using Loop)

This Python program generates the Fibonacci series up to n terms using an iterative (loop-based) approach.

📌 Features

Takes number of terms as input

Uses loop-based logic

Beginner-friendly implementation

Interview-ready solution

Efficient iterative approach

💻 Technology Used

Python 3

🚀 How It Works

The program takes the number of terms (n) as input.

Initializes the first two Fibonacci numbers as 0 and 1.

Uses a for loop to calculate the next terms.

Each next term is calculated as:

next_term = first + second

Updates values and continues until n terms are printed.

📝 Code
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
▶️ Example

Input:

Enter number of terms: 6

Output:

Fibonacci series:
0 1 1 2 3 5


🎯 Learning Concepts

Loops (for)

Variable updating

Basic mathematical logic

Sequence generation

Conditional statements
