Write a menu driven Java Program using class, methods and reference variables, to construct a doubly linked list consisting of the following information in each  node: student regd_no (int), mark secured in a subject (float).

The class definition should be as follows.
```java
class Node {
    protected int regd_no;
    protected float mark;
    protected Node  next;
    protected Node prev;
}
```
The prototype of the create method should be as follows.
```java
public static Node create(Node start, Node end)
```
Define the methods for each of the following operations to be supported by the above linked list are:
1. <b>The insertion operation</b>

    i. At the beginning of the list<br>
    Method Prototype:
    ```java
    public static Node InsBeg(Node start, Node end)
    ```
    ii. At the end of the list<br>
    Method Prototype:
    ```java
    public static Node InsEnd(Node start, Node end)
    ```
    iii. At any position in the list<br>
    Method Prototype: 
    ```java
    public static Node InsAny(Node start, Node end)
    ```


2. <b>The deletion operation</b>

    i. From the beginning of the list<br>
    Method Prototype: 
    ```java
    public static Node DelBeg(Node start, Node end)
    ```
    ii. From the end of the list<br>
    Method Prototype: 
    ```java
    public static Node DelEnd(Node start, Node end)
    ```
    iii. From any position in the list<br>
    Method Prototype: 
    ```java
    public static Node DelAny(Node start, Node end)
    ```
3. <b>Search a node based on student regd_no and update the mark of the student. If the specified node is not present in the list an error message should be displayed.</b><br>
    Method Prototype: 
    ```java 
    public static void search(Node start)
    ```
4.  <b> Displaying all the nodes in the list The prototype of the display function should be as follows.</b>
    ```java
    public static void display(Node start)
    ```

The template for menu driven java program to use  the above list and invoke the required methods 
to  perform different operations is given below.
```java
public class DLinkedList {
    public static Node create(Node start, Node end) {
        /* Code for create method*/
    }

    public static void display(Node start, Node end) {
        /* Code for display method*/
    }

    public static Node insBeg(Node start, Node end) {
        /* Code for insBeg method*/
    }

    /* Code for the remaining user defined methods*/
    
    public static void main(String[] args) {
        /* Code for Scanner object declaration and other required code (if any)*/
        while(true) {
            System.out.println("****MENU*****");
            System.out.println("0: Exit");
            System.out.println("1: Creation");
            System.out.println("2: Display");
            /* Remaining print statements*/
            System.out.println("Enter your choice");
            int choice = sc.nextInt();
            switch(choice) {
                case 0:
                    System.exit(0);
                case 1:
                    end = create(start, end);
                    break;
                case 2:
                    display(start, end);
                    break;
                /* Code for remaining cases */
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