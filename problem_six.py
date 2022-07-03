#This function helps to swap a number
def swap(array):
    pos=sorted(list(enumerate(array)),key=lambda x: x[1])
    counts=0

    for index in range(len(array)):
        while True:
            if (pos[index][0] == index):
                break
            else:
                counts+=1
                swap_index=pos[index][0]
                pos[index], pos[swap_index]=pos[swap_index], pos[index]
    return counts

#used to return minimum number
def minimum(array):
    return min(swap(array),swap(array[::-1]))

#Print our numbers in the list and minimum number after swapping 2 numbers
nums=[12,6,8,9,32,5,3,2]
print("numbers is:",nums)
print("Minimum number after swapping 2 numbers is:",minimum(nums))            