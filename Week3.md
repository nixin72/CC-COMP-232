### Class 4
Translation from English to Logic. 

1. Some student in this class has visisted Maxico. 
    Let M(x) denote "x has visited Mexico" and S(x) "x is a student in this class"
    $\exists x(S(x)\land M(x))$
2. Every student in this class has visited Canada or Mexico 
    $\forall x(S(x)->(M(x) \vee VC(x)))$

$F(x) = $ x is a fleegle
$S(x) = $ x is a snurd
$T(x) = $ x is a thingamabob
Translate everything is a fleegle
$\forall xF(x)$
Nothing is a snurd
$\forall x\neg S(x)$ OR $\neg\exists xS(x)$
All fleegles are snurds
$\forall x(F(x) \rightarrow S(x))$
Some fleegles are also thingamabobs
$\exists x(F(x)\land T(x))$
No snurd is a thingamabob
$\neg\exists x(S(x)\land T(x))$
$\forall x(\neg S(x) \vee \neg T(x))$
If any fleegle is a snurd, then it is also a thingamabob
$\forall x((F(x) \land S(x)) \rightarrow T(x))$

1. All lions are firce
2. Some Lions do not drink coffee
3. Some fierce creatures do not drink coffee
    1. $\forall x(P(x) -> Q(x))$
    2. $\exists x(P(x)\land\neg R(x))$
    3. $\exists x(Q(x)\land\neg R(x))$

#### Nested Quantifiers
Often necessary to express the meaning of english sentances as well as important concepts in CS and MAth

Ex. Every real number has an inverse
- $\forall x\exists y(x + y = 0)$
Where the domains of x and y a the real numbers. 

$\forall x\exists y(x + y = 0)$ can be viewed as $\forall xQ(x) $ where Q(x) is $\exists yP(x, y)$ where $P(x,y) = x + y = 0$

1. $P(x) = x + y == y + x$ 
    >$\forall x\forall yP(x,y) \equiv \forall y\forall xP(x,y)$

2. Let $Q(x,y) = x + y = 0$
    >$\forall x\exists yQ(x,y) \ne \exists y\forall xQ(x,y)$


- $P(x,y) = x * y = 0$
    > $\forall x \forall yP(x,y) = false$
$\forall x\exists yP(x,y) = true$
$\exists x\forall yP(x,y) = true$
$\exists x\exists yP(x,y) = true$

- $P(x,y) = x / y = 1$
    > $\forall x \forall yP(x,y) = false$
$\forall x\exists yP(x,y) = false$
$\exists x\forall yP(x,y) = false$
$\exists x\exists yP(x,y) = true$


Translate the statement
$\forall x(C(c) \vee \exists y(C(y) \land F(x,y)))$
$C(x) = $ x has a computer
$F(x) = $ x and y are friends
$U~of~x, y = $ all friends in your school
> Every student in your school has a computer or has a friend who has a computer. 

$\exists x\forall y\forall z((F(x,y)\land F(x,z) \land (y \ne z)) \rightarrow \neg F(y,z))$
> 
>There is a student none of whose friends are also friends with each other. 

---
### Class 5
The Argument
If the premises are $p_1, p_2,..., p_n$ and the conclusion is 1 then 
    $p_1 \land p_2 \land p_n \rightarrow q$

---
$p \rightarrow q$
$p\over{\therefore q}$
$(q\land(p\rightarrow q)) \rightarrow q$
Let $p$ be "It is snowing"
Let $q$ be "I will study discrete math"
- "If it is snowing, then I will study discrete math."
- "It is snowing."
- "Therefore, I will study discrete math"
---
$p \rightarrow q$
$\neg q\over{\therefore\neg p}$
$(\neg q \land(p \rightarrow q))\rightarrow\neg q$
Let $p$ be "It is snowing"
Let $q$ be "I will study discrete math"
- "If it is snowing, then I will study discrete math."
- "I will not study discrete math"
- "Therefore, it is not snowing"

---

$p \rightarrow q$
$q \rightarrow r\over{p \rightarrow r}$
$((p \rightarrow q) \land (q \rightarrow r)) \rightarrow (p \rightarrow r)$

---
$p\vee q$
$\neg p\over{\therefore q}$
$(\neg p \land(p \vee q)) \rightarrow q$
Let $p$ be "I will study discrete math"
Let $q$ be "I will study English Lit."
- "I will study discrete math or I will study lit. "
- "I will not study discrete math"
- "Therefore, I will study English Lit."

---
$p\over{\therefore p\vee q}$
$p\rightarrow(p\vee q)$
Let $p$ be "I will study discrete math"
Let $q$ be "I will visits Las Vegas"
- "I will study discrete math"
- "Therefore, I will study discrete math or I will visit Las Vegas"

---

$p\land q\over{\therefore p}$
$(p \land q) \rightarrow p$

---

$p$
$q\over{\therefore p\land q}$
$((p)\land(q))\rightarrow(p\land q)$

---

$p\vee q$
$\neg p \vee q\over{\therefore q \vee r)}$
$((\neg p \vee r)\land(p \vee q))\rightarrow(q\vee r)$
Let p be "I will study discrete math"
Let q be "I will study English Literature"
Let r be "I will study databases"
- I will study m or I will study databases"
- I will not study discrete math or I will study English Literature"
- Therefore, I will study databases or I will study English Literature"

