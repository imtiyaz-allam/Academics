# PART-II Dynamic Implementation (Linked List Implementation) 
A Queue is implemented dynamically by using a Linked list where each node in the linked list has two parts, the data element and the reference to the next element of the queue.  

The class definition of Node is given below. 
```java
class Node {

    int info; 
    Node next; 
} 
```

The Queue elements can be integers, characters, strings or user defined types. There is no restriction on how big the Queue can grow. 
The operations to be performed on a Queue:
```java 
public static Node insert (Node rear, Node front) // adding an element x to the queue Q requires creation of node containing x and putting it next to the rear and rear points to the newly added element.  
```
```java
public static Node delete (Node rear, Node front) // deletes the front node from the queue Q 
```
```java
public static void display (Node rear, Node front) // display all the elements of the queue Q. 
```
Write a menu driven Java Program using class, methods and list, to construct a Queue and implement the above three operations. 
The code template for constructing the above Queue and performing the required operation is given below.
```java 
import java.util.Scanner; 
public class QueueDemo2 { 

    public static Node insert(Node rear, Node front) { 
        /* Code for inser method */
    } 

    /* Write the code for remaining user defined methods*/ 

    public static void main(String[] args) { 
        Node rear, front;
        /* Code for Scanner object declaration and other required code (if any)*/
        while(true) { 
            System.out.println("****MENU****"); 
            System.out.println("0:Exit"); 
            System.out.println("1:Insert"); 
            System.out.println("2:Delete"); 
            System.out.println("3:Display"); 
            System.out.println("Enter your choice"); 
            int choice = sc.nextInt(); 
            switch(choice) { 
            case 0: 
                System.exit(0); 
            case 1: 
                front = insert(rear, front); 
            break;
            case 2: 
                front = delete(rear, front); 
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