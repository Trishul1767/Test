nums=[1,2,3,1,2,1,2,3,4,1]
longest = 0
best_sequence = []
for i in range(len(nums)):
    current=nums[i]
    temp_sequence = [current]
    while current +1 in nums:
        current += 1
        temp_sequence.append(current)
    if len(temp_sequence) > longest:
        longest = len(temp_sequence)
        best_sequence = temp_sequence
print("Longest consecutive sequence:", best_sequence)