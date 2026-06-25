# Riemann Zeta Computational Observatory

A reproducible computational laboratory for finite numerical experiments around the Riemann zeta function, non-trivial zeros, prime-counting functions, zero-spacing statistics, and related visualizations.

This repository is written for education, experimentation, and careful numerical exploration. It does **not** prove the Riemann Hypothesis, and it should not be read as claiming to provide mathematical evidence beyond the finite computations actually performed.

## What the project does

The current codebase provides:

- an installable Python package, `riemann_lab`, for small computational number theory experiments;
- a command-line interface for computing finite lists of zeta-zero approximations;
- finite checks that computed zeros have real part close to `1/2` within a chosen numerical tolerance;
- prime-counting comparisons between exact `π(x)` and the logarithmic integral `Li(x)` at finite cutoffs;
- zero-spacing calculations for finite lists of zero ordinates;
- plotting and visualization helpers for zeta values, zeros, prime-counting comparisons, and spacing statistics;
- legacy educational scripts for visualizations, a small web calculator, and exploratory random-matrix / quantum-chaos and machine-learning experiments.

## What the project does not claim

This repository does **not** claim to:

- prove the Riemann Hypothesis;
- reduce the Riemann Hypothesis to a finite computation;
- show that finite verification is a proof;
- treat machine-learning predictions as mathematical evidence for RH;
- treat random-matrix or quantum-chaos comparisons as explanations or proofs;
- provide certified large-scale zero verification comparable to specialist numerical zeta-zero computations.

A command such as `riemann_lab verify --count 5` checks five computed approximations. It says nothing about all non-trivial zeros.

## Mathematical motivation

The Riemann zeta function is one of the central objects in analytic number theory. Its zeros are deeply connected with the distribution of prime numbers through explicit formulas and related results. The Riemann Hypothesis predicts a precise location for all non-trivial zeros: their real part should be `1/2`.

Computers are useful here for:

- reproducing small examples;
- checking implementations against known values;
- visualizing complex-valued functions;
- exploring finite zero-spacing statistics;
- comparing exact prime counts with classical smooth approximations;
- developing intuition before reading more advanced analytic number theory.

Computation can illuminate these topics, but finite computation does not settle a universal theorem about infinitely many zeros.

## Quick start

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .[test,visualization]
python -m pytest
```

Run a small zero computation:

```bash
python -m riemann_lab zeros --count 5 --precision 50
```

Example output:

```text
Finite numerical approximations to non-trivial zeros (not a proof of RH):
Zero 1: s = 0.5 + 14.134725141734695j
Zero 2: s = 0.5 + 21.022039638771556j
Zero 3: s = 0.5 + 25.010857580145689j
Zero 4: s = 0.5 + 30.424876125859512j
Zero 5: s = 0.5 + 32.935061587739192j
```

## Installation

### Editable development install

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .[test]
```

### Optional dependency groups

The project keeps heavier dependencies optional:

```bash
python -m pip install -e .[visualization]
python -m pip install -e .[web]
python -m pip install -e .[quantum]
python -m pip install -e .[ml]
```

Use only the extras needed for the part of the repository you plan to run.

## CLI examples

The CLI can be run either as a module or, after installation, through the console script `riemann-lab`.

### Compute zero approximations

```bash
python -m riemann_lab zeros --count 5 --precision 50
```

Write the same type of output to a file:

```bash
python -m riemann_lab zeros --count 20 --precision 80 --output artifacts/zeros/first_20.txt
```

### Verify a finite computed list against the critical line

```bash
python -m riemann_lab verify --count 5 --tolerance 1e-10
```

Example output:

```text
PASS: checked 5 finite zero approximations
Tolerance: 1e-10
Maximum |Re(s)-1/2|: 0.000e+00
Finite numerical verification is not a proof of the Riemann Hypothesis.
```

### Compare `π(x)` and `Li(x)`

```bash
python -m riemann_lab primes --limit 100
```

Example output:

```text
π(100) = 25
Li(100) ≈ 30.127465
Absolute error: 5.127465
Relative error: 0.205099
```

### Compute zero spacings

```bash
python -m riemann_lab spacing --count 10
```

Example output begins:

```text
Computed 9 consecutive spacings from 10 zeros.
Mean spacing: 3.9599008151
First normalized spacings:
  1.7392643954
  1.00730248752
```

The spacing command prints a reminder that random-matrix comparisons are analogies for finite statistics, not proofs.

## Repository structure

```text
.
├── riemann_lab/                 # Installable package and CLI implementation
│   ├── zeta/                    # Zeta evaluation and critical-line helpers
│   ├── zeros/                   # Zero computation, finite verification, spacing
│   ├── primes/                  # Prime counting and smooth approximations
│   ├── statistics/              # Distribution and random-matrix comparison helpers
│   ├── visualization/           # Data preparation for plots and heatmaps
│   └── experiments/             # Small experiment runners
├── tests/                       # Pytest suite for package and CLI behavior
├── docs/                        # Scientific notes, usage guide, roadmap, references, images
├── compute_zeros/               # Legacy zero scripts and small reference fixture
├── prime_distribution/          # Legacy prime-counting scripts
├── quantum_connections/         # Exploratory analogy scripts
├── machine_learning/            # Optional exploratory ML scripts
├── visualizations/              # Standalone visualization scripts and dashboard
└── web_calculator/              # Educational Flask zeta calculator
```

