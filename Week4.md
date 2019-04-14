### Class 6
- Mathematical Proofs
- Forms of Theorums
- Direct proofs 
- Indirect proofs
    - Proof of the contrapositive
    - Proof by contradiction

*Trivial proof*: If we know q is true then, 
    $p -> q$ is true as well
    "If it is raining then 1=1"

Vacuous Proof: If we know p is false then 
    $P -> q$ is true as well
    "IF I am both rich and poor then 2+2=5"


**Definition**: The int $n$ is even if there exists an int $k$ sich that $n = 2k$, and $n$ is odd if there exists and int $k$, such that $n = 2k +1$. Note that every int is either odd or even and no int is both odd and even. 

*Direct Proof*: Assume that $p$ is true. USe rules of inference, axioms, and logical equivalencies to show that $q$ must also be true. 

**Example**
Give a direct proof of the theorum "If $n$ is an odd in, then $n^2$ is odd."
Assume that n is odd then n = 2k+1 for an int k. Squaring both sides of the equation, we get: 
$n^2$
$=(2k + 1)^2$
$=4k^2 + 4k + 1$
$=2(2k^2 + 2k) +1$
$=2r + 1$

Where $r = 2k^2 +2k$, an integer.

We have prooved that if $n$ is an odd int $n^2$ is an odd int. 


#### Proving conditional statements: $p \rightarrow q$
*Proof by the contraposition*: Assume $\neg q$ and show $\neg p$ is also true. This is sometimes called an *indirect proof* method. If we give a direct proof of $\neg q \rightarrow \neg p$ then we have a proof of p => q.

**Example:** Prove that if $n$ is an integer and $3n+2$ is odd, then $n$ is odd. 
$3n +2$
$3(2k)+2$
$6k+2$
$2(3k +1)$
$2j$ for $j = 3k + 1$

Therefore 3n+2 is even. sinve we have shown ~q ->~p, p -> q must hold as well. If n is an int and 3n+2 is odd


**Example** Prove that for an integer $n$, if $n^2$ is odd, then $n$ is odd. 
**solution**: Use the proof by contraposition. Assume $n$ is even. Therefore, there existd and integer $k$ such that $n = 2k$. Hence:
$n^2 = 4k^2 =2(2k^2)$
and $n^2$ is even. 

We have shown that if $n$ is an even integer, then $n^2$ is even. Therefore, by contraposition, for an integer $n$ if $n^2$ is odd, then $n$ is odd. 


*Proof by contradiction*: 
To prove p, assume $\neg p$ and derive a contradiction such as $p \land \neg p$ Since we have shown that $\neg p \rightarrow F$ is true, it follows that the contrapositive $T \rightarrow p$ also holds. 

**Example:** Pove that if you pick 22 days from the calendar, at least 4 must fall on the same day of the week. 

**Solution:** Assume that no more than 3 of the 22 days fall on the same day of the week. Because there are 7 days of the week, we could have only picked 21 days. This contradicts the assumption that we have picked 22 days. 

**Example:** Prove that there is no largest prime number.
**Solution:** Assume that there is a largest prime number. Call it $p_n$. Hence, we can list all the primes: $2,3,...,p_n$. Form

$r = p_1 * p_2 * ... * p_n +1$

None of the prime numbers on the list divides r. Therefore, by a theorum in Chapter 4, either $r$ is a prime or there is a smaller prime that divides $r$. This contradicts the assumption that there is a largest prime. Therefore, there is no larges prime. 

#### Theorums that atre biconditional statements
To prive ta theorum that is a biconditional statement, te show that p-> q and q->p are bpoth true. 


"Proof" that $1=2$
1. $a=b$
    1. premise
2. $a^2=axb$
    1. Multiply both sides of (1) by $a$
3. $a^2-b^2 = axb-b^2$
    1. Subtract $b^2$ from both sides of (2)
4. $(a-b)(a+b)=b(a-b)$
    1. Algebra on (3)
5. $a+b=b$
    1. Divide both sides by (a-b)
6. $2b=b$
7. $2=1$


#### Looking ahead
If direct methods of proof do not work:
- We may need a clever use of a proof by contrapositive
- Or a proof by contradiction

#### Proof by cases
To prove a conditional statement of the form:
    $(p_1 \vee p_2 \vee ...\vee p_n) \rightarrow q$

Use the tautology
$[(p_1 \vee p_2 \vee ... \vee p_n)\rightarrow q] \leftrightarrow $

**Example:**
Let a@b = max{a,b} = a if a>= b, otherwise a@b = max(a,b) =b. 
Show that for all real numbers, a,b,c
$(a@b)@c = a @ (b @ c)$
(This means the operation @ is associative)

