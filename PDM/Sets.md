# Sets
Set is a well-defined collection of distinct objects.
## Subset
When we say "A is a subset of B," it means that every element found in set A is also found in set B. Here's a more detailed explanation:

* **Definition:**
    * A set A is a subset of a set B if and only if every element of A is also an element of B.
* **Notation:**
    * This relationship is often written as A ⊆ B.
* **Key Points:**
    * **Every set is a subset of itself:** So, B ⊆ B is always true.
    * **The empty set is a subset of every set:** The empty set (∅) contains no elements, so the condition "every element of ∅ is in B" is always true.
    * **Proper Subset:** If A is a subset of B, and A is not equal to B, then A is a "proper subset" of B. This is written as A ⊂ B. This means that all elements of A are in B, and B contains at least one element that is not in A.
* **Example:**
    * If A = {1, 2} and B = {1, 2, 3}, then A is a subset of B (A ⊆ B). In this case, A is also a proper subset of B (A ⊂ B) because B has the element 3, which is not in A.
    * If A = {1,2} and B = {1,2} then A is a subset of B (A ⊆ B). but A is not a proper subset of B.
## Proper Subset
To clarify the concept of a "proper subset," here's a breakdown:

* **Core Idea:**
    * A proper subset is a subset that is not equal to the original set. This means it contains some, but not all, of the elements of the larger set.
* **Formal Definition:**
    * If A is a proper subset of B, then:
        * Every element of A is also an element of B.
        * B contains at least one element that is not in A.
* **Notation:**
    * The symbol for a proper subset is ⊂. So, "A is a proper subset of B" is written as A ⊂ B.
* **Key Distinction from a Subset:**
    * Remember that a set can be a subset of itself (A ⊆ A). However, a set cannot be a *proper* subset of itself.
* **Example:**
    * Let B = {1, 2, 3}.
    * Then, A = {1, 2} is a proper subset of B (A ⊂ B).
    * However, C = {1, 2, 3} is a subset of B (C ⊆ B), but it is not a proper subset, because C = B.

In essence, a proper subset is a smaller piece of a larger set, where "smaller" means it lacks at least one element from the original.
## Laws related to sets
### De-Morgan's Law
De Morgan's laws are a pair of transformation rules in logic and set theory. They provide a way to express the negation of a compound statement. Here's a breakdown:

* **1st Law:**
    * The complement of the union of two sets is equal to the intersection of their complements.
    * Symbolically: $\overline{A ∪ B} = \overline A ∩ \overline B$
    * Proof: <br>
    $\lbrace x:x \in \overline{A \cup B}\rbrace$ <br>
    $=\lbrace x:x \notin (A \cup B)\rbrace $<br>
    $=\lbrace x:x \notin A { and } x \notin B\rbrace $ <br>
    $=\lbrace x:x \in \overline{A} { and } x \in \overline{B}\rbrace $<br>
    $=\lbrace x:x \in (\overline{A}  \cap \overline{B})\rbrace $

* **2nd Law:**
    * The complement of the intersection of two sets is equal to the union of their complements.
    * Symbolically: $\overline{A ∩ B} = \overline A ∪ \overline B$
    * Proof: <br>

    $\lbrace x:x \in \overline{A \cap B}\rbrace$ <br>
    $=\lbrace x:x \notin (A \cap B)\rbrace $<br>
    $=\lbrace x:x \notin A { or } x \notin B\rbrace $ <br>
    $=\lbrace x:x \in \overline{A} { or } x \in \overline{B}\rbrace $<br>
    $=\lbrace x:x \in (\overline{A}  \cup \overline{B})\rbrace $

**Essentially, De Morgan's laws:**

* Provide a way to "distribute" negation over conjunctions (AND) and disjunctions (OR).
* Show how to convert between AND and OR by using negation.

These laws are fundamental in:

* Simplifying logical expressions.
* Designing digital circuits.
* Proving mathematical theorems.


### Commutative law:
- __Union__ <br>
$A \cup B = B \cup A$
- __Intersection__<br> 
$A \cap B = B \cap A$

### Associative law
- __Union__ <br>
$(A \cup B) \cup C = A \cup (B \cup C)$ 
- __Intersection__<br>
$(A \cap B) \cap C = A \cap (B \cap C)$ 

### Distributive Law
- Intersection over union
$A \cup (B \cup C) = (A \cap B) \cup (A \cap C)$
- Union over intersection:
$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$

### Law of complement
- $\overline{\overline{A}} = A$<br>
- $A \cup \overline{A} = U$<br>
- $A \cap \overline{A} = \phi$
### Other Laws
1) $A \cup \phi = A$<br>
$A \cap U = A$
2) $A \cup U = U$<br>
$A \cap \phi= \phi$
3) $A \cup A = A$<br>
$A \cup A = A$