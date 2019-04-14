### Class 2

- **Tautologies**
    - A proposition which always evaluates to true ($p \vee \neg p$)
- **Contradiction**
    - A proposition which always evaluates to false ($p \land \neg p$)
- **Contingencies**
    - A proposition that is neither a tautology or a contradiction

<table>
    <tr>
        <td>p</td>
        <td>~p</td>
        <td>p V ~p</td>
        <td>p ^ ~p</td>
    </tr>
    <tr>
        <td>T</td>
        <td>F</td>
        <td>T</td>
        <td>F</td>
    </tr>
    <tr>
        <td>F</td>
        <td>T</td>
        <td>T</td>
        <td>F</td>
    </tr>
</table>

- Logical equivalent:
    - Two compound propositions $p$ and $q$ are logically equivalent if $p \leftrightarrow q$ is a tautology
    - Their columns in a truth table agree

<table>
    <tr>
        <th>p</th>
        <th>q</th>
        <th>~p</th>
        <th>~p V q</th>
        <th>p -> q</th>
    </tr>
    <tr>
        <td>T</td>
        <td>T</td>
        <td>F</td>
        <td>T</td>
        <td>T</td>
    </tr>
    <tr>
        <td>T</td>
        <td>F</td>
        <td>F</td>
        <td>F</td>
        <td>F</td>
    </tr>
    <tr>
        <td>F</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>
    <tr>
        <td>F</td>
        <td>F</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>
</table>

### De Morgan's Law
- $\neg(p \land q) \equiv \neg p \vee \neg q$
- $\neg(p \vee q) \equiv \neg p \land \neg q$

<table>
    <tr>
        <th>p</th>
        <th>q</th>
        <th>~p</th>
        <th>~q</th>
        <th>p V q</th>
        <th>~(p V q)</th>
        <th>~p ^ ~q</th>
    </tr>
    <tr>
        <td>T</td>
        <td>T</td>
        <td>F</td>
        <td>F</td>
        <td>T</td>
        <td>F</td>
        <td>F</td>
    </tr>
    <tr>
        <td>T</td>
        <td>F</td>
        <td>F</td>
        <td>T</td>
        <td>T</td>
        <td>F</td>
        <td>F</td>
    </tr>
    <tr>
        <td>F</td>
        <td>T</td>
        <td>T</td>
        <td>F</td>
        <td>T</td>
        <td>F</td>
        <td>F</td>
    </tr>
    <tr>
        <td>F</td>
        <td>F</td>
        <td>T</td>
        <td>T</td>
        <td>F</td>
        <td>T</td>
        <td>T</td>
    </tr>
</table>

Key Logical Equivalencies

- **Identity Laws**: 
    - $p \land T \equiv p$
    - $p \vee F \equiv p$
- **Domination Laws**: 
    - $p \vee T \equiv T$ 
    - $p \land F \equiv F$
- **Idempotent Laws**: 
    - $p \vee p \equiv p$
    - $p \land p \equiv p$ 
- **Double Negation Laws**
    - $\neg(\neg p) \equiv p$
- **Negation Laws**
    - $p \vee \neg p \equiv T$
    - $p \land \neg p \equiv F$
- **Commutative Laws**
    - $p \vee q \equiv q \vee p$
    - $p \land q \equiv q \land p$
- **Associative Laws**
    - $(p \land q)\land r \equiv p \land(q\land r)$ 
    - $(p \vee q)\vee r \equiv p \vee(q\vee r)$ 
- **Distributive Laws**
    - $(p \vee (q \land r)) \equiv (p \vee q) \land (p \vee r)$
    - $(p \land (q \vee r)) \equiv (p \land q) \vee (p \land r)$
- **Absorption Laws**
    - $p \vee(p \land q) \equiv p$
    - $p \land(p \vee q) \equiv p$

**Show that: $\neg(p \land(\neg p \land q)) \equiv \neg p \land \neg q$**
- $\neg(p\land(\neg p\land q))$
- $\neg p\land\neg(\neg p\land q)$
- $\neg p\land\neg(\neg p\land q)$
- $\neg p\land(p\land \neg q)$
- $(\neg p\land p) \vee (\neg p \land \neg q)$
- $F \vee (\neg p \land \neg q)$
- $(\neg p \land \neg q) \neg F$
- $(\neg p \land \neg q)$