**Proof** Let a,b,c be arbitraty real numbers. Then one of the following 6 cases must hold. 
1. a >= b >= c
2. a >= c >= b
3. b >= a >= c
4. b >= c >= a
5. c >= b >= a
6. c >= a >= b

Case 1: a >= b >= c
(a@b) = a, a @ c = a, b @ c = b
Hence (a @ b) @ c = a = a @ (b @ c)

Therefore the equality holds for the first case. 

A complete proof requires that the equality be shown to hold for all 6 cases. But the proofs of the remaining cases are similar. 

Case 2: a >= c >= b
(a @ c) = a, a @ b = a, c @ b = c
Hence: (a @ c) @ b = a = a @ (c @ b)

Therefore the equality holds for the second case...


#### Without loss of generality
**Exampe:** Show that if x and y are ints and both x*y and x+y are even, then both x and y are even. 

**Proof:** USe a proof by contraposition. Suppose x and y are not both even. Then, one or both are odd. Without loss of generality, assume that x is odd. Then x = 2m+1 for some int m. 

**case 1**: y is even. Then y = 2n for some int n, so x+y = (2m+1)+2n = 2(m + n) + 1 is odd.
**case 2**: y is odd. Then y = 2n+1 for some int n so x*y = (2m+1)(2n+1)=2(2m*n+m+n+1) is odd.

We only cover the case where x is odd because the case where y is odd is similar. The use phrase *without loss of generality* (WLOG) indicates this. 

#### Existence proof
Proof of theorums of the form ExP(x)

Constructive existence proof:
- Find an exlicit value of c, for which P(c) is true. 
- Then ExP(x) is true by the existential generalization (EG). 

**Example:** Show that there is a positive int that can be written as the sum of cubes of positive ints in two different ways. 
**Proof:** 1729 is such a number since 
$1729 = 10^3 + 9^3 = $

#### Counterexamples
Every positive int is the sum of the squares of 3 integers. The integer 7 is a counterexample, so the claim is false. 


#### Uniqueness proof
Some theorums assert the eixstence of a unique element with a particular property E!xP(x). The two parts of a uniqueness proof are: 
- Existence: We show that an element x with the property exists
- Uniqueness: We show that if y!= x, then y does not have the property. 

**Example:** Show that if a and b are real numbers and a != 0, then there is a unique real number r such that ar+b = 0.

Solution: 
- Existace: The real number r = -b/a is a solution of ar+b = because a(-b/a)+b = -b+b=0/
- Uniqueness: SUppose that s is a real number such that as +b = 0. Then ar +b = as +b, where r = -b/a. Subtracting b from both sides and dividing by a shows that r = s. 

#### Proof strategies for proving $p \rightarrow q$

Chose a method:
1. First try a direct method of proof.
2. IF this does not work, try an indirect method. 

#### Proof and disproof: Tilings
**Example 1:** Can we tile the standard checkboard using dominoes? 
**Solution:** yes! One example provides a constructive existence of this.

**Example 2:** Can we tile a checkerboard obtained by removeing **one** of the four corner squares of a standard cheker board? 
**Solution**
8*8 = 64 - 1 = 63
Each piece is 2*1 which means you cannot have an odd number covered. 

---
### Class 7

#### Sets 
- An unordered list of objects. 
- $s = \{a,b,c,d\} \equiv t = \{d,c,b,a\}$
    - $a\in S$
- Listing an object more than once is redundant, each element is considered unique. 
- Elipses may be used to descibe a set without listing all of the memebers when the pattern is clear. $S = \{a,b,c,d,...,z\}$
    - Ex. Set of all vowels in English
        $V = \{a,e,i,o,u\}$
    - Set of all positive integers less than 10
        $O = \{1,3,5,7,9\}$
    - Set of all positive integers less than 100
        $S = \{1,2,3,4,...,99\}$
- Some important sets: 
    - Natural numbers - $\mathbb{N}$
    - Integers - $\mathbb{Z}$
    - Positive Integers - $\mathbb{Z+}$
    - Real numbers: - $\mathbb{R}$
    - Positive real numbers: $\mathbb{R+}$
    - Complex numbers: $\mathbb{C}$
    - Rational numbers: $\mathbb{Q}$


###### Set builder notation
Specify the property or properties that all members must satisfy 
- $S = \{x | x~is~a~positive~integer~less~than~100\}$
- $O = \{x | x~is~an~odd~positive~integer~less~than 10\}$
- $O = \{x\in\mathbb{R+} | x~is~ odd~ and~ x < 10\}$
  
A predicate may also be used 
$S = \{x | P(x)\}$
Example: $S = \{x | Prime(x)\}$

##### Interval notation
$[a,b] = \{x | a<=x<=b\}$
$[a,b) = \{x | a<=x< b\}$
$(a,b] = \{x | a< x<=b\}$

