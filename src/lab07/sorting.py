def bubble_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется.
 
    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([2, 2, 1]) -> [1, 2, 2]
    bubble_sort([]) -> []
    """
    nums = list(nums)
    for i in range(len(nums)-1):
        f = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

 
 
def insertion_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется.
    insertion_sort([3, 1, 2]) -> [1, 2, 3]
    insertion_sort([2, 2, 1]) -> [1, 2, 2]
    insertion_sort([]) -> []
    """
    nums = list(nums)
    for i in range(1, len(nums)):
        n = nums[i]
        j = i-1
        while j >= 0 and n < nums[j]:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = n
    return nums
 
 
def selection_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется.
    selection_sort([3, 1, 2]) -> [1, 2, 3]
    selection_sort([2, 2, 1]) -> [1, 2, 2]
    selection_sort([]) -> []
    """
    nums = list(nums)
    for i in range(len(nums)-1):
        min_n = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_n]:
                min_n = j
        nums[i], nums[min_n] = nums[min_n], nums[i]
    return nums