# Given a string ‘str’ of digits, find length of the longest substring of ‘str’,
# such that the length of the substring is 2k digits and 
# sum of left k digits is equal to the sum of right k digits.

# 从 k 最大的取值开始枚举

for _ in range(int(input().strip())):
    nums = list(map(int, [s for s in input().strip()]))
    k = int(len(nums) / 2) * 2
    maxLen = 0
    while k > 1:
        halfk = int(k / 2)
        for i in range(0, len(nums) - k + 1):
            suml = sum(nums[i:i+halfk])
            sumr = sum(nums[i+halfk:i+k])
            if suml == sumr:
                maxLen = max(maxLen, k)
                k = 0
                break
        k -= 2
    print(maxLen)