##### Universal Set and Empty Set 
The *universal set* is the set containing everything currently under consideration. 
- Sometimes implicit
- Sometimes explicitely stated
- Contents depends on the context

The empty set is the set with no elements. Symbolized by $\phi$ but $\{\}$ is also used. 

##### Russell's Paradox
Let S be the set of all sets which are not memebers of themselves. A paradox results from trying to answer the question "Is S a member of itself?"

Henry is a barber who shaves all pepople who do not shave themselves. A paradox results from trying to answer the question "Does Henry shave himself?"

##### Some things to rememebr 
Sets can be elements of sets.
$\{\{a,2,3\}, a, \{b,c\}\}$
$\{N,Z,Q,R\}$

The eompty set is different from a set containing the empty set.
$\phi\neq\{\phi\}$

##### Set equality
**Definition** Two sets are equal if and only if they have te same elements. Therefore if A and B are sets, then A and B are equal if and only if $\forall x(x\in A \leftrightarrow x\in B)$

We write $A = B$ if $A$ and $B$ are equal sets. 
{1,3,5} = {3,5,1}
{1,5,5,5,3,3,1} = {1,3,5}

##### Subsets
The set of $A$ is a subset of $B$ iff every element of $A$ is also an element of $B$. 
The notation $A \subseteq B$ is used to indicate that $A$ is a subset of $B$. 

$A \subseteq B$ holds iff $\forall x(x\in A -> x\in B)$ is true. 
1. Because $a\in\phi$ is always false, $\phi\subseteq S$, for every set S.
2. Because $a\in S \rightarrow a\in S~S\subseteq S$, for every set $S$. 

Recall that two sets $A$ and $B$ are equal, denoted by $A=B$ iff 
- $\forall x(x\in A \leftrightarrow x\in B)$
- $\forall x[(x \in A \rightarrow x\in B) \land (x\in B \rightarrow x\in A)]$
    - $A \subseteq B$ and $B \subseteq A$

##### Proper subsets
If $A \subseteq B$, but $A \neq B$, then we say $A$ is a proper subset of $B$, denoted by $A \subset B$. IF $A \subset B$, then $\forall x(x\in A \rightarrow x\in B) \land \exists x(x\in B \land x\notin A)$ is true.

##### Set cardinality
1. $|\phi| = 0$
2. Let S be the letters of the english language. Then $|S| = 26$
3. $|\{1,2,3\}| = 3$
4. $|\{\phi\}| = 1$

##### Power Sets 
- The set of all subsets of a set $A$, denoted $P(A)$ is called the power set of $A$. 
- If $A = \{a,b\}$
    $P(A) = \{\phi, \{a\}, \{b\}, \{a,b\}\}$

If a set has $n$ elements, then the cardinality of the power set if $2^n$. 

#### Tuples
The *ordered n-tuple* $\{a_1, a_2, a_3,...,a_n\}$
Two n-tuples are equal iff their corresponding elements are equal. 
2-tuples are called *ordered pairs*
The ordered pairs $(a,b)$ and $(c,d)$ are equal iff $a=c$ and $b=d$. 

##### Cartesian Product
product of two sets $A$ and $B$ denoted by $A\times B$ is the set of ordered pairs $(a,b)$ where $a\in A$ and $b\in B$
    $A\times B = \Big\{(a,b)|a\in A\land b\in B\Big\}$
**Ex.**
- $A = \{a,b\}, B = \{1,2,3\}$
- $A\times B = \Big\{(a,1),(a,2),(a,3),~(b,1),(b,2),(b,3)\Big\}$

$A_1\times A_2\times...\times A_n=\{(a_1,a_2,...,a_n)|a_i\in A_i~for~i =1,2,...,n\}$


##### Truth sets of Quantifiers

Given a predicate P and a domain D, we define the *truth set* of $P$ to be the set of elements in $D$ for which $P(x)$ is true. The Truth set of $P(x)$ is denoted by: $\{x\in D|P(x)\}$

**Example:** The truth set of $P(x)$ where the domain is the integers and $P(x)$ is "$|x| = 1$" is the set $\{-1,1\}$

##### Set operations
Let A and B be sets. The union of the sets A and B, denoted by A $\cup$ B, is the set: {x|x\in A \vee x\in B}

**Example** What is {1,2,3} U {3,4,5} is {1,2,3,4,5}.

**Intersection** is denoted by $A \cap B$, is $\{x | x\in A \vee x \in B\}$

##### Compliment
If $A$ is a set, then the *complement* of the $A$ (with respect to $U$), denoted by $\bar{A}$ is the set $U-A$
$\bar{A} = \{x|x\in U | x \notin A\}$

(The complement of A is sometimes denoted by A^c)

**Example:** If U is the positive integers less than 100, what is the complement of {x | x>70}?