The `riemann_lab/` package is the preferred interface for new work. Some older scripts remain for educational continuity and may be refactored gradually.

## Core concepts, briefly

### Riemann zeta function

For complex `s` with real part greater than `1`, the zeta function is defined by the convergent series

```text
ζ(s) = 1 + 1/2^s + 1/3^s + 1/4^s + ...
```

It also has an Euler product over primes in this half-plane, which is one reason it is connected to prime numbers.

### Analytic continuation

Although the series above only converges for `Re(s) > 1`, the zeta function can be extended, in a precise analytic sense, to almost all complex numbers. The extended function has one pole at `s = 1`. This repository uses numerical libraries for evaluation rather than deriving analytic continuation from first principles.

### Critical strip

The critical strip is the region `0 < Re(s) < 1`. The non-trivial zeros of the analytically continued zeta function lie in this strip.

### Critical line

The critical line is the vertical line `Re(s) = 1/2`. The Riemann Hypothesis states that every non-trivial zero lies on this line.

### Non-trivial zeros

The zeta function has “trivial” zeros at negative even integers. The zeros relevant to RH are the non-trivial zeros in the critical strip.

### Numerical verification

A finite numerical verification checks a bounded list of computed approximations under stated precision and tolerance choices. It is a useful implementation check and educational demonstration. It is not a proof of a statement about infinitely many zeros.

### Prime-counting function

The prime-counting function `π(x)` counts primes less than or equal to `x`. Classical analytic number theory relates the distribution of primes to zeta zeros through explicit formulas and asymptotic results.

### Zero spacing

Zero-spacing statistics study gaps between consecutive imaginary parts of non-trivial zeros. Normalized spacing patterns can be compared with statistical models, but finite comparisons are descriptive and not proofs.

### Random matrix analogy

Some statistics of high zeta zeros resemble statistics from certain random matrix ensembles. In this repository, such comparisons are treated as analogies and finite-data experiments, not explanations of RH.

### Limitations of computation

No finite list of zeros can prove a statement about every zero. Numerical computations also depend on algorithms, precision, rounding, tolerances, input ranges, and implementation details.

## Reproducibility notes

- Use a virtual environment and record the Python version when producing results.
- Prefer `python -m riemann_lab ...` or the installed `riemann-lab` command over legacy scripts.
- Keep generated outputs under `artifacts/` or another clearly named output directory.
- Include command lines, precision, tolerances, and package versions with any reported numerical result.
- Treat images in `docs/images/` as examples unless regenerated from the corresponding scripts in your environment.

## Testing

Run the test suite with:

```bash
python -m pytest
```

Useful smoke checks:

```bash
python -m riemann_lab zeros --count 5 --precision 50
python -m riemann_lab verify --count 5 --tolerance 1e-10
python -m riemann_lab primes --limit 100
python -m riemann_lab spacing --count 10
```

## Limitations

- The CLI currently targets small and moderate demonstrations, not certified high-volume zeta-zero verification.
- `mpmath.zetazero` is convenient for educational computation but is not a replacement for specialist large-scale verification methods.
- Some legacy scripts still have script-oriented assumptions and may require optional dependencies.
- Machine-learning experiments are exploratory tooling only; their outputs are not mathematical evidence for RH.
- Random-matrix and quantum-chaos material is included as analogy and statistical comparison, not as a proof strategy implemented by this repository.

## Roadmap

Planned and possible improvements include:

- clearer precision and error-reporting policies;
- cached zero datasets with documented provenance;
- more reproducible plotting commands;
- zeta heatmaps and domain-coloring examples;
- Gram point experiments;
- modest Riemann-Siegel style computations if they can be implemented and tested responsibly;
- prime-counting comparison plots;
- richer zero-spacing summaries;
- notebook examples;
- benchmark scripts;
- improved separation of generated data from source code.

See [`docs/ROADMAP.md`](docs/ROADMAP.md) for a more detailed project roadmap.

## Further reading and project notes

- [`docs/SCIENTIFIC_NOTES.md`](docs/SCIENTIFIC_NOTES.md) gives a careful mathematical overview.
- [`docs/USAGE.md`](docs/USAGE.md) gives command-oriented usage instructions.
- [`docs/REFERENCES.md`](docs/REFERENCES.md) explains reference handling and background topics.
- [`docs/AUDIT.md`](docs/AUDIT.md) records an earlier repository audit and refactor plan.

## License

This repository is distributed under the terms of the [MIT License](LICENSE).
