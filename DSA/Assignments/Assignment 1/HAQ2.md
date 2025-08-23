# Home Assignment: Question 2
## Problem Statement
Write a Java program that takes all the lines input to standard input and writes them to standard output in reverse order. That is, each line is output in the correct order, but the ordering of the lines is reversed.

## Solution
```java
import java.util.Scanner;

public class ReverseLines {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the number of lines: ");
        int n = scanner.nextInt();
        scanner.nextLine(); 

        String[] lines = new String[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Enter line " + (i + 1) + ": ");
            lines[i] = scanner.nextLine();
        }

        System.out.println("\nReversed output:");
        for (int i = n - 1; i >= 0; i--) {
            System.out.println(lines[i]);
        }

        scanner.close();
    }
}
```

### Output
```
Enter the number of lines: 3
Enter line 1: Hello world
Enter line 2: Java programming
Enter line 3: Reversing lines

Reversed output:
Reversing lines
Java programming
Hello world
```