#binary search with recursion
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
l1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
n=int(input("Enter the number to search: "))
result = binary_search(l1, n, 0, len(l1) - 1)
if result != -1:
    print(f"Element found at index: {result}")
else:   print("Element not found in the list.") 