# COMP_361_Assignement
COMP 361/5611 - Elementary Numerical Methods
Assignment 1 - Due Sunday, February 7, 2021
(This assignment does not require any knowledge of the Lecture Notes.)
PProblem 1. (25%) Write a program and use it to compute the Harmonic sum , N
k=1
1
k ; using single precision (i.e., 
oat), for N = 10n, with n = 1; 2; 3;    ; 8; (or
higher). Repeat the computations, but use the double precision. Plot the partial
sums on the graph in terms of N values. Mathematically, i.e., when using exact
arithmetic, this sum is known to diverge as N tends to innity, i.e., the sum can be
made arbitrarily large by taking N suciently large. Explain the observed behavior of
the numerically computed sums. You can the calculus books, e.g. Stewart Calculus,
Cengage 2015 or internet to determine the asymptotic behaviour of the harmonic
series and to help you to interpret the results of computations (always cite your
sources in the assignment report).
Similarly compute the sum
PN
k=1
1
3k ; (in single and double precision) and report
your ndings. Plot the partial sums on the graph in terms of N values.
Mathematically this sum is known to converge as N tends to innity. Use the
internet or calculus books to compute the sum analytically for a xed N and nd its
limit when N ! 1.
Problem 2. (25%) For given x(0), say, x(0) = 1:0, write a program to compute the
sequence x(1), x(2), x(3),   , x(N), up to a suitably large value of N, e.g., N = 20, or
higher where necessary, using the recurrence relation
x(k+1) = f(x(k)); k = 0; 1; 2; 3;    ;
where f(x) = 2x3+5
3x2 . Plot the results on the graph in terms of N values.
Describe in a few words the observed behavior of the sequence. In particular,
does the sequence approach a limiting value? If yes, then do you recognize what
this limiting value is? Does the limiting value depend on x(0) ? The theory for this
problem may be found in the Notes, p. 102-116.
Also compute the sequence with f(x) = cx(1􀀀x), for ve cases, namely, c = 0:95,
c = 1:55, c = 2:0, c = 3:6, and c = 3:98. For each of these cases choose the value of
x(0) to lie between 0 and 1, for example, x(0) = 0:1. Plot the results on the graph in
terms of N values. In each case describe the observed behavior of the sequence. The
theory for this problem may be found in the Notes, p. 117-125.
Problem 3. (50%) Consider the approximate integration of a function f(x) over
1
the interval [0; 1]. Let M be a positive integer, and let h = 1=M, and xk = kh, for
k = 0; 1; 2; 3;    ;M: Thus x0 = 0 and xM = 1. Then one approximate integration
formula is
Z 1
0
f(x)dx  h
h
f(x0+
h
2
)+f(x1+
h
2
)+f(x2+
h
2
)+    +f(xM􀀀2+
h
2
)+f(xM􀀀1+
h
2
)
i
= MP(M):
This method is known as the Midpoint Rule.
Another approximate integration formula is
Z 1
0
f(x)dx 
h
3
h
f(x0)+4f(x1)+2f(x2)+4f(x3)+  +2f(xM􀀀2)+4f(xM􀀀1)+f(xM)
i
= SI(M):
This method, which requires M to be even, is known as the Simpson's Rule.
Implement these two methods in programs, and use each of these to approximately
integrate the function f(x) = sin(x) over the interval [0; 1], using successively the
following values of M: M = 2, 4, 8, 16,    . For each of these values of M print the
error, i.e., the absolute value of the dierence between the approximation and the
known exact value of the integral, which you can obtain analytically. Plot the results
on the graphs. Make sure to represent  to sucient precision in your program!
Furthermore, for each of the two methods, determine from your computations the
smallest value of M for which the error is less than 10􀀀7. How many function evalu-
ations are required in each of these two cases?
Can you describe the observed behavior of the error? In particular, for each of the two
methods, can you say approximately how the error depends on h ? More specically,
it is known that the errors will be approximately proportional to hp, where p is an
integer that depends on the method. Can you tell from the numerical results what
p is for each of the two methods? Also can you explain what happens to the error
when M gets \very large"?
In the last part of this problem you will justify some of the previous results
theoretically. Specically:
(a) Use the internet, the calculus books or the textbook to nd the upper bounds
on the error of the Midpoint Rule, i.e., on j
R 1
0 f(x)dx 􀀀 MP(M)j in terms of
f, its derivatives and M. Use the bound to nd the smallest value of M such
that the error bound becomes less than 10􀀀7.
(b) Use the internet, the calculus books, the textbook or the Notes, p. 268-
286 to nd the error bound for the Simpson Rule, i.e. the upper bounds on
2
j
R 1
0 f(x)dx 􀀀 SI(M)j in terms of f, its derivatives and M. Use the bound to
nd the smallest value of M such that the error bound becomes less than 10􀀀7.
For this assignment you need to submit the report describing your ndings and the
source codes of all the programs you developed.
3
