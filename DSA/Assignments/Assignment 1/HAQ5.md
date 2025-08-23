# Home Assignment: Question 5
## Problem Statement
Write a java program that randomly fills in 0s and 1s into a 4-by-4 matrix, prints the matrix, 
and finds the first row and column with the most 1s. 
 
Sample run: 
``` 
0   0   1   1 
0   0   1   1 
1   1   0   1 
1   0   1   0 

The largest row index: 2  
The largest column index: 2 
```

## Solution
```java
public class MatrixOnesMathRandom {

    public static void main(String[] args) {
        int size = 4;
        int[][] matrix = new int[size][size];

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                matrix[i][j] = (int)(Math.random() * 2); 
            }
        }
        
        System.out.println("Matrix:");
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                System.out.print(matrix[i][j] + "   ");
            }
            System.out.println();
        }
        
        int maxRowIndex = 0;
        int maxRowCount = -1;
        for (int i = 0; i < size; i++) {
            int rowCount = 0;
            for (int j = 0; j < size; j++) {
                if (matrix[i][j] == 1) rowCount++;
            }
            if (rowCount > maxRowCount) {
                maxRowCount = rowCount;
                maxRowIndex = i;
            }
        }
        
        int maxColIndex = 0;
        int maxColCount = -1;
        for (int j = 0; j < size; j++) {
            int colCount = 0;
            for (int i = 0; i < size; i++) {
                if (matrix[i][j] == 1) colCount++;
            }
            if (colCount > maxColCount) {
                maxColCount = colCount;
                maxColIndex = j;
            }
        }
        
        System.out.println("\nThe largest row index: " + maxRowIndex);
        System.out.println("The largest column index: " + maxColIndex);
    }
}

```

### Output
```
Matrix:
0   1   0   0   
0   0   1   1   
1   1   0   1   
1   0   1   1   

The largest row index: 2
The largest column index: 3
```