# Heap Sort using Min Heap and Max Heap

def heapify(arr, n, i, heap_type):
    largest_or_smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if heap_type == "max":
        # Max Heap
        if left < n and arr[left] > arr[largest_or_smallest]:
            largest_or_smallest = left

        if right < n and arr[right] > arr[largest_or_smallest]:
            largest_or_smallest = right

    else:
        # Min Heap
        if left < n and arr[left] < arr[largest_or_smallest]:
            largest_or_smallest = left

        if right < n and arr[right] < arr[largest_or_smallest]:
            largest_or_smallest = right

    if largest_or_smallest != i:
        arr[i], arr[largest_or_smallest] = arr[largest_or_smallest], arr[i]

        heapify(arr, n, largest_or_smallest, heap_type)

def heap_sort(arr, heap_type):
    n = len(arr)

    # Build heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, heap_type)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, heap_type)

    return arr

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("\n1. Min Heap - Descending Order")
print("2. Max Heap - Ascending Order")

choice = int(input("Enter choice: "))

if choice == 1:
    result = heap_sort(arr, "min")
    print("Sorted in Descending Order:", result)

elif choice == 2:
    result = heap_sort(arr, "max")
    print("Sorted in Ascending Order:", result)

else:
    print("Invalid choice!")
