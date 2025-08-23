# Home Assignment: Question 3
## Problem Statement
Write a Java program that takes two arrays a and b of length n storing int values, and returns the dot product of a and b. That is, it returns an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1. 

## Solution
```java
import java.util.Scanner;

public class DotProductArrays {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the length of the arrays: ");
        int n = scanner.nextInt();

        int[] a = new int[n];
        int[] b = new int[n];
        int[] c = new int[n]; // Result array

        System.out.println("Enter " + n + " elements for array a:");
        for (int i = 0; i < n; i++) {
            System.out.print("a[" + i + "] = ");
            a[i] = scanner.nextInt();
        }

        System.out.println("Enter " + n + " elements for array b:");
        for (int i = 0; i < n; i++) {
            System.out.print("b[" + i + "] = ");
            b[i] = scanner.nextInt();
        }

        for (int i = 0; i < n; i++) {
            c[i] = a[i] * b[i];
        }

        System.out.println("Resulting array c (dot product):");
        for (int i = 0; i < n; i++) {
            System.out.println("c[" + i + "] = " + c[i]);
        }

        scanner.close();
    }
}

```


### Output
```
Enter the length of the arrays: 4
Enter 4 elements for array a:
a[0] = 1
a[1] = 2
a[2] = 3
a[3] = 4
Enter 4 elements for array b:
b[0] = 5
b[1] = 6
b[2] = 7
b[3] = 8
Resulting array c (dot product):
c[0] = 5
c[1] = 12
c[2] = 21
c[3] = 32
```