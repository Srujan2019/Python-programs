import time

# Menu-driven main function
def main():
    while True:
        print("\n--- Data Structures and Algorithms ---")
        print("1. Basic Data Structures")
        print("2. Abstract Data Types (ADT)")
        print("3. Stack Operations")
        print("4. Linear Search")
        print("5. Bubble Sort")
        print("6. Selection Sort")
        print("7. Insertion Sort")
        print("8. Binary Search (Iterative)")
        print("9. Binary Search (Recursive)")
        print("10. Fibonacci Sequence (Dynamic Programming)")
        print("11. Singly Linked List")
        print("12. Doubly Linked List")
        print("13. Circular Linked List")
        print("14. Stack (Using List)")
        print("15. Bracket Matching")
        print("16. Recursive Operations (Factorial/Fibonacci)")
        print("17. Towers of Hanoi")
        print("18. Queue")
        print("19. Priority Queue")
        print("20. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            basic_data_structures()
        elif choice == 2:
            abstract_data_type()
        elif choice == 3:
            stack_operations()
        elif choice == 4:
            linear_search()
        elif choice == 5:
            bubble_sort()
        elif choice == 6:
            selection_sort()
        elif choice == 7:
            insertion_sort()
        elif choice == 8:
            binary_search_iterative()
        elif choice == 9:
            binary_search_recursive()
        elif choice == 10:
            fibonacci_sequence()
        elif choice == 11:
            singly_linked_list()
        elif choice == 12:
            doubly_linked_list()
        elif choice == 13:
            circular_linked_list()
        elif choice == 14:
            stack_using_list()
        elif choice == 15:
            bracket_matching()
        elif choice == 16:
            recursive_operations()
        elif choice == 17:
            towers_of_hanoi()
        elif choice == 18:
            queue_operations()
        elif choice == 19:
            priority_queue_operations()
        elif choice == 20:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

# Define each function
def basic_data_structures():
    print("List:", [1, 2, "ABC", 3, "xyz", 2.3])
    print("Dictionary:", {"a": 134, "b": 266, "c": 343})
    print("Tuples:", (10, 20, 30, 40, 50, 40))
    print("Sets:", {10, 30, 20, 40, 50})

def abstract_data_type():
    class Date:
        def __init__(self, day, month, year):
            self.day = day
            self.month = month
            self.year = year

        def display(self):
            print(f"Date: {self.day}/{self.month}/{self.year}")
            months = ["Unknown", "January", "February", "March", "April", "May", "June", 
                      "July", "August", "September", "October", "November", "December"]
            print("Month Name:", months[self.month])
            print("Leap Year:" if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0) else "Not a Leap Year")

    d = Date(3, 8, 2000)
    d.display()

import time

