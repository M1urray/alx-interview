# 2D Matrix Rotation

This Python program rotates an n x n 2D matrix 90 degrees clockwise in-place.

## Function Signature

```python
def rotate_2d_matrix(matrix):
```

## Input

The function takes a single parameter:

matrix (list of lists): An n x n 2D matrix to be rotated. The matrix is assumed to have 2 dimensions and will not be empty.

## Output

The function does not return anything. The matrix is edited in-place.

## Approach

The rotation is done in two steps:

Transposing the matrix: The elements are swapped across the diagonal.
Reversing each row: Each row is reversed to achieve the desired rotation.
Example
python
Copy code
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

rotate_2d_matrix(matrix)

 The matrix is rotated 90 degrees clockwise in-place:

 [

 [7, 4, 1],

 [8, 5, 2],

 [9, 6, 3]

 ]

## Time Complexity

The time complexity of the rotate_2d_matrix function is O(n^2), where n is the number of rows (or columns) in the matrix. This is because both the transposition and row reversal operations require iterating over all elements in the matrix.

## Space Complexity

The space complexity of the function is O(1) since the rotation is done in-place without requiring any additional data structures.

## Copy code

Feel free to customize the content and formatting of the README file.
