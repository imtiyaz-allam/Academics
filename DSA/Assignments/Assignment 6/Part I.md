# PART-I Static Implementation (Array Implementation)
## Problem Statement
A stack is implemented statically by using an array of size MAX to hold stack elements and an integer top storing the position of top of the stack. The stack elements can be integers, characters, strings or user defined  data types.

The operations to be performed on a stack are:
```java
public static int push(int S[], int top) // adding an element x to the stack S
```
```java
public static int pop(int S[], int top) // deletes and returns the top element from the stack S
``` 
```java
public static void display(int S[], int top) // display all the elements of Stack S
```
```java
public static boolean isEmpty(int top) // check if the stack is empty
```
```java
public static boolean isFull(int top) // check if the stack is full when top equals MAX - 1
```
Write a menu driven Java Program using class, methods and array, to construct a Stack and implement the above five operations.

The template for menu driven java program to use  the above Stack and invoke the required methods to  perform different operations is given below.
```java
import java.util.Scanner;
public class StackDemo1 {
    public static int push(int S[], int top) {
        /* Code for push method */
    }

    /* Code for remaining user defined methods*/
    
    public static final int MAX = 10;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int stack[] = new int[MAX];
        int top = -1;
        while(true) {
            System.out.println("***MENU***");
            System.out.println("0: Exit");
            System.out.println("1: Push");
            System.out.println("2: Pop");
            System.out.println("3: Display");
            System.out.println("Enter your choice");
            int choice = sc.nextInt();
            switch(choice) {
            case 0: 
                System.exit(0);
            case 1: 
                top = push(stack,top);
            break;
            /* Code for remaining cases*/
            default:
                System.out.println("Invalid choice");
            }
        }
    }
}
```

## Solution
```java

```

### Output
```

```