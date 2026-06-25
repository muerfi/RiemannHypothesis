# Scientific notes

These notes describe the mathematical setting for the repository. They are intentionally cautious: the code in this project supports finite numerical experiments, visualizations, and educational comparisons. It does not prove the Riemann Hypothesis.

## 1. The Riemann zeta function

For complex numbers `s` with real part greater than `1`, the Riemann zeta function is defined by the infinite series

```text
ζ(s) = Σ 1/n^s,  n = 1, 2, 3, ...
```

In the same half-plane, it has an Euler product over primes:

```text
ζ(s) = Π (1 - p^(-s))^(-1), over primes p.
```

The Euler product is one of the basic reasons zeta is tied to prime numbers. It shows that analytic information about `ζ(s)` can encode information about primes, at least in regions where the formula is valid and after substantial additional analysis.

## 2. Analytic continuation, at a high level

The defining series converges only for `Re(s) > 1`. However, the zeta function has an analytic continuation to the complex plane except for a simple pole at `s = 1`.

This project does not implement a symbolic derivation of analytic continuation. Numerical evaluation is delegated to numerical libraries or small helper functions, depending on the task.

## 3. What the Riemann Hypothesis states

The zeta function has zeros at negative even integers:

```text
s = -2, -4, -6, ...
```

These are called the trivial zeros.

The remaining zeros in the critical strip

```text
0 < Re(s) < 1
```

are called non-trivial zeros. The Riemann Hypothesis states:

> Every non-trivial zero of the Riemann zeta function has real part `1/2`.

The vertical line

```text
Re(s) = 1/2
```

is called the critical line.

## 4. What non-trivial zeros are

A non-trivial zero is a complex number `s` in the critical strip for which the analytically continued zeta function satisfies `ζ(s) = 0`.

The zeros are usually listed by increasing positive imaginary part. Numerically, the first few are commonly written in the form

```text
1/2 + i t_n
```

where `t_n` is the ordinate, or imaginary part, of the `n`th zero on the upper half-plane.

When this repository prints values such as `0.5 + 14.1347j`, it is printing finite numerical approximations to such zeros.

## 5. Why numerical verification is useful

Finite numerical checks are useful for several reasons:

- they test whether code is calling numerical libraries correctly;
- they reproduce standard small examples;
- they help detect parsing, precision, and formatting mistakes;
- they provide data for visualization and finite statistical summaries;
- they make abstract definitions more concrete for learners.

A finite verification statement should always include the number of zeros checked, the precision used, and the numerical tolerance.

## 6. Why finite computation cannot settle RH

The Riemann Hypothesis is a universal statement about all non-trivial zeros. There are infinitely many such zeros. Checking the first `N` zeros, even for very large `N`, leaves all zeros beyond that range unchecked.

Finite computation can support statements of the form:

```text
Within this implementation, precision, tolerance, and range, these N computed approximations satisfy the tested condition.
```

It cannot support the statement:

```text
Therefore every non-trivial zero lies on the critical line.
```

Large certified computations may be mathematically and historically important, but they remain finite verification unless combined with a theorem that covers the remaining infinite range.

## 7. Prime-counting and zeta zeros

The prime-counting function `π(x)` counts primes less than or equal to `x`. The prime number theorem describes the leading asymptotic behavior of `π(x)`, and the logarithmic integral `Li(x)` is a classical smooth approximation.

Riemann's work connected primes with zeros of the zeta function through explicit-formula ideas. In broad terms, the main trend in prime counting comes from smooth terms, while oscillatory corrections are connected with zeta zeros.

This repository includes finite comparisons such as `π(100)` versus `Li(100)`. Such comparisons are useful demonstrations, but they do not test RH directly and should not be described as proof-like.

## 8. Zero-spacing statistics

Zero-spacing statistics examine gaps between consecutive zero ordinates, for example

```text
t_{n+1} - t_n.
```

Because the average spacing changes with height, gaps are often normalized before comparison. For small lists, this repository may normalize by the sample mean. More serious studies use height-dependent scaling and much larger datasets.

Finite spacing experiments can illustrate patterns and motivate questions, but small samples are not conclusive statistical evidence.

## 9. Random matrix and quantum-chaos comparisons

Some high-zero statistics resemble eigenvalue statistics from random matrix theory, especially ensembles that also arise in quantum-chaos models. This connection is an important and well-known area of mathematical physics and analytic number theory.

In this repository, these comparisons are analogies and finite statistical experiments. They are not explanations of why RH should hold, and they are not proofs of RH. Scripts under `quantum_connections/` should be read as exploratory demonstrations unless explicitly documented otherwise.

## 10. Machine-learning experiments

Machine-learning scripts, if run, should be treated as exploratory tools for learning workflows and visualizing sequences. A model may fit or extrapolate a finite sequence of zero ordinates, but that does not create mathematical evidence for RH.

ML outputs are sensitive to training data, model architecture, preprocessing, random seeds, and evaluation protocol. They should not be used to make claims about the truth of RH.

## 11. Classification of project material

A useful way to read this repository is:

1. **Known theory**: definitions, standard statements, and classical relationships described in documentation.
2. **Numerical experiment**: finite computations with stated precision, tolerances, and input ranges.
3. **Visualization**: plots designed to build intuition, not to establish theorems.
4. **Analogy**: random-matrix and quantum-chaos comparisons.
5. **Speculation**: possible research directions or heuristic interpretations, clearly labelled as such.
6. **Future work**: engineering and documentation improvements that are not yet implemented.
