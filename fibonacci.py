n = int(input("Enter a number: "))

step_count1 = 0
step_count2 = 0

def iterative_fibonacci(n):
    global step_count1
    a, b = 0, 1
    
    for _ in range(n):
        print(a, end = " ")
        a, b = b, a + b
        step_count1 += 1
        
print("\nIterative Fibonacci Series:")
iterative_fibonacci(n)
print("\nStep count:", step_count1)

def recursive_fibonacci(n):
    global step_count2
    step_count2 += 1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)
    
print("\nRecursive Fibonacci Series:")
for i in range(n):
    print(recursive_fibonacci(i), end = " ")
print("\nStep count:", step_count2)