# Menu-driven main function
def main():
    while True:
        print("\n--- Data Structures and Algorithms ---")
        print("1. Basic Data Structures")
        print("2. Abstract Data Types (ADT)")
        print("3. Stack Operations")
        print("4. Linear Search")
        print("5. Bubble Sort")
        print("6. Selection Sort")
        print("7. Insertion Sort")
        print("8. Binary Search (Iterative)")
        print("9. Binary Search (Recursive)")
        print("10. Fibonacci Sequence (Dynamic Programming)")
        print("11. Singly Linked List")
        print("12. Doubly Linked List")
        print("13. Circular Linked List")
        print("14. Stack (Using List)")
        print("15. Bracket Matching")
        print("16. Recursive Operations (Factorial/Fibonacci)")
        print("17. Towers of Hanoi")
        print("18. Queue")
        print("19. Priority Queue")
        print("20. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            basic_data_structures()
        elif choice == 2:
            abstract_data_type()
        elif choice == 3:
            stack_operations()
        elif choice == 4:
            linear_search()
        elif choice == 5:
            bubble_sort()
        elif choice == 6:
            selection_sort()
        elif choice == 7:
            insertion_sort()
        elif choice == 8:
            binary_search_iterative()
        elif choice == 9:
            binary_search_recursive()
        elif choice == 10:
            fibonacci_sequence()
        elif choice == 11:
            singly_linked_list()
        elif choice == 12:
            doubly_linked_list()
        elif choice == 13:
            circular_linked_list()
        elif choice == 14:
            stack_using_list()
        elif choice == 15:
            bracket_matching()
        elif choice == 16:
            recursive_operations()
        elif choice == 17:
            towers_of_hanoi()
        elif choice == 18:
            queue_operations()
        elif choice == 19:
            priority_queue_operations()
        elif choice == 20:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

# Define each function
def basic_data_structures():
    print("List:", [1, 2, "ABC", 3, "xyz", 2.3])
    print("Dictionary:", {"a": 134, "b": 266, "c": 343})
    print("Tuples:", (10, 20, 30, 40, 50, 40))
    print("Sets:", {10, 30, 20, 40, 50})

def abstract_data_type():
    class Date:
        def __init__(self, day, month, year):
            self.day = day
            self.month = month
            self.year = year

        def display(self):
            print(f"Date: {self.day}/{self.month}/{self.year}")
            months = ["Unknown", "January", "February", "March", "April", "May", "June", 
                      "July", "August", "September", "October", "November", "December"]
            print("Month Name:", months[self.month])
            print("Leap Year:" if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0) else "Not a Leap Year")

    d = Date(3, 8, 2000)
    d.display()

def stack_operations():
    stack = []
    while True:
        print("\nStack Operations")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if Stack is Empty")
        print("5. Display Stack")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            element = input("Enter the element to push: ")
            stack.append(element)
            print(f"{element} pushed to stack")
        elif choice == 2:
            if stack:
                element = stack.pop()
                print(f"{element} popped from stack")
            else:
                print("Stack is empty!")
        elif choice == 3:
            if stack:
                print(f"Top element is: {stack[-1]}")
            else:
                print("Stack is empty!")
        elif choice == 4:
            print("Stack is empty!" if not stack else "Stack is not empty!")
        elif choice == 5:
            print("Stack contents:", stack)
        elif choice == 6:
            break
        else:
            print("Invalid choice!")

def linear_search():
    arr = [10, 20, 30, 40, 50]
    target = int(input("Enter the number to search: "))
    for index, value in enumerate(arr):
        if value == target:
            print(f"Element found at index {index}")
            return
    print("Element not found!")

def bubble_sort():
    arr = [64, 34, 25, 12, 22, 11, 90]
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Sorted array:", arr)

def selection_sort():
    arr = [64, 25, 12, 22, 11]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Sorted array:", arr)

def insertion_sort():
    arr = [12, 11, 13, 5, 6]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print("Sorted array:", arr)

def binary_search_iterative():
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target = int(input("Enter the element to search: "))
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            print(f"Element found at index {mid}")
            return
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print("Element not found!")

def binary_search_recursive():
    def binary_search(arr, target, low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)

    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target = int(input("Enter the element to search: "))
    result = binary_search(arr, target, 0, len(arr) - 1)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found!")

def fibonacci_sequence():
    n = int(input("Enter the number of terms in Fibonacci sequence: "))
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    print("Fibonacci sequence:", fib)

def singly_linked_list():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            new_node = Node(data)
            if not self.head:
                self.head = new_node
            else:
                last = self.head
                while last.next:
                    last = last.next
                last.next = new_node

        def display(self):
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.display()

def doubly_linked_list():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    class DoublyLinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            new_node = Node(data)
            if not self.head:
                self.head = new_node
            else:
                last = self.head
                while last.next:
                    last = last.next
                last.next = new_node
                new_node.prev = last

        def display(self):
            current = self.head
            while current:
                print(current.data, end=" <-> ")
                current = current.next
            print("None")

    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.display()

