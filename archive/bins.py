n = int(input())
m = int(input())
numbers = [int(x) for x in input().split()]
queries = [int(x) for x in input().split()]

# numbers = [10, 20, 30, 40, 50]
# queries = [40, 10, 35, 15, 40, 20]

def binary_search(array, query):
    
    n = len(array)
    if n == 0:
        return -1
    if n == 1:
        if array[0] == query:
            return 1
        else:
            return -1
    if(array[n//2] == query):
        return n//2 + 1
    elif(array[n//2] < query):
        result = binary_search(array[((n//2) + 1):], query)
        if result == -1:
            return -1
        else:
            return n//2 + result + 1
    elif(array[n//2] > query):
        return binary_search(array[:n//2], query)

for query in queries:
    print(binary_search(numbers, query), end=" ")
    