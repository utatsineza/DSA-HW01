# Sparse Matrix Operations

## Overview
This project implements a Sparse Matrix data structure and supports basic matrix operations: **Addition, Subtraction, and Multiplication**. The program reads two sparse matrices from input files, processes them efficiently, and outputs the result.

## Features
- Reads sparse matrices from text files.
- Stores data efficiently using a dictionary-based approach.
- Supports matrix **addition, subtraction, and multiplication**.
- Handles incorrect file formats with error handling.
- Works efficiently on large datasets.

## Input File Format
Each matrix file follows this format:
```
rows=3
cols=3
(0,0,5)
(1,2,8)
(2,1,3)
```
- First line specifies number of rows.
- Second line specifies number of columns.
- Subsequent lines define matrix elements `(row, column, value)`.

## How to Run
1. **Navigate to the project directory:**
   ```sh
   cd dsa/sparse_matrix/code/src
   ```

2. **Run the Python script:**
   ```sh
   python sparse_matrix_operations.py
   ```

3. **Follow on-screen prompts:**
   - Enter the paths of two matrix files.
   - Choose an operation (Addition, Subtraction, Multiplication).
   - View the result printed to the console.

## Example Usage
### Sample Input Files
**matrix1.txt**:
```
rows=3
cols=3
(0,0,2)
(1,1,4)
(2,2,6)
```

**matrix2.txt**:
```
rows=3
cols=3
(0,0,3)
(1,1,5)
(2,2,7)
```

### Expected Output (Addition)
```
Sparse Matrix Result:
(0,0,5)
(1,1,9)
(2,2,13)
```

## Error Handling
- **Whitespace in files** → Ignored automatically.
- **Incorrect format (e.g., missing parentheses, wrong data types)** → Raises `std::invalid_argument("Input file has wrong format")`.
- **Invalid operations (e.g., mismatched dimensions for multiplication)** → Displays an error message and exits.
