## The Two Number Sum

Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. If any two numbers in the input array sum
up to the target sum, the function should return them in an array, in any
order. If no two numbers sum up to the target sum, the function should return
an empty array.


Note that the target sum has to be obtained by summing two different integers
in the array; you can't add a single integer to itself in order to obtain the
target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.

Example input
```python
input = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
```
Your function should ouput
```python
[11, -1]
```

See below for function signature:
```python
def two_number_sum(input: list[int], target: int)-> list[int]:
    ...
```
