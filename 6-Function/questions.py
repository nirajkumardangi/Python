# Q1. Print positive and negative elemnts of an list

# lists = [10, 30, -19, 80, -20, -12]

# positive_element = []
# negative_element = []

# def element_filter(lists):
#     for num in lists:
#         if num > 0:
#             positive_element.append(num)
#         else:
#             negative_element.append(num)
            
# element_filter(lists)

# print("Positive elements: ", positive_element)
# print("Negative elements: ", negative_element)


# Q2. Find smallest element on a list

# lists = [20, 40, 50, 10, 20, 70]

# def smallest_element(lists):
#     smallest = lists[0]
#     for i in range(1, len(lists)):
#         if lists[i] < smallest:
#             smallest = lists[i]
#     return smallest

# print("Smallest element:", smallest_element(lists))


# Q3. Find the greatest element

# def greatest_element(lists):
#     largest = lists[0]
#     for i in range(len(lists)):
#         if lists[i] > largest:
#             largest = lists[i]
    
#     return largest
    
# print("Largest element: ", greatest_element([20, 40, 50, 10, 20]))


# Q4. Find second largest element

def second_largest(lists):
    first_largest = lists[0]
    second_largest = lists[1]
    for i in range(len(lists)):
        if lists[i] > first_largest:
            second_largest = first_largest
            first_largest = lists[i]
            
        elif lists[i] > second_largest:
            second_largest = lists[i]
    
    return second_largest    
    
print("Second larest element: ", second_largest([20, 40, 60, 50]))