---

Using the rules of inference to build valid arguments. 
From the single proposition
$p \land (p\rightarrow q)$
Show that $q$ is a conclusion

1. $p\land (p\rightarrow q)$
    - Premise
2. $p$ 
    - Simplification using (1)
3. $p \rightarrow q$ 
    - Simplification using (1)
4. $q$ 
    - Modus Ponens using (2) and (3)

---

IT is not summy this afternoon and it's colder than yesterday.
We will go swimming only if its sunny.
If we do not go swimming, we will go canoeing 
If we go canoeing, we will be home by sunset. 
$\vee\vee\vee\vee\vee$
We will be home by sunset

1. Chose propositional values.
    - p = "It is sunny this afternoon"
    - q = "It is colder than yesterday
    - r = "We will go swimming"
    - s = "We will go canoeing"
    - t = "We will be home by sunset"
2. Translate to propositional logic:
    - Hypothesis: $\neg p \land q, r\rightarrow p, \neg r \rightarrow s, s\rightarrow t$
3. Construct the arguments
    1. $\neg p \land q$
        - Premise
    2. $\neg p$
        - Simplification using (1)
    3. $r \rightarrow p$
        - Premise
    4. $\neg r$
        - Modus Tollens using (2) and (3)
    5. $\neg r \rightarrow s$
        - Premise
    6. $s$  
        - Modus Ponens using (4) and (5)
    7. $s \rightarrow t$
        - Premise
    8. $t$
        - Modus Ponens using (6) and (7)

---
####Universal Instantiation

$\forall{xP(x)}\over{\therefore{P(x)}}$
Ex. $U$ consists of all dogs, and Fido is a dog. 
- "All dogs are cuddly"
- "Therefore, Fido is cuddly"


$P(c) for~an~arbitrary~c\over{\therefore{\forall{xP(x)}}}$
Used often implicitely in mathematical proofs. 

$\exists{xP(x)}\over{\therefore{P(c) for~some~element~c}}$

$P(x) for~some~element~c\over{\therefore \exists xP(x)}$

Ex. 
"John smith has two legs."
"Every man has two legs", "John smith is a man"
Let M(x) be "x is a man" and L(x) be "x has two legs"
1. $\forall{x(M(x)\rightarrow{L(x)})}$
    - Premise
2. $M(j)\rightarrow L(j)$
    - UI from (1)
3. $M(j)$
    - Premise
4. $L(j)$
    - Modus Ponens using (2) and (3)

Ex. 
"Someone who passed the first exam has not read the book"
"A student in this class has not read the book"
"Everyone in this class passed the first ecam"
- Let C(x) be "x is in this class"
- Let B(x) be "x has read the book"

$\exists x(C(x)\land \neg B(x))$
${\forall x(C(x)\rightarrow P(x))}\over{\therefore\exists x(P(x)\land\neg B(x))}$

1. $\exists x(C(x)\land\neg B(x))$
    - premise
2. $C(a) \land\neg B(a)$
    - EI from (1)
3. $C(a)$
    - Simplification from (2)
4. $\forall x(C(x)\rightarrow P(x))$
    - Premise
5. $C(a)\rightarrow P(a)$
    - Universal Instantiation From (4)
6. $P(a)$
    - MP from (3) and (5)
7. $\neg B(a)$
    - Simplification from (2)
8. $P(a)\land\neg B(a)$
    - Conj from (6) and (7)
9. $\exists x(P(x)\land\neg B(x))$
    -  EG from (8)


$\forall x(Man(x) \rightarrow Mortal(x))$
$Man(Socrates)\over{\therefore Mortal(Socrates)}$

1. $\forall x(Man(x)\rightarrow Mortal(x)$
2. Man(socrates) \rightarrow Mortal(socrates)
3. $Man(Socrates)$
4. $Mortal(Socrates)$


$\forall x(P(x) \rightarrow P(x))$
$P(a), where~a~is~a~particular~element~in~the~domain\over{\therefore Q(x)}$

Why proofs are important:
- Verifications that computer programs are correct
- Establishing that an operating system is secure
- Enabling programs to make inferences in AI
- Showing that system specifications are consistent

A *theorum* is a statement that can be shown to be true using 
    - Definitions
    - Other Theorums
    - Axioms
    - Rules of inference
- A *Lemma* is a "helping theorum" or a result which is needed to prove a theorum.
- A *conjecture* is a statement that is being proposed to be true. Once a proof of a conjecture is found, it becomes a theorum. It may turn out to be false. 

Definition:
- The int. $n$ is even if there exists an int $k$ such that $n = 2k$, and $n$ is odd if there exists an int $k$, such that $n = 2k + 1$. Note that every int is either odd or even.

Assum $p$ is true. 
Give a direct proof of the theorum "If n is an odd int, then n^2 is also odd."
Assuming that $n$ is odd, then $n = 2k+1$ for an int $k$. Squaring both sides of the equation, we get:
$n^2 = (2k+1)^2 = 4k^2 + 4k +1 = 2(2k^2 +2k) + 1 = 2r+1$
where $r = 2k^2 + 2k$, an int.
We have proved that if $n$ is an odd int, then $n^2$ is an odd int. 