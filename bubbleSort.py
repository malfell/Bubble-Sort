# write your bubble sort algorithm below

def bubble_sort(lst):
    # first FOR loop runs the bubble algorithm as many times as 
    # there are elements in the list (one less than length of list)
    # outer loop
    for i in range(len(lst)-1):
        # this variable determines if elements are swapped in passs through list
        # if not, then list is sorted, and function stops
        swapped = False

        print(f"iteration ")
        # second FOR loop compares all values in the list for each pass
        # inner loop
        for j in range(len(lst) - 1):
            print(f"comparing {lst[j], lst[j+1]}")
            # conditional statement in inner loop checks if element on the left
            # is greater than the element on the right. 
            if lst[j] > lst[j+1]:
                # if it is, switch the order of the elements
                lst[j], lst[j+1] = lst[j+1], lst[j]
                # if elements are swapped, value turns to True
                swapped = True
        
        if swapped == False:
            return
            
    # return value of list after it has been sorted
    return lst

# TESTING ZONE
sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")