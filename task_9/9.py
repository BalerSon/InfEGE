s = open("/home/balerso/old study/PYege/9_23709.txt")

count = 0

for line in s:
    nums = sorted([int(x) for x in line.split()])
    
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        
    arr = list(freq.values())
    if (sorted(arr) == [1, 1, 2, 3]) or ((nums[0] + nums[1] + nums[2]) >= (nums[-2] + nums[-1])):
        count += 1
        
print(count)
