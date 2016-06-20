nums = []
for i in range(1, 9):
    for j in range(0, 9)-i:
        for m in range(0, 9)-i-j:
            for n in range(0, 9)-i-j-m:
                nums = nums+i*1000+j*100+m*10+n
print(nums)
# numbers = {}
#
# for i in range(0, 6):
#     number = input('input a number:')
#     a = input('input a:')
#     b = input('input b:')
#     dict1 = {number: [a, b]}
#     numbers.update(dict1)
# print(numbers)
# number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# tmp = []

