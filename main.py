# Sean A
# Merge Sort
# Use our knowledge of algorithms to make a merge sort algorithm

def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        firstHalf = mergeSort(nums[mid:])
        secondHalf = mergeSort(nums[:mid])
        firstIndex = 0
        secondIndex = 0
        newList = []
        while firstIndex < len(firstHalf) and secondIndex < len(secondHalf):
            if firstHalf[firstIndex] < secondHalf[secondIndex]:
                newList.append(firstHalf[firstIndex])
                firstIndex += 1
            else:
                newList.append(secondHalf[secondIndex])
                secondIndex += 1
        if len(firstHalf) == firstIndex:
            newList.extend(secondHalf[secondIndex:])
        else:
            newList.extend(firstHalf[firstIndex:])
        return newList
    else:
        return nums


def main():
    nums1 = [6, 2, 5, 8, 3, 4, 8]
    nums2 = [1, 2, 3, 4, 5, 6, 7, 8]
    nums3 = [8, 2, 6, 0, 1, 3]

    for num_list in [nums1, nums2, nums3]:
        print(f"\nOriginal: {num_list}")
        new = mergeSort(num_list)
        print(f"Sorted: {new}\n")


if __name__ == "__main__":
    main()
