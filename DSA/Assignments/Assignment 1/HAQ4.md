# Home Assignment: Question 4
## Problem Statement
Write a method to add two matrices. The header of the method is as follows: 

```java 
public static double[][] addMatrix(double[][] a, double[][] b)  
```
In  order  to  be  added,  the  two  matrices  must  have  the  same  dimensions  and  the  same  or 
compatible types of elements.

## Solution

```java
public class MatrixAddition {

    public static double[][] addMatrix(double[][] a, double[][] b) {
        if (a.length != b.length || a[0].length != b[0].length) {
            throw new IllegalArgumentException("Matrices must have the same dimensions.");
        }

        int rows = a.length;
        int cols = a[0].length;
        double[][] result = new double[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[i][j] = a[i][j] + b[i][j];
            }
        }

        return result;
    }

    public static void printMatrix(double[][] matrix) {
        for (double[] row : matrix) {
            for (double val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        double[][] matrix1 = {
            {1, 2, 3},
            {4, 5, 6}
        };

        double[][] matrix2 = {
            {7, 8, 9},
            {10, 11, 12}
        };

        System.out.println("Matrix 1:");
        printMatrix(matrix1);

        System.out.println("\nMatrix 2:");
        printMatrix(matrix2);

        double[][] result = addMatrix(matrix1, matrix2);

        System.out.println("\nSum of Matrix 1 and Matrix 2:");
        printMatrix(result);
    }
}

```

### Output
```
Matrix 1:
1.0 2.0 3.0 
4.0 5.0 6.0 

Matrix 2:
7.0 8.0 9.0 
10.0 11.0 12.0 

Sum of Matrix 1 and Matrix 2:
8.0 10.0 12.0 
14.0 16.0 18.0 

```