def circular_linked_list():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class CircularLinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            new_node = Node(data)
            if not self.head:
                self.head = new_node
                new_node.next = self.head
            else:
                last = self.head
                while last.next != self.head:
                    last = last.next
                last.next = new_node
                new_node.next = self.head

        def display(self):
            if not self.head:
                print("Empty list")
                return
            current = self.head
            while True:
                print(current.data, end=" -> ")
                current = current.next
                if current == self.head:
                    break
            print("None")

    cll = CircularLinkedList()
    cll.append(10)
    cll.append(20)
    cll.append(30)
    cll.display()

def stack_using_list():
    stack = []
    while True:
        print("\nStack Operations")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if Stack is Empty")
        print("5. Display Stack")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            element = input("Enter the element to push: ")
            stack.append(element)
            print(f"{element} pushed to stack")
        elif choice == 2:
            if stack:
                element = stack.pop()
                print(f"{element} popped from stack")
            else:
                print("Stack is empty!")
        elif choice == 3:
            if stack:
                print(f"Top element is: {stack[-1]}")
            else:
                print("Stack is empty!")
        elif choice == 4:
            print("Stack is empty!" if not stack else "Stack is not empty!")
        elif choice == 5:
            print("Stack contents:", stack)
        elif choice == 6:
            break
        else:
            print("Invalid choice!")

def bracket_matching():
    def is_balanced(expression):
        stack = []
        matching_brackets = {')': '(', '}': '{', ']': '['}
        for char in expression:
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if stack and stack[-1] == matching_brackets[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

    expression = input("Enter an expression with brackets: ")
    if is_balanced(expression):
        print("Brackets are balanced.")
    else:
        print("Brackets are not balanced.")

def recursive_operations():
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    choice = int(input("Choose operation: 1. Factorial 2. Fibonacci: "))
    if choice == 1:
        num = int(input("Enter a number for factorial: "))
        print(f"Factorial of {num} is {factorial(num)}")
    elif choice == 2:
        num = int(input("Enter a number for Fibonacci: "))
        print(f"Fibonacci of {num} is {fibonacci(num)}")

def towers_of_hanoi():
    def hanoi(n, source, target, auxiliary):
        if n == 1:
            print(f"Move disk 1 from {source} to {target}")
        else:
            hanoi(n - 1, source, auxiliary, target)
            print(f"Move disk {n} from {source} to {target}")
            hanoi(n - 1, auxiliary, target, source)

    num_disks = int(input("Enter the number of disks: "))
    hanoi(num_disks, 'A', 'C', 'B')

def queue_operations():
    class Queue:
        def __init__(self):
            self.queue = []

        def enqueue(self, item):
            self.queue.append(item)
            print(f"{item} added to queue.")

        def dequeue(self):
            if self.queue:
                item = self.queue.pop(0)
                print(f"{item} removed from queue.")
            else:
                print("Queue is empty!")

        def display(self):
            print("Queue contents:", self.queue)

    q = Queue()
    while True:
        print("\nQueue Operations")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            item = input("Enter item to enqueue: ")
            q.enqueue(item)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice!")

def priority_queue_operations():
    import heapq

    class PriorityQueue:
        def __init__(self):
            self.pq = []

        def enqueue(self, priority, item):
            heapq.heappush(self.pq, (priority, item))
            print(f"Item {item} with priority {priority} added.")

        def dequeue(self):
            if self.pq:
                priority, item = heapq.heappop(self.pq)
                print(f"Item {item} with priority {priority} removed.")
            else:
                print("Priority Queue is empty!")

        def display(self):
            print("Priority Queue contents:", [item[1] for item in self.pq])

    pq = PriorityQueue()
    while True:
        print("\nPriority Queue Operations")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            priority = int(input("Enter priority: "))
            item = input("Enter item to enqueue: ")
            pq.enqueue(priority, item)
        elif choice == 2:
            pq.dequeue()
        elif choice == 3:
            pq.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice!")

# Start the program
if __name__ == "__main__":
    main()
