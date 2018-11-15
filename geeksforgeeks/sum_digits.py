'''
https://www.geeksforgeeks.org/sum-digit-number-using-recursion/
'''

def sum_digits(digits):

    def helper(digits_list, total_sum):
        if not digits_list:
            return total_sum
        return helper(digits_list[1:], total_sum + digits_list[0])

    digits_list = [int(i) for i in str(digits)]
    total_sum = 0
    total_sum = helper(digits_list, total_sum)
    return total_sum

print(sum_digits(45632))
