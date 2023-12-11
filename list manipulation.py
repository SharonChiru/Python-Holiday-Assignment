#ASSIGNMENT 1:
#create a python script that reads a list of numbers
numbers = [2, 5, 8, 10, 12, 102,365, 14, 22, 25, 9]

#Implement functions to find the sum, average , maximum and minimum of the numbers
#sum
Sum = sum(numbers)
print("Sum of numbers: ", Sum)

#average
 #we can find the average of a list by simply using the sum() and len() functions.
#sum(): Using sum() function we can get the sum of the list.
#len(): len() function is used to get the length or the number of elements in a list.

average = sum(numbers)/len(numbers)
print("Average of numbers: ", average)

#maximum and minimum of the numbers
max_num = max(numbers)
print("Maximum number:", max_num)
min_num = min(numbers)
print("Minimum number:", min_num)

#implement a function to filter out even numbers from the list
def filter_even_numbers(numbers):
    # Use the filter function to filter out even numbers
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    return odd_numbers

if __name__ == "__main__":
    # Use the filter_even_numbers function to get odd numbers
    odd_numbers = filter_even_numbers(numbers)

    # Display the original list and the filtered odd numbers
    print("Original list of numbers:", numbers)
    print("Odd numbers:", odd_numbers)



