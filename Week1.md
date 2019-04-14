### Class 1

## Propositional Logic

- Propositions are statements that can be true or false. 
    - ex. 
        - The moon is made of cheese. 
        - The Capital of Canada is Ottawa
        - 1 + 0 = 1
    - !ex. 
        - Sit down! 
        - What time is it? 
        - x + 1 = 2

Operators:
- Negation: $\neg$
- Conjunction: $\land$
- Disjunction: $\vee$
- Implication: $\rightarrow$
- Biconditional: $\leftrightarrow$

The **negation** of proposition p is denoted by $\neg p$
Truth table: 

<table>
    <tr>
        <td>p</td>
        <td>~P</td>
    </tr>
    <tr>
        <td>T</td>
        <td>F</td>
    </tr>
    <tr>
        <td>F</td>
        <td>T</td>
    </tr>
</table>


The **conjunction** of p and q is $p \land q$
<table>
    <tr>
        <th>p</th>
        <th>q</th>
        <th>p ^ q</th>
    </tr>
    <tr>
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>
    <tr>
        <td>T</td>
        <td>F</td>
        <td>F</td>
    </tr>
    <tr>
        <td>F</td>
        <td>T</td>
        <td>F</td>
    </tr>
    <tr>
        <td>F</td>
        <td>F</td>
        <td>F</td>
    </tr>
<table>

The **Disjunction** of $p$ and $q$  is $p \vee q$
<table>
    <tr>
        <th>p</th>
        <th>q</th>
        <th>p V q</th>
    </tr>
    <tr>
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>
    <tr>
        <td>T</td>
        <td>F</td>
        <td>T</td>
    </tr>
    <tr>
        <td>F</td>
        <td>T</td>
        <td>T</td>
    </tr>
    <tr>
        <td>F</td>
        <td>F</td>
        <td>F</td>
    </tr>
<table>

$p$ = "I am home"
$q$ = "It is raining"
$p\vee q$ = "I am home and it is raining"

**Exclusive or** is $\bigoplus$
<table>
    <tr>
        <th>p</th>
        <th>q</th>
        <th>p O q</th>
    </tr>
    <tr>
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>
    <tr>
        <td>T</td>
        <td>F</td>
        <td>T</td>
    </tr>
    <tr>
        <td>F</td>
        <td>T</td>
        <td>T</td>
    </tr>
    <tr>
        <td>F</td>
        <td>F</td>
        <td>F</td>
    </tr>
<table>

**Implication** of $p$ and $q$ is $p \rightarrow q$ (if $p$, then $q$)
<table>
    <tr>
        <th>p</th>
        <th>q</th>
        <th>p -> q</th>
    </tr>
    <tr>
        <td>T</td>
        <td>T</td>
        <td>F</td>
    </tr>
    <tr>
        <td>T</td>
        <td>F</td>
        <td>T</td>
    </tr>
    <tr>
        <td>F</td>
        <td>T</td>
        <td>T</td>
    </tr>
    <tr>
        <td>F</td>
        <td>F</td>
        <td>F</td>
    </tr>
<table>
If the first proposition is false, then there is no implication, so it's true. 

From $p \rightarrow q$, we can form new rules. 
- $q \rightarrow p$ is the converse of $p \rightarrow q$
- $\neg q \rightarrow \neg p$ is the contrapositive of $p \rightarrow q$
- $\neg p \rightarrow \neg q$ is the inverse of $p \rightarrow q$

Ex. "It is raining is a sufficient condition for my not going to town."
- $p =$ It is raining"
- $q =$ "Going to town"

Converse: $\neg q \rightarrow p$ "If I do not go to town, then it is raining"
Contrapositive: $q \rightarrow \neg p$
Inverse: $\neg p \rightarrow q$

**Biconditional** of $p$ and $q$ is $p \leftrightarrow q$
<table>
    <tr>
        <th>p</th>
        <th>q</th>
        <th>p <-> q</th>
    </tr>
    <tr>
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>
    <tr>
        <td>T</td>
        <td>F</td>
        <td>F</td>
    </tr>
    <tr>
        <td>F</td>
        <td>T</td>
        <td>F</td>
    </tr>
    <tr>
        <td>F</td>
        <td>F</td>
        <td>T</td>
    </tr>
<table>

---
$p \vee q \rightarrow \neg r$
<table>
    <tr>
        <th>p</th>
        <th>q</th>
        <th>r</th>
        <th>~r</th>
        <th>p V q</th>
        <th>p V q -> ~r</th>
    </tr>
    <tr>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>F</td>
        <td>T</td>
        <td>F</td>
    </tr>
    <tr>
        <td>T</td>
        <td>T</td>
        <td>F</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>
    <tr>
        <td>T</td>
        <td>F</td>
        <td>T</td>
        <td>F</td>
        <td>T</td>
        <td>F</td>
    </tr>
    <tr>
        <td>T</td>
        <td>F</td>
        <td>F</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>
    <tr>
        <td>F</td>
        <td>T</td>
        <td>T</td>
        <td>F</td>
        <td>T</td>
        <td>F</td>
    </tr>
    <tr>
        <td>F</td>
        <td>T</td>
        <td>F</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>
    <tr>
        <td>F</td>
        <td>F</td>
        <td>T</td>
        <td>F</td>
        <td>F</td>
        <td>T</td>
    </tr>
    <tr>
        <td>F</td>
        <td>F</td>
        <td>F</td>
        <td>T</td>
        <td>F</td>
        <td>T</td>
    </tr>
</table>

The last two are true because the hypothesis is false, therefore there is no implication. 

<table>
    <tr>
        <th>p</th>
        <th>q</th>
        <th>~p</th>
        <th>~q</th>
        <th>p -> q</th>
        <th>~q -> ~p</th>
    </tr>
    <tr>
        <td>T</td>
        <td>T</td>
        <td>F</td>
        <td>F</td>
        <td>T</td>
        <td>T</td>
    </tr>
    <tr>
        <td>T</td>
        <td>F</td>
        <td>F</td>
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
        <td>T</td>
    </tr>
    <tr>
        <td>F</td>
        <td>F</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>
<table>

The conditional is the same as the contrapositive. 
<table>
    <tr>
        <th>p</th>
        <th>q</th>
        <th>~p</th>
        <th>~q</th>
        <th>p -> q</th>
        <th>~p -> ~q</th>
        <th>q -> p</th>
    </tr>
    <tr>
        <td>T</td>
        <td>T</td>
        <td>F</td>
        <td>F</td>
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>
    <tr>
        <td>T</td>
        <td>F</td>
        <td>F</td>
        <td>T</td>
        <td>F</td>
        <td>T</td>
        <td>T</td>
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
        <td>T</td>
        <td>T</td>
        <td>T</td>
    </tr>
<table>

The converse nor the inverse are not equal to the implication. 

Precedence of logical operators:
1. $\neg$
2. $\land$
3. $\oplus$
4. $\vee$
5. $\rightarrow$
6. $\leftrightarrow$

"The automated reply cannot be sent when the file system is full"
**Solution:**
$p =$ "The automated reply can be sent"
$q =$ "The file system is full"
$q \rightarrow \neg p$