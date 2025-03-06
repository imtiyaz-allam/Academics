# Home Assignment: Question 1
## Problem Statement
Write a Java program that takes as input three integers, a, b, and c, from the Java console and determines if they can be used in a correct arithmetic formula (in the given order), like "a + b = c," "a = b − c," or "a b = c."∗

## Solution
```java
import java.util.Scanner;

public class ArithmeticChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in)
        System.out.print("Enter three integers (a, b, c): ");
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        boolean isValidFormula = false;
        String formula = "";
        if (a + b == c) {
            isValidFormula = true;
            formula = a + " + " + b + " = " + c;
        } else if (a == b - c) {
            isValidFormula = true;
            formula = a + " = " + b + " - " + c;
        } else if (a * b == c) {
            isValidFormula = true;
            formula = a + " * " + b + " = " + c;
        }
        if (isValidFormula) {
            System.out.println("The integers can form the correct arithmetic formula: " + formula);
        } else {
            System.out.println("The integers cannot form a correct arithmetic formula in the given order.");
        }
    }
}
```

# Output
```
Enter three integers (a, b, c): 1 2 3
The integers can form the correct arithmetic formula 1 + 2 = 3
``