def binary_search(list, item):
    low = 0  # low and high keep track of which part of the list you'll search in
    high = len(list) - 1

    while low <= high:  # while you haven't narrowed it down to one element
        mid = (low + high) / 2  # check the middle element
        guess = list[mid]
        if guess == item:  # Found the item
            return mid
        if guess > item:  # The guess was too high
            high = mid - 1
        else:  # The guess was too low
            low = mid + 1
    return None  # The item doesn't exist


def test_binary_search(list, item):
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 3))  # => 1
    print(binary_search(my_list, -1))  # => None
