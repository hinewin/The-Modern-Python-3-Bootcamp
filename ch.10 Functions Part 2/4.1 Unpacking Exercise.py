# Function called count_sevens and need to call it twice
# First call with the arguments 1,4,7 and save results
# in variable result1

# 2nd, call the same count_sevens, passing
# in all numbers contained in nums
# list as individual arguments (unpack list)
# save that in result 2

def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]

### No Touching ######################

result1 = count_sevens(1,4,7,7) # count how many 7 are in the given list
result2 = count_sevens(*nums) # now count it throughout the whole list
# instead of just a single item (the list)
print (result1)
print (result2)