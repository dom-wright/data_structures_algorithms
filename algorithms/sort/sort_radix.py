'''
Radix Sort

Radix sort is a non-comparative sorting algorithm that sorts data by processing individual digits or groups of digits of the numbers being sorted. It works by distributing the elements into different "buckets" or "bins" based on the values of their digits. Then it recombines the buckets and repeats the process on the next positioned digit. Progressively the bucket will become sorted.

Steps:
- Determine the maximum number of digits among all the elements in the list.
- Start with the least significant digit (rightmost digit) and perform a stable sort on the list using that digit as the key.
- After sorting the elements based on the least significant digit, gather them back into a single list.
- Repeat steps 2 and 3 for each subsequent digit, moving from right to left, until all digits have been processed. Each pass sorts the elements based on the next more significant digit.
- After processing all the digits, the list will be sorted in ascending order.

Runtime:
Radix sort has a linear time complexity of O(d * (n + k)), where n is the number of elements, d is the maximum number of digits, and k is the range of digit values. This linear time complexity makes radix sort efficient for large datasets when d and k are small.

When to use:
- Fixed-Length Keys: Effective when the keys being sorted have a fixed length.
- Small Range of Key Values: Relatively small range of keys compared to the number of elements.
'''


def radix_sort(to_be_sorted):
    being_sorted = to_be_sorted[:]
    maximum_value = max(being_sorted)
    max_exponent = len(str(maximum_value))

    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position

        digits = [[] for i in range(10)]

        for number in being_sorted:
            number_as_a_string = str(number)
            try:
                digit = number_as_a_string[index]
            except IndexError:
                digit = 0
            digit = int(digit)

            digits[digit].append(number)

        print(f"Index position {index}: {digits}")

        being_sorted = []
        for numeral in digits:
            being_sorted.extend(numeral)

        print(f"Round {position} complete: {being_sorted}")

    return being_sorted


unsorted_list = [500, 153, 57, 6]

# unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199,
#                  535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]

sorted_list = radix_sort(unsorted_list)
print(sorted_list)
