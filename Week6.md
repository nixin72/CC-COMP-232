Floor function: $⌊x⌋$
Ceiling Function: $⌈x⌉$

1. 
    1. $⌊x⌋ = n\iff n <= x < n+1$
    2. $⌈x⌉ = n\iff n-1 < x <= n$
    3. $⌊x⌋ = n\iff x-1 < n <= x$
    4. $⌈x⌉ = n\iff x <= n < x+1$
2. $x - 1 < ⌊x⌋ <= x <= ⌈x⌉ < x + 1$
3. 
    1. $⌈-x⌉ = -⌊x⌋;$
    2. $⌊-x⌋ = -⌈x⌉;$
4. 
    1. $⌊x + n⌋ = ⌊x⌋ + n$
    2. $⌈x + n⌉ = ⌈x⌉ + n$

Proving properties of functions 
$⌊2x⌋ = ⌊x⌋ + ⌊x + 1/2⌋;$
Let x = $ϵ + n$ where $n$ is an integer and $0 < ϵ < 1$

Case 1: $ϵ < {1\over{2}}$
- $2x = 2n + 2ϵ$ and $⌊2x⌋ = 2n$, since $0 < 2ϵ < 1$
- $⌊x + 1/2⌋ = n$ since $x + 1/2 = n + (1/2 + ϵ)$ and $0 < 1/2 + ϵ < 1$
- Hence, $⌊2x⌋ = 2n$ and $⌊x⌋ + ⌊x + 1/2⌋ = n+n = 2n$

Case 2: $ϵ > {1\over{}2}$
- $2x = 2n + 2ϵ = (2n+1) + (2e-1)$ and $⌊2x⌋ = 2n+1$ since $0 <= 2ϵ -1 < 1$
- $⌊x + 1/2⌋ = ⌊n + (1/2 + ϵ)⌋ = ⌊x+1 + (ϵ - 1/2)⌋ = n+1$ since $0 <= ϵ -1/2 < 1$
- Hence, $⌊2x⌋ = 2n+1$ and $⌊x⌋ + ⌊x+1/2⌋ = n + (n+1) = 2n +1$

#### Factorial: 
$f: N \to Z^+$, denoted by $f(x) = n!$ is the product of the first $n$ positive integers when $n$ is a non-negative integer. 

$f(n) = 1⋅2⋅⋅⋅(n-1)⋅n, ~~~~~~~~~~~~~~~~~~~~~~ f(0) = 0! = 1;$

---

#### Cardinality of sets 
Denoted by: $|A| \equiv |B|$

A set that is countable that is either finite or has the same cardinality as the set of positive interger, it is called *countable*. 

Let $f(x) = 2x$

Then $f$ is a bijection from $N$ to $E$ since $f$ is both one-to-one and onto. To sow that is is one-to-one, suppose that $f(n) = f(m)$. Then $2n = 2m$, and so $n = m$. To see that it is onto, suppose that t is an even positive interver. When t = 2k for 


Show that the set of integers $\mathbf{Z}$ is countable. 
Solution: Can list in a sequence:
$0,1,-1,2,-2,3,-3$

Or can define a bijection from $\mathbf{N}$ to $\mathbf{Z}$: 
When n is even, $f(n) = n/2$
When n is odd: $f(n) = -(n-1)/2$

#### Strings
Show that the set of finite strings $S$ over a finite alphabet $A$ is countably infinite. 

Assume an alphabetical ordering of symbols in $A$. 

**Solution**: Show that the strings can be listed in a sequence. First list
1. All the strings of length 0 in alphabetical order. 
2. Then all the strings of length 1 in lexicographic order
3. Then all the strings of length 3
4. And so on...

This implies a bijections from $N$ to $S$ and hence it is countably infinite 

Show that the set of all Java programs are countable. 
Let $S$ be the set of strings constructed from the characters which can appear in a Java program. Use the ordering from the previous example. Take each string in turn:
- Feed the string into a Java compiler.
- If the compiler says YES, this is a syntactically correect Java program, we add the program to the list. 
- We move on to the next string. 

In this way we construct an implied bijection from **N** to the set of Java programs. Hence, the set of java programs is countable. 

Uncountable sets: Real numbers
**Example:** Show that the set of real numbers is uncountable. 
**Solution:** The method is called the Cantor diagnalization argument, and is a proof by contradiction.
1. Suppose R is countable. Then the real numbers between 0 and 1 are also countable. 
2. The real numbers between 0 and 1 can be listed in order $r_1, r_2, r_3$
3. Let the decmial representaion of this listing be $r_1 = 0,d_11d_12d_13d_14...$
4. Form a new real number with the decimal expansion r = $r_1r_2r_3r_4...$
   Where $r_1 = 3$ if $d_{ii} \neq 3$ and $r_1 =4$ if $d_{ii} = 3$


