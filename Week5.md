#### Union

#### Intersection

#### Complement
**Definition**: If A is a set, then the complement is denoted by $\bar{A}$ is the set 

#### Difference
$A-B = \{x | x \in A \land x \notin B\} = A \cap \bar{B}$

#### The Cardinality of the Union of Two Sets 
$|A \cup B| = |A| + |B| - |A \cap B|$

$Let~U = \{0,1,2,3,4,5,6,7,8,9,10\}, A = \{1,2,3,4,5\}, B = \{4,5,6,7,8\}$
1. $A \cup B = \{1,2,3,4,5,6,7,8\}$
2. $A \cap B = \{4,5\}$
3. $\bar{A} = \{0,6,7,8,9,10\}$
4. $\bar{B} = \{0,1,2,3,9,10\}$
5. $A-B = \{1,2,3\}$
6. $B-A = \{6,7,8\}$


#### Difference

#### Symmetric Difference (optional)
$A \oplus B = (A-B) \cup (B-A)$

#### Set Identities
1. **Identity Laws**
    1. $A \cup \phi = A$ 
    2. $A \cap U = A$
2. **Domination Laws**
    1. $A \cup U = U$
    2. $A \cap \phi = \phi$
3. **Idempotent Laws**
    > $A \cup A = A$
    $A \cap A = A$
4. **Complementation Law**
    > $(\bar{\bar{A}}) = A$
5. **Commutative Laws**
    > $A \cup B = B \cup A$ 
    $A \cap B = B \cap A$
6. **Associative Laws**
    > $A \cup (B \cup C) = (A \cup B) \cup C$
    $A \cap (B \cap C) = (A \cap B) \cap C$
7. **Distributive Laws**
    > $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
    $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
8. **De Morgan's Law**
    > $\overline{A \cup B} = \bar{A} \cap \bar{B}$
    $\overline{A \cap B} = \bar{A} \cup \bar{B}$
9. **Absorption Laws**
    > $A \cup (A \cap B) = A$
    $A \cap (A \cup B) = A$ 
1.  **Complement Laws**
    > $A \cup \bar{A} = U$
    $A \cap \bar{A} = \phi$

**Proof of second De Morgan's Law**
1. $\overline{A \cap B} \subseteq \bar{A} \cup \bar{A}$
    > $x \in \overline{A \cap B}$
    $x \notin A \cap B$
    $\neg((x \in A) \land (x \in B))$
    $\neg(x \in A) \vee \neg(x \in B)$
    $x \notin A \vee x \notin B$
    $x \in \bar{A} \vee x \in \bar{B}$
    $x \in \bar{A} \cup \bar{B}$
2. $\bar{A} \cup \bar{B} \subseteq \overline{A \cap B}$
    > $x \in \bar{A} \cup \bar{B}$
    $(x \in \bar{A}) \vee (x \in \bar{B})$
    $(x \notin A) \vee (x \notin B)$
    $\neg(x \in A) \vee\neg(x \in B)$
    $\neg((X \in A) \land (x \in B)$
    $\neg(x \in A \cap B)$
    $x \in \overline{A \cap B}$

#### Set Builder Notation: Second De Morgan's Law
$\overline{A \cap B} = x \in \overline{A \cap B}$
= {x|~(x E(A n B))}
= {x|~(x E A ^ x E B)}
= {x|~(x E A) v ~(x E B)}
= {x|x !E A v x !EB}
= {x|x E A` v x E B`}
= {x|x E A` u B`}
= {x|A` u B`}

#### Membership Table

| A | B | C | B n C | A u (BnC) | A u B | A u C | (A u B) n (A u C) |
|:-:|:-:|:-:|:-----:|:---------:|:-----:|:-----:|:-----------------:|
| 1 | 1 | 1 | 1     | 1         | 1     | 1     | 1                 |
| 1 | 1 | 0 | 0     | 1         | 1     | 1     | 1
| 1 | 0 | 1 | 0     | 
| 1 | 0 | 0 | 0     |
| 0 | 1 | 1 | 1     |
| 0 | 1 | 0 | 0     |
| 0 | 0 | 1 | 0     |
| 0 | 0 | 0 | 0     |

#### Conversion Between Bin, Oct, and Hex Expansions
$\cup^n_{i=1} A_i = A_1 \cup A_2 \cup ... \cup A_n$
$\cap^n_{i=1} A_i = A_1 \cap A_2 \cap ... \cap A_n$

---

## Functions 
Let $A$ and $B$ be nonempty sets. A *function* $f$ from $A$ to $B$, denoted $f: A\to B$ is an assignment of each element of $A$ to exactly one element of $B$ We write $f(a) = b$ if $b$ is the unique element of $B$ assigned by the function $f$ to the element $a$ of $A$. 

Functions are sometimes called mappings or transformations. 

A function can be:
- An explicit statement of the assignment 
- A formula
- A program...

A function can also be defined as a subset of AxB (a relation). This subset is restricted to be a relaiton where no two elements of t relation have the same first element. 

Specifically, a function f from A to B contains one, and only one ordered pair (a, b) for every element $a\in A$

Formal Definition:
$\forall x\big[x\in A \to \exists y[ y \in B \land (x,y) \in f]\big]$

#### Injections 
A function $f$ is said to be *one-to-one* or injective iff $f(a) = f(b)$ implies that $a = b$ for all $a$ and $b$ in the domain.

#### Surjections 
A function $f$ from $A$ to $B$ is called onto or surjective iff for every element $c \in B$ there is an element $a \in A$ with $f(a) = b$

#### Bijections 
A function $f$ is a one-to-one correspondance or a bijection if it is both 1-1 and onto. (Subjective and injective)