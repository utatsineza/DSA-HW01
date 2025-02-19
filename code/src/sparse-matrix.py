class SparseMatrix:
    def __init__(self, matrix_file_path=None, num_rows=None, num_cols=None):
        """
        Initializes a sparse matrix either from a file or with given dimensions.

        :param matrix_file_path: Path to the file containing the matrix
        :param num_rows: Number of rows for an empty matrix
        :param num_cols: Number of columns for an empty matrix
        """
        if matrix_file_path:
            self.data, self.rows, self.cols = self.load_from_file(matrix_file_path)
        else:
            self.data = {}  # Dictionary to store nonzero elements as {(row, col): value}
            self.rows = num_rows
            self.cols = num_cols

    def load_from_file(self, file_path):
        """
        Reads a sparse matrix from a file and stores it efficiently in a dictionary.
        
        :param file_path: Path to the file containing the sparse matrix
        :return: Dictionary representation of sparse matrix and its dimensions
        """
        data = {}
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()

                # Read the number of rows and columns
                rows = int(lines[0].strip().split('=')[1])
                cols = int(lines[1].strip().split('=')[1])

                # Parse nonzero elements
                for line in lines[2:]:
                    line = line.strip()
                    if line:
                        # Validate format (must be in (row, col, value) format)
                        if not (line.startswith("(") and line.endswith(")")):
                            raise ValueError("Input file has wrong format")
                        
                        # Extract row, col, value
                        parts = line[1:-1].split(',')
                        if len(parts) != 3:
                            raise ValueError("Input file has wrong format")

                        r, c, v = int(parts[0]), int(parts[1]), int(parts[2])
                        data[(r, c)] = v  # Store only nonzero values

                return data, rows, cols

        except Exception as e:
            raise ValueError(f"Error reading file: {str(e)}")

    def get_element(self, row, col):
        """
        Retrieves the value at a given row and column.
        Returns 0 if the element is not explicitly stored.

        :param row: Row index
        :param col: Column index
        :return: Value at (row, col)
        """
        return self.data.get((row, col), 0)

    def set_element(self, row, col, value):
        """
        Sets the value at a given position.
        If value is zero, it removes the entry to maintain sparsity.

        :param row: Row index
        :param col: Column index
        :param value: Value to set
        """
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def add(self, other):
        """
        Adds two sparse matrices.

        :param other: Another SparseMatrix object
        :return: New SparseMatrix object (result of addition)
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition")

        result = SparseMatrix(num_rows=self.rows, num_cols=self.cols)

        # Add elements from self
        for (r, c), v in self.data.items():
            result.set_element(r, c, v + other.get_element(r, c))

        # Add elements from other (that are not in self)
        for (r, c), v in other.data.items():
            if (r, c) not in self.data:
                result.set_element(r, c, v)

        return result

    def subtract(self, other):
        """
        Subtracts another sparse matrix from the current matrix.

        :param other: Another SparseMatrix object
        :return: New SparseMatrix object (result of subtraction)
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for subtraction")

        result = SparseMatrix(num_rows=self.rows, num_cols=self.cols)

        # Subtract elements from self
        for (r, c), v in self.data.items():
            result.set_element(r, c, v - other.get_element(r, c))

        # Subtract elements from other (that are not in self)
        for (r, c), v in other.data.items():
            if (r, c) not in self.data:
                result.set_element(r, c, -v)

        return result

    def multiply(self, other):
        """
        Multiplies two sparse matrices.

        :param other: Another SparseMatrix object
        :return: New SparseMatrix object (result of multiplication)
        """
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions must be compatible for multiplication")

        result = SparseMatrix(num_rows=self.rows, num_cols=other.cols)

        # Matrix multiplication
        for (r1, c1), v1 in self.data.items():
            for c2 in range(other.cols):
                v2 = other.get_element(c1, c2)
                if v2 != 0:
                    result.set_element(r1, c2, result.get_element(r1, c2) + v1 * v2)

        return result

    def display(self):
        """
        Prints the nonzero elements of the sparse matrix in (row, col, value) format.
        """
        for (r, c), v in sorted(self.data.items()):
            print(f"({r}, {c}, {v})")

# ---------------- Main Program ----------------
def main():
    print("Sparse Matrix Operations")
    
    # File paths (update these based on actual files)
    file1 = "matrix1.txt"
    file2 = "matrix2.txt"

    try:
        # Load matrices
        matrix1 = SparseMatrix(matrix_file_path=file1)
        matrix2 = SparseMatrix(matrix_file_path=file2)

        while True:
            print("\nChoose an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                result = matrix1.add(matrix2)
                print("\nResult of Addition:")
                result.display()
            elif choice == "2":
                result = matrix1.subtract(matrix2)
                print("\nResult of Subtraction:")
                result.display()
            elif choice == "3":
                result = matrix1.multiply(matrix2)
                print("\nResult of Multiplication:")
                result.display()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
