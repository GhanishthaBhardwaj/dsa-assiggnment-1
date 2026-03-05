# AERT - Algorithmic Efficiency & Recursion Toolkit
# Name: Ghanishtha Bhardwaj
# Course: B.Tech CSE (AI ML), 2nd Semester
# Roll No: 2501730296


# Part A: Stack Implementation
class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.empty():
            return self.data.pop()
        return None

    def top(self):
        if not self.empty():
            return self.data[-1]
        return None

    def empty(self):
        return len(self.data) == 0

    def length(self):
        return len(self.data)


# Part B: Factorial using Recursion
def factorial_recursive(num):
    if num < 0:
        return "Invalid input"
    if num == 0 or num == 1:
        return 1
    return num * factorial_recursive(num - 1)


# Fibonacci (Simple Recursive)
simple_count = 0
def fibonacci_simple(n):
    global simple_count
    simple_count += 1

    if n <= 1:
        return n

    return fibonacci_simple(n - 1) + fibonacci_simple(n - 2)


# Fibonacci (Using Memoization)
memo_count = 0
def fibonacci_memo(n, cache=None):
    global memo_count
    memo_count += 1

    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]

    if n <= 1:
        cache[n] = n
    else:
        cache[n] = fibonacci_memo(n - 1, cache) + fibonacci_memo(n - 2, cache)

    return cache[n]


# Part C: Tower of Hanoi
def tower_of_hanoi(disks, src, aux, dest, move_stack):

    if disks == 1:
        step = f"Move disk 1 from {src} to {dest}"
        move_stack.push(step)
        print(step)
        return

    tower_of_hanoi(disks - 1, src, dest, aux, move_stack)

    step = f"Move disk {disks} from {src} to {dest}"
    move_stack.push(step)
    print(step)

    tower_of_hanoi(disks - 1, aux, src, dest, move_stack)


# Part D: Recursive Binary Search
def recursive_binary_search(array, target, start, end):

    if start > end:
        return -1

    middle = (start + end) // 2

    if array[middle] == target:
        return middle

    elif target < array[middle]:
        return recursive_binary_search(array, target, start, middle - 1)

    else:
        return recursive_binary_search(array, target, middle + 1, end)


# Main Driver Function
def run_tests():

    print("Factorial Test Cases:")
    for value in [0, 1, 5, 10]:
        print(f"Factorial({value}) =", factorial_recursive(value))


    print("\nFibonacci Test Cases:")

    for value in [5, 10, 20, 30]:

        global simple_count, memo_count

        simple_count = 0
        result_simple = fibonacci_simple(value)

        print(f"\nSimple Fibonacci({value}) =", result_simple)
        print("Function Calls (Simple) =", simple_count)

        memo_count = 0
        result_memo = fibonacci_memo(value)

        print(f"Memoized Fibonacci({value}) =", result_memo)
        print("Function Calls (Memoized) =", memo_count)


    print("\nTower of Hanoi Test:")

    stack_obj = Stack()
    tower_of_hanoi(3, 'A', 'B', 'C', stack_obj)

    print("\nTotal Moves Stored in Stack:", stack_obj.length())


    print("\nBinary Search Test:")

    numbers = [1, 3, 5, 7, 9, 11, 13]

    for key in [7, 1, 13, 2]:
        position = recursive_binary_search(numbers, key, 0, len(numbers) - 1)
        print(f"Search {key} -> Index:", position)

    empty_list = []
    print("Search in empty list:", recursive_binary_search(empty_list, 5, 0, -1))


if __name__ == "__main__":
    run_tests()