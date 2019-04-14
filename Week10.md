## Proving Inequalities
**Example:** Use mathermatical induction ro prove that $2^n < n!$, for ever int $n \geq 4$

*Solution:* Let $P(n)$ be the proposition that $2^n < n!$
- BASIS STEP: $P(4)$ is true since $2^4 = 16 < 4! = 24$
- Inductive step: Assume $P(k)$ holds, i.e. $2^k < k!$ for an arbitrary $k \geq 4$. To show that $P(k+1)$ holds: 
    - $2^{k+1} = 2 * 2^k$
    - $< 2 * k!$
    - $< (k + 1)k!$
    - $= (K + 1)!$

Therefore, $2^n < n!$ holds, for every integer $n \geq 4$.

## Strong induction

To prove taht p(n) is true for all positive integers n, where P(n) is a poropositional function, complete two steps. 
- Basis step: Verify that the proposition P(1) is true.
- Inductive step: Show that the conditional statement 
    $[P(1) ∧ P(2) ∧ ... ∧ P(k)] \to P(k+1)$
    holds for all positive integers k.

#### Which form of induction should be used? 
We can always use strong induction instead of mathematical induction. But there is no reason to use it if it is simpler to use mathematical induction instead. 

#### Completion of the proof of the Fundamental Theorum of Arithmetic. 
**Example:** Show that if $n$ is an integer greater than 1, then $n$ can be written as the product of primes. 

Solution: Let P(n) be the proposition that $n$ can be written as the product of primes. 
- BASIS step: P(2) is true since 2 itself is prime. 
- Inductive step: The inductive hypothesis is P(j) is true for all integers j with 2 <= j <= k. To show that P(k+1) must be true under this assumption, two cases must be considered
    - If k+1 is prime, then P(k+1) is true. 
    - Otherwise, k+1 is compisite and can bwr written as the product of two positive integers a and b with 2 <= a <= b <= k+1. By the inductive hypothesis a and b can be written as the product of primes, and therefore k+1 can also be written as the product of those primes. 

Hence, it has been shown that every integer greater than 1 can be written as the product of primes. 