# Cartesian Product
In mathematics, the Cartesian product of two sets is a fundamental operation that creates a new set from those two sets. Here's a breakdown:

**Definition:**

* The Cartesian product of two sets A and B, denoted by $A × B$, is the set of all possible ordered pairs $(a, b)$, where $a$ is an element of $A$ and $b$ is an element of $B$.
* In simpler terms, it's a way to combine elements from two sets into pairs.

**Key Concepts:**

* **Ordered Pairs:** The order of elements in a pair matters. $(a, b)$ is different from $(b, a)$ unless $a = b$.
* **Notation:** $A × B$ represents the Cartesian product of sets A and B.
* **Resulting Set:** The result of a Cartesian product is itself a set, where the elements are ordered pairs.

**Example:**

* Let 
$$A = \lbrace 1, 2 \rbrace$$
$$B = \lbrace x, y, z\rbrace $$
* Then, $A × B = \lbrace (1, x), (1, y), (1, z), (2, x), (2, y), (2, z)\rbrace $.

**Important Points:**

* **Cardinality:** If set $A$ has 'm' elements and set $B$ has 'n' elements, then the Cartesian product $A × B$ will have $m × n$ elements.
* **Non-Commutative:** In general, $A × B$ is not equal to $B × A$. The order of the sets matters.
* **Generalization:** The Cartesian product can be extended to more than two sets. For example, $A × B × C$ would be the set of all ordered triples $(a, b, c)$.

# Relation
In mathematics, a "relation" describes a connection or association between elements of sets. Here's a breakdown:

**Core Concept:**

* A relation essentially tells you how elements from one or more sets are related to each other.
* It's a way to express whether a certain property holds between those elements.

**Formal Definition:**

* Formally, a relation between two sets, $A$ and $B$, is a subset of their Cartesian product $(A × B)$. This means a relation is a set of ordered pairs $(a, b)$, where $a$ belongs to $A$ and $b$ belongs to $B$.
* If $(a, b)$ is in the relation, we say that $a$ is related to $b$.

**Key Aspects:**

* **Ordered Pairs:**
    * The order of elements in the pairs matters. $A$ relation from $A$ to $B$ is generally different from a relation from $B$ to $A$.
* **Types of Relations:**
    * Mathematics explores various types of relations, each with specific properties:
        * **Reflexive:** Every element is related to itself.
        * **Symmetric:** If $a$ is related to $b$, then $b$ is related to $a$.
        * **Transitive:** If $a$ is related to $b$ and $b$ is related to $c$, then $a$ is related to $c$.
        * **Equivalence Relations:** Relations that are reflexive, symmetric, and transitive.
        * And many more.
* **Examples:**
    * "Is less than" ($<$) is a relation between numbers.
    * "Is equal to" ($=$) is another relation between numbers.
    * "Is a sibling of" is a relation between people.
    * "Is a subset of" is a relation between sets.
## Types of relations:
### 1. Reflexive relations:
A relation $R$ on $A$ is called reflexive if $(a, a) \in R$ for all $a \in A$ <br>
__Example__:<br> 
> $A = \lbrace 1, 2, 3\rbrace $<br>
> $R = \lbrace (1, 1), (2, 2), (1, 2),(2, 1),(3, 3)\rbrace $
### 2. Symmetric Relation
A relation $R$ is said to be symmetric iff both $(a, b) \in R$ and $(b, a) \in R$ 
__Example__: <br>
> $A = \lbrace 1, 2, 3\rbrace $<br>
> $R = \lbrace (1, 2), (2, 1), (3, 2), (2, 3)\rbrace $
### 3. Antisymmetric Relation
A relation $R$ is said to be antisymmetric if $(a,b) \in R$ and $(b, a) \in R$ together implies $a = b$.<br>
__Example__:
> $A = \lbrace 1, 2, 3\rbrace $<br>
> $R = \lbrace (1, 1), (2, 2), (3, 3), (1, 2)\rbrace $
### 4. Transitive Relation
A relation $R$ on $A$ is transitive if $(a, b) \in R$ and $(b, c) \in R$
then $(a, c) \in R$<br>
__Example__:<br>
> $A = \lbrace 1, 2, 3\rbrace $<br>
> $R = \lbrace (1, 2), (2, 3), (1, 3)\rbrace $

__Q)__ <br>
<img src="img\RelationQ1.png" width=300 height=300><br>
__Ans)__ $\lbrace (A,B), (B, A), (A, D), (D, A), (A, C), (C, A), (B, C), (C, B), (D, C), (C, D)\rbrace $

### 5. Equivalence Relation:
If a relation is symmetric, transitive and reflexive, then it is called equivalence relation.<br>
__Example__:<br>
> $A = \lbrace 1, 2, 3, 4\rbrace $<br>
> $R = \lbrace (1, 1), (2, 2), (4, 4), (1, 3), (2, 1), (3, 3), (1, 2), (3, 1)\rbrace $

### 6. Partial Order Relation:
A relation which is reflexive, antisymmetric and transitive.<br>
__Example__:<br>
> $A = \lbrace 1, 2, 4, 8\rbrace $<br>
> $R = \lbrace (a, b) \in A \times A | a ~ is ~ divisor ~ of ~ b\rbrace $<br>
> $\implies R = \lbrace (1, 1), (1, 2), (1, 4), (1, 8), (2, 2), (2, 4), (2, 8), (4, 4), (4, 8)\rbrace $

### 7. Total-order Relation
A partial order relation is called total-order relation if every pair of elements are comparable.<br>

__Example__:<br>
> $A = \lbrace 1, 2, 3\rbrace $<br>
> $R = \lbrace (1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)\rbrace$