# PART-II Dynamic Implementation (Linked List Implementation)
## Problem Statement
A stack is implemented dynamically by using a Linked list where each node in the linked list has two parts, the data element and the reference to the next element of the stack. The class definition of Node is given below.
```java
class Node {

    int info;
    Node next;
}
```
The stack elements can be integers, characters, strings or user defined data types. There is no restriction on how big the stack can grow.

The operations to be performed on a stack are:
```java
public static Node push(Node top) //  Add an element x to the stack S requires creation of node containing x and putting it in front of the top node pointed by S.
```
```java
public static Node pop(Node top) // Delete the top node from the stack S so that next element becomes the top.
```
```java 
public static void display(Node top) // Display all the elements of Stack S.
```

Write a menu driven Java Program using class, methods and list, to construct a Stack and implement the above three operations.The code template for constructing the above Stack and performing the required operation is given below.
```java
public class StackDemo2 {
    
    public static Node push(Node top) {
        /* Code for push method*/
    }

    /* Write the code for remaining user defined methods*/
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Node top;
        top = null;
        while(true) {
            System.out.println("****MENU****");
            System.out.println("0:Exit");
            System.out.println("1:Push");
            System.out.println("2:Pop");
            System.out.println("3:Display");
            System.out.println("Enter your choice");
            int choice = sc.nextInt();
            switch(choice) {
                case 0:
                    System.exit(0);
                case 1:
                    top = push(top);
                    break;
                /* Code for remaining cases*/
                default:
                System.out.println("Wrong choice");
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