**Show that: $(p\land q) \rightarrow (p \vee q)$ is a tautology**
- $(p\land q) \rightarrow (p \vee q)$
- $\neg(p\land q) \vee (p \vee q)$
- $(\neg p\land\neg q) \vee (p \vee q)$
- $(\neg p\vee p) \vee (\neg q \vee q)$
- $T \vee T$
- $T$

---
### Class 3

## Predicate Logic

Predicate Logic uses the following new features:
- Variables: $x, y, z$
- Predicates: $P(x), M(x)$
- Quantifiers: To be covered later

Propositional functions are a generalization of propositions. Propositional functions become propositions when their variables are each replaced by a value from the domain, $U$.
- $P(x)$ is said to be the value of the propositional function $P$ at $x$.
- Ex.
    - $P(x)$ denotes $x > 0$ and the domain be $\{x\in\mathbb{Z}\}$
        - $P(-3) = false$
        - $P(0) = false$
        - $P(3) = true$
    - The $domain$ is denoted by $U$. 

- Let $x + y = z$ be denoted by $R(x,y,z)$ and $U = \{x\in\mathbb{Z}\}$
    - $R(2,-1,5) = false$
    - $R(3,4,7) = frue$
    - $R(x,-1,z) = $ $Not$ $a$ $Proposition$
- Let $x - y = z$ be $Q(x,y,z)$, with $U = \{x\in\mathbb{Z}\}$
    - $Q(2,-1,3) = true$
    - $Q(2,-1,2) = false$
    - $Q(2,-1,z) = Not$ $a$ $Proposition$
  
Expressions with variables are not propositions and therefore do not have truth values. 

Connectives from propositional logic carry over to predicate logic. If $P(x) = x > 0$, find these:
- $P(3) \vee P(-1) = true$
- $P(3) \land P(-1) = false$
- $P(3) \rightarrow P(-1) = false$
- $P(3) \rightarrow\neg P(-1) = true$

We need quantifiers to express the meaning of English words including all and some:
- All men are mortal
- Some cats don't have fur

The symbols for which are the following: 

- $\forall x P(x)$ 
    - Asserts $P(x)$ is true for **every** x in $U$
    - Ex.   
        >$\begin{alignedat}
            \ P(x) = x > 0, U = \{x\in\mathbb{Z}\}
            \\ \forall x P(x) = false
        \end{alignedat}$
- $\exists x P(x)$
    - Asserts $P(x)$ is true for **some** x in $U$
    - Ex. 
        >$\begin{alignedat}
            \ P(x) = x > 0, U = \{x\in\mathbb{Z}\}
            \\ \forall x P(x) = true
        \end{alignedat}$
- $\exists! x P(x)$ is one and only one $x$ in $U$ that will make the predicate true. 

>$\exists x(P(x) \land \forall y(P(y) \rightarrow y = x))$

- The truth value of $\exists x P(x)$ and $\forall x P(x)$ depends on both the propositional function $P(x)$ and on the domain $U$.

- $\forall x$ and $\exists x$ have higher precedence than all logical operators. 
    - $\forall x P(x) \vee Q(x) \equiv (\forall x P(x)) \vee Q(x)$
    - $\forall x(P(x) \vee Q(x))$ is different. 

Introduce the propositional function $Man(x) = $ "x is a man" and $Motral(x) = $ "x is a mortal" and the domain is all people. 
> $\forall x(Man(x) \rightarrow Mortal(x)$ 
> $Man(socrates)$
> $Mortal(socrates)$

### Equivalencies in Predicate Logic
$S \equiv T$ indicates $S$ and $T$ are logically equivalent

Thinking about Quantifiers, Conjunctions and Disjunctions
> $\forall x P(x) \equiv P(1) \land P(2) \land P(3)$ for $\{x\in\mathbb{Z}|0<x<4\}$

> $\exists x P(x) \equiv P(x_1) \vee P(x_2) \vee ... \vee P(x_n)$ for $\{x\in\mathbb{Z}\}$

### Negating Quantified Expressions
- Consider $\forall x J(x)$ where $J(x) =$ "x has taken a course in Java"
    - Negating the original statement gives "It is not the case that every student in the class has taken a course in Java".
    - >$\neg\forall x J(x) \equiv \exists x\neg J(x)$

- Now consider $\exists xJ(x)$
    - "There is a student in this class who has taken a course in Java"
    - "It is not the case that a student in this class has taken a course in Java"
    - >$\neg\exists xJ(x) \equiv \forall x\neg J(x)$

