# Arrays
An array is a linear data structure that consists of elements of homogeneous type and stored in memory in the contiguous manner.

if ```arr``` is

| Memory Address | 1000 | 1004 | 1008 | 1012 |
|---|---|---|---|---|
| Value  | 20  | 15 | 13| 17 |
|index| 0 | 1 | 2 | 3 |

``` Java
arr[0] = 20
arr[1] = 15
arr[2] = 13
arr[3] = 17
```
- Accessing length of ```arr```
```Java
arr.length
```

- Accessing the last element of ```arr```
```Java
arr[arr.length - 1]
```
__Q)__ Write a program to input n elements into an array and display all the elements
```Java
import Java.util.Scanner;

public class ArrayElements {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Get the size of array from user
        System.out.print("Enter the number of elements (n): ");
        int n = scanner.nextInt();
        
        // Create array of size n
        int[] arr = new int[n];
        
        // Input elements into array
        for(int i = 0; i < n; i++) {
            System.out.print("Enter element " + (i+1) + ": ");
            arr[i] = scanner.nextInt();
        }
        
        // Display all elements
        System.out.print("\nElements in the array are:");
        for(int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
```
__Q)__ Write a Java program to find the sum of all elements of an array


```Java
import Java.util.Scanner;
public class ArraySum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Get the size of array from user
        System.out.print("Enter the number of elements (n): ");
        int n = scanner.nextInt();
        
        // Create array of size n
        int[] arr = new int[n];
        
        // Input elements into array
        for(int i = 0; i < n; i++) {
            System.out.print("Enter element " + (i+1) + ": ");
            arr[i] = scanner.nextInt();
        }
        
        // Display the array elements and find the sum of all elements
        int sum = 0; 
        System.out.print("\nElements in the array are:");
        for(int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
            sum += arr[i];
        }
        System.out.println("\nSum of all elements: " + sum);
    }
}
```
__Q)__ Write a Java program to find the largest elements in the array
```Java
import Java.util.Scanner;

public class ArraySum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Get the size of array from user
        System.out.print("Enter the number of elements (n): ");
        int n = scanner.nextInt();
        
        // Create array of size n
        int[] arr = new int[n];
        
        // Input elements into array
        for(int i = 0; i < n; i++) {
            System.out.print("Enter element " + (i+1) + ": ");
            arr[i] = scanner.nextInt();
        }
        
        // Display the array elements and find the largest element
        int max = arr[0];
        System.out.print("\nElements in the array are:");
        for(int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
            if(arr[i] > max) 
                max = arr[i]
        }
        System.out.println("\nLargest all elements: " + maax);
    }
}
```

__Q)__ Write a Java program to count the number of even and odd elements in an array
```Java
import Java.util.Scanner;

public class EvenOddCount {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Get the size of array from user
        System.out.print("Enter the number of elements (n): ");
        int n = scanner.nextInt();
        
        // Create array of size n
        int[] arr = new int[n];
        
        // Input elements into array
        for(int i = 0; i < n; i++) {
            System.out.print("Enter element " + (i+1) + ": ");
            arr[i] = scanner.nextInt();
        }
        
        // Display the array elements and Count even and odd elements
        int evenCount = 0;
        int oddCount = 0;
        System.out.print("\nElements in the array are:");
        for(int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
            if(arr[i] % 2 == 0) 
                evenCount++;
            else 
                oddCount++;
        }
        
        // Display counts
        System.out.println("\nNumber of even elements: " + evenCount);
        System.out.println("Number of odd elements: " + oddCount);
    }
}
```

