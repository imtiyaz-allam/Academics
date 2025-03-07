# 2 Dimensional Array
### Q) Create a 2D Array, insert elements into it and display the elements.
```java
import java.util.Scanner;
public class Test {
    public static void main(String[] args) {
        System.out.print("Enter number of rows and column 2-D Array: ");
        int r = sc.nextInt();
        int c = sc.nextInt();
        int[][] arr1 = new int[r][c];
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++) {
                System.out.printf("Enter element at row %d column %d: ", i + 1, j + 1);
                arr1[i][j] = sc.nextInt();
            }
        for (int i = 0; i < r; i++){
            for (int j = 0; j < c; j++) {
                System.out.printf(arr1[i][j] + "\t");
            }
            System.out.println();
        }
    }
}
```

### Q) Write a method to display the elements of 2D array
```java
static void display(int[][] matrix) {
    for (int i = 0; i < matrix.length; i++) {
        for (int j = 0; j < matrix[i].length; j++)
            System.out.print(matrix[i][j] + "\t");
        System.out.println();
    }
}
```
### Q) Write a method to calculate the sum of all elements in an array
```java
static int sum(int[][] arr) {
    int s = 0;
    for (int i = 0; i < arr.length; i++)
        for (int j = 0; j < arr[i].length; j++)
            s += arr[i][j];
    return s;
}
```

### Q) Write a java method to find the sum of both major amd minor diagonal of a matrix

```java
static void sumDiagonal(int[][] arr) {
    if (arr[0].length != arr.length) {
        System.out.println("The given matrix should be square matrix");
        return;
    }
    int sumMajor = 0, sumMinor = 0, n = arr.length;
    for (int i = 0; i < n; i++) {
        sumMajor += arr[i][i];
        sumMinor += arr[i][n - i - 1];
    }
    System.out.println("Sum of elements of major diagonal = " + sumMajor);
    System.out.println("Sum of elements of minor diagonal = " + sumMinor);
}
```

### Q) Write a method to add two matrix
```java
static void sum(int[][] a, int[][] b) {
        if (a.length == b.length && a[0].length == b[0].length) {
            int[][] c = new int[a.length][b.length];
            for (int i = 0; i < b.length; i++)
                for (int j = 0; j < a[0].length; j++)
                    c[i][j] = a[i][j] + b[i][j];
            System.out.println("Addition of first and second matrix is:");
            display(c);
        } else
            System.out.println("Addition not possible as dimensions are different");
    }
```

### Q) Write a method to subtract two matrix
```java
static void diff(int[][] a, int[][] b) {
    if (a.length == b.length && a[0].length == b[0].length) {
        int[][] c = new int[a.length][b.length];
        for (int i = 0; i < b.length; i++)
            for (int j = 0; j < a[0].length; j++)
                c[i][j] = a[i][j] - b[i][j];
        System.out.println("Difference of first and second matrix is:");
        display(c);
    } else
        System.out.println("Addition not possible as dimensions are different");
}
```

### Q) Write a method to perform matrix multiplication

<a href="#q-write-a-method-to-display-the-elements-of-2d-array">Click here to view ```display(int[][] matrix)```</a>

```java
public static void multiply(int[][] A, int[][] B) {
    if(A[0].length != B.length) {
        System.out.println("Matrix multiplication not possible");
        return;
    }
    int[][] c = new int[A.length][B[0].length];
    for(int i = 0; i < A.length; i++)
        for(int j = 0; j < B[0].length; j++)
            for(int k = 0; k < A[0].length; k++)
                c[i][j] += A[i][K] * B[k][i];
    System.out.println("Product of given two matrices is");
    display(C); // display method is already is defined before being used
}
```

### Q) Write a method to find the transpose of a matrix

<a href="#q-write-a-method-to-display-the-elements-of-2d-array">Click here to view ```display(int[][] matrix)```</a>

```java
public static void transpose(int[][] a) {
    int[][] b = new int[a[0].length][a.length];
    for(int i = 0; i < b.length; i++) 
        for(int j = 0; j < b[0].length; j++)
            b[i][j] = a[j][i];
    System.out.println("Transpose of the given matrix is: ");
    display(b); // display method is already is defined before being used    
}
```
