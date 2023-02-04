# Multilinear-Polynomial-Extension-MLE
### Compute the Multilinear Polynomial Extension (MLE) of your function based on your inputs

## What is Multilinear Polynomial Extension (MLE) 

The multilinear polynomial extension (MLE) is a low-degree polynomial extension in which each variable has a degree of at most one.
Given a function Z : {0, 1}<sup>m</sup> → F , the multilinear extension of Z(·) is the unique multilinear polynomial $\tilde{Z}$ : F<sup>m</sup> → F . It can be computed as follows:

<img width="499" alt="Screen Shot 2023-02-04 at 5 14 53 PM" src="https://user-images.githubusercontent.com/35253872/216791700-dbcfe241-c2f7-47e2-9900-bc96c1666bb8.png">

## How to Run
``python3 multilinearPolynomial.py``

## Example

Consider function f:
  * f:{0,1}<sup>2</sup> -> F<sub>5</sub> is a function mapping {0,1}<sup>2</sup> to the field F<sub>5</sub> and f<sub>0</sub> = 1, f<sub>1</sub> = 2, f<sub>2</sub> = 1, f<sub>3</sub> = 4:

|   | 0 | 1 | 
| - | - | - |
| 0 | 1 | 2 |
| 1 | 1 | 4 |

For computing the Multilinear Polynomial Extension ( $\tilde{f}$ ) of function f based on x<sub>1</sub> = 2 and x<sub>2</sub> = 3:

Please specify the group order: 
1. 5\
Please enter your inputs, then type "end" when you're done: 
2. 1
3. 2
4. 1
5. 4
6. end\
Your multilinear polynomial extension has 2 inputs.\
Please enter your inputs for your multilinear polynomial extension:
7. 2
8. 3\
Final result: 16\
16 mod 5 =  1

$\tilde{f}$ is the Multilinear Polynomial Extension of function f based on different inputs over F<sub>5</sub>:

|   | 0 | 1 | 2 | 3 | 4 |
| - | - | - | - | - | - |
| 0 | 1 | 2 | 3 | 4 | 0 |
| 1 | 1 | 4 | 2 | 0 | 3 |
| 2 | 1 | 1 | 1 | 1 | 1 |
| 3 | 1 | 3 | 0 | 2 | 4 |
| 4 | 1 | 0 | 4 | 3 | 2 |

## Support
Reach out to me at riasiarman@yahoo.com