__Q)__ Write a Java program to insert an element at a given position in 1D array
```Java
import Java.util.Scanner;

public class ArrayInsert {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Input number of elements
        System.out.print("Enter the number of elements (n): ");
        int n = sc.nextInt();
        
        // Create array of size n + 1 to accommodate extra element
        int[] arr = new int[n + 1];
        
        // Input array elements
        System.out.print("Enter " + n + " elements: ");
        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        
        // Input element to insert
        System.out.print("Enter the element to insert: ");
        int element = sc.nextInt();
        
        // Input position (1-based index)
        System.out.print("Enter the position (1 to " + (n + 1) + "): ");
        int position = sc.nextInt();
        
        // Convert position to 0-based index
        int index = position - 1;
        
        // Validate position
        if(position < 1 || position > n + 1) {
            System.out.println("Invalid position! Position should be between 1 and " + (n + 1));
        } else {
            // Shift elements to right from insertion point
            for(int i = n; i > index; i--) {
                arr[i] = arr[i - 1];
            }
            
            // Insert element at position
            arr[index] = element;
            
            // Print resulting array
            System.out.println("Array after insertion:");
            for(int i = 0; i <= n; i++) {
                System.out.print(arr[i] + " ");
            }
            System.out.println();
        }
        
        sc.close();
    }
}
```
__Q) Write a Java program to delete an element from the array

```Java
import Java.util.Scanner;

public class ArrayRemove {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Input number of elements
        System.out.print("Enter the number of elements (n): ");
        int n = sc.nextInt();
        
        // Create array of size n
        int[] arr = new int[n];
        
        // Input array elements
        System.out.print("Enter " + n + " elements: ");
        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        
        // Input number to remove
        System.out.print("Enter the number to remove: ");
        int num = sc.nextInt();
        
        // Find index of number
        int index = -1;
        for(int i = 0; i < n; i++) {
            if(arr[i] == num) {
                index = i;
                break;
            }
        }
        
        // If number found, remove it
        if(index == -1) {
            System.out.println("Number " + num + " not found in array");
        } else {
            // Shift elements left from removal point
            for(int i = index; i < n - 1; i++) {
                arr[i] = arr[i + 1];
            }

            arr[n - 1] = 0;
            
            // Print resulting array
            System.out.print("Array after removal:");
            for(int i = 0; i < n - 1; i++) {
                System.out.print(arr[i] + " ");
            }
            System.out.println();
        }
    }
}
```
__Q)__ Write a method to display the elements of array
```Java
public static void display(int[] A) {
    System.out.print("Array Elements are: ");
    for(int i = 0; i < A.length; i++) {
        System.out.print(A[i] + " ");
    }
    System.out.println();
}
```
__Q)__ Write a Java method to reverse an array
```java
public static void reverseArray(int[] arr) {
    int start = 0;              // First index
    int end = arr.length - 1;   // Last index
    
    // Continue swapping until pointers meet in the middle
    while (start < end) {
        // Swap elements at start and end indices
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        
        // Move pointers towards center
        start++;
        end--;
    }
}
```
__Q)__ Write a Java method that returns the smallest element in an array
```Java
public static int min(int[] arr) {
    int min = arr[0];
    for(int i = 0; i < n; i++) {
        if(arr[i] < min) 
            min = arr[i]
    }
    return min;
}
```
__Q)__ Write a Java method to apply Bubble sort

```java
public static void bubbleSort(int[] arr) {
    int n = arr.length;
    // Outer loop for number of passes
    for (int i = 0; i < n - 1; i++) {
        // Inner loop for comparing adjacent elements
        for (int j = 0; j < n - i - 1; j++) {
            // Compare adjacent elements and swap if they are in wrong order
            if (arr[j] > arr[j + 1]) {
                // Swap elements
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
```
__Q)__ Write a Java method to apply Selection sort

```java
public static void insertionSort(int[] arr) {
    int n = arr.length;
    // Start from second element (index 1)
    for (int i = 1; i < n; i++) {
        int key = arr[i]; // Element to be inserted
        int j = i - 1;    // Index of last element in sorted portion
        
        // Move elements that are greater than key
        // to one position ahead of their current position
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key; // Place key in its correct position
    }
}
```
__Q)__ Write a Java method to apply Insertion sort

```java
public static void selectionSort(int[] arr) {
    int n = arr.length;
    // Move boundary of unsorted subarray one by one
    for (int i = 0; i < n - 1; i++) {
        // Find minimum element in unsorted array
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        
        // Swap the found minimum element with first element
        int temp = arr[minIdx];
        arr[minIdx] = arr[i];
        arr[i] = temp;
    }
}
```