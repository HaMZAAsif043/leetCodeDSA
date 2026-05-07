# LeetCode

## Array:

1. **SmallerNumbersThanCurrent** -> brute force using enumerate (O(n²))
   - loop through each element, count how many others are smaller
   - better approach: sort + rank using sorted(enumerate(nums))

2. **TwoSum** -> HashMap (complement lookup) O(n)
   - complement = target - current number
   - store each number in a dict {value: index}
   - check if complement already exists in dict BEFORE adding current
   - note: enumerate brute force works but is O(n²) — avoid in interviews

3. **Find All Disappeared Numbers** -> set difference
   - convert nums to a set
   - return all numbers in range(1, len(nums)+1) not in the set
   - watch out: range is 1 to n inclusive, easy to off-by-one

4. **MissingNumber** -> Gauss formula (expected - actual)
   - expected = n * (n+1) // 2
   - actual = sum(nums)
   - answer = expected - actual
   - watch out: n = len(nums), range is 0..n so n+1 total numbers

5. **Spiral Matrix** -> matrix layer peeling using pop()
   - peel the matrix layer by layer until empty
   - 4 steps each iteration:
     - pop(0) -> top row left to right
     - row.pop() for each row -> right column top to bottom
     - pop()[::-1] -> bottom row right to left
     - row.pop(0) for each row reversed -> left column bottom to top
   - watch out: check `if matrix and matrix[0]` after EACH step