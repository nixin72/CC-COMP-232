Chapter 4: Properties of a relation, Matrix representation

### Closures of Relations
Let $R \subseteq A \times A$
$R$ may or may not be reflexive, but we may need to obtain a relation $Q$ that: 
- Contains $R$
- Is Reflexive - $(a, a) | a \in A$
- Is the smallest relation that contains $R$ and is reflexive

$Q$ is called the **reflexive closure** of $R$.

The **reflexive closure** of $R$ is the smallest relation that contains $R$ and is reflexive. 

Add to $R$ all pairs relating an element to itself. 
Define the diagonal relation on $A$ as $Id = \{(a,a) : a\in A\}$
- The reflexive closure of R is equal to $R \cup Id$
$M_{R\cup Id} = M_R \lor $ NxM identity Matrix

**Example:**
Consider the following relation:
$R_2 = \{(a,b)|a>b\}$
**Is it reflexive?** No, (1,1) would be false
**What is the reflexive closure of $R_2$?** $R_2 = \{(a,b)|a\geq b\}$

#### Symmetric Closure
To obtain the symmetric closure of $R$, for every pair (a,b) \in R, add the pair (b,a).

We can use the inverse of R to obtain the symmetric closure. The SC of R is equal to $R \cup R^{-1}$

The matrix of the SC of R is $M_{R\cup R^{-1}} = M_R \lor (M)$

#### Transitive Closure
The **connectivity relation** R* of R consists of all paris (a,b) such that there is a path from a to b in R. IOW
R* = R u R^2 u R^3 ...


### Equivalence Relations
For a relation to be an equivalence relation, it must be reflexive, symmetric and transitive.

### Parial Ordering 
A relation R on a set S is called partial ordering or partial order, if it is reflexive, antisymmetric, and transitive. A set togther with a partial ordering R is called a partially ordered set, or poset, and is denoted by (S,R). Members of S are called elements of the poset.




