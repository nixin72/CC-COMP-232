Every positive integer greater than $1$ can be written uniquely as a prime or as the product of two or more primes where the prime factors are written in order of non-decreasing size. 

**Example:**
$100 = 2 ⋅ 2 ⋅ 5 ⋅ 5 = 2^5 ⋅ 5 ^2$
$641 = 641$
$999 = 3 ⋅ 3 ⋅ 3 ⋅ 37 = 3^3 ⋅ 37$
$1024 = 2 ⋅ 2 ⋅ 2 ⋅ 2 ⋅ 2 ⋅ 2 ⋅ 2 ⋅ 2 ⋅ 2 ⋅ 2 = 2^{10}$

The Sieve of Erastosthenes
Can be used to find all primes not exceeding a specified positive integer. Ex. begin with the list of ints betweeen 1 and 100.

1. Delete all the integers orther than 2, divisible by 2. 
2. Delete all integers, other than 3, divisible by 3. 
3. Delete all integers, other than 5, divisible by 5
4. Delete all integers, other than 7, divisible by 7.
5. Since all the remaining integers are not divisible by any of the previous integers, then they must be prime numbers . 

If an integer $n$ is a compositie integer, then it has a prime divisor less than or equal to $sqrt(n)$. To see this, note that if $n = ab$, then $a\leq\sqrt n$ or $a\leq\sqrt n$ 

Trial division, a very inefficient method of determining if a number $n$ is prime, is to try every integer $i \leq \sqrt{n}$ and see if $n$ is divisible by $i$.

