# DAA-lab-practicals
pracricals
def MaxCrossingSum(A, low, mid, high):
left_sum = float('-inf')
total = 0
for i in range(mid, low - 1, -1):
total += A[i]
if total > left_sum:
left_sum = total
right_sum = float('-inf')
total = 0
for j in range(mid + 1, high + 1):
total += A[j]
if total > right_sum:
right_sum = total
return left_sum + right_sum
def MaxSubarraySum(A, low, high):
if low == high:
return A[low]
mid = (low + high) // 2
left_sum = MaxSubarraySum(A, low, mid)
right_sum = MaxSubarraySum(A, mid + 1, high)
cross_sum = MaxCrossingSum(A, low, mid, high)
return max(left_sum, right_sum, cross_sum)
def max_subarray_sum_with_constraint(resources, constraint):
n = len(resources)
max_sum = 0
current_sum = 0
start = 0
best_subarray = None
for end in range(n):
current_sum += resources[end]
while current_sum > constraint and start <= end:
current_sum -= resources[start]
start += 1
if current_sum <= constraint and current_sum > max_sum:
max_sum = current_sum
best_subarray = resources[start:end+1]

return max_sum, best_subarray
def run_tests():
test_cases = [
([2, 1, 3, 4], 5, "Test 1: Basic small array"),
([2, 2, 2, 2], 4, "Test 2: Exact match to constraint"),
([1, 5, 2, 3], 5, "Test 3: Single element equals constraint"),
([6, 7, 8], 5, "Test 4: No valid subarray"),
([1, 2, 3, 2, 1], 5, "Test 5: Multiple optimal subarrays"),
([1, 1, 1, 1, 1], 4, "Test 6: Large window valid"),
([4, 2, 3, 1], 5, "Test 7: Sliding window shrink needed"),
([], 10, "Test 8: Empty array"),
([1, 2, 3], 0, "Test 9: Constraint = 0"),
(list(range(1, 100001)), 10**9, "Test 10: Very large input"),
]
for resources, constraint, description in test_cases:
print(description)
max_sum, subarray = max_subarray_sum_with_constraint(resources, constraint)
print(f"Constraint: {constraint}")
print(f"Max Sum ≤ Constraint: {max_sum}")
print(f"Subarray: {subarray if subarray else 'No valid subarray'}\n")
run_tests()
