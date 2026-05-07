# Usage guide

This guide gives practical commands for running the Riemann Zeta Computational Observatory. Commands assume you are in the repository root.

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install the package in editable mode with test dependencies:

```bash
python -m pip install -e .[test]
```

Install optional extras only when needed:

```bash
python -m pip install -e .[visualization]
python -m pip install -e .[web]
python -m pip install -e .[quantum]
python -m pip install -e .[ml]
```

## Running the CLI

The safest form during development is:

```bash
python -m riemann_lab --help
```

After installation, the console script should also be available:

```bash
riemann-lab --help
```

## Computing small sets of zeros

Compute the first five non-trivial zero approximations at 50 decimal digits of working precision:

```bash
python -m riemann_lab zeros --count 5 --precision 50
```

Write zero approximations to a file:

```bash
python -m riemann_lab zeros --count 20 --precision 80 --output artifacts/zeros/first_20.txt
```

The output file includes a reminder that the values are finite numerical approximations, not a proof of RH.

## Verifying finite numerical results

Check that a finite computed list lies on the critical line within a tolerance:

```bash
python -m riemann_lab verify --count 5 --tolerance 1e-10
```

This command reports `PASS` when every checked approximation has real part within the tolerance of `1/2`. A pass is an implementation and finite-data check only. It is not a proof of the Riemann Hypothesis.

You can adjust precision and count:

```bash
python -m riemann_lab verify --count 25 --precision 80 --tolerance 1e-12
```

For very large counts or high precision, runtime may increase substantially.

## Prime-counting examples

Compare the exact prime-counting function `π(x)` with `Li(x)` at a finite cutoff:

```bash
python -m riemann_lab primes --limit 100
```

Expected output includes:

```text
π(100) = 25
Li(100) ≈ 30.127465
```

Larger cutoffs are possible, but the current implementation is intended for small and moderate demonstrations rather than optimized prime-counting research.

## Zero-spacing examples

Compute consecutive spacings between the first ten zero ordinates:

```bash
python -m riemann_lab spacing --count 10
```

The command prints normalized spacings using the finite sample mean. Random-matrix comparisons, when made, are analogies for finite statistics and should not be read as proof-like.

To print fewer normalized spacing values:

```bash
python -m riemann_lab spacing --count 25 --show 5
```

## Generating plots and visualizations

The package contains visualization data-preparation helpers under `riemann_lab.visualization`. The repository also contains legacy plotting scripts under `visualizations/` and `docs/scripts/`.

Install visualization dependencies first:

```bash
python -m pip install -e .[visualization]
```

Example legacy plotting commands may include:

```bash
python docs/scripts/plot_zeros_critical_line.py
python docs/scripts/plot_prime_counting.py
python docs/scripts/plot_zeta_magnitude.py
python docs/scripts/plot_domain_coloring.py
```

These scripts are retained as educational examples. Some older scripts may assume particular output paths or optional dependencies. Prefer new `riemann_lab` APIs for new work.

## Web calculator

If the web extra is installed, the educational Flask calculator can be launched with:

```bash
python web_calculator/app.py
```

Then open `http://127.0.0.1:5000` in a browser. The calculator is for interactive evaluation and visualization, not for proof or certification.

## Running tests

Run the test suite:

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

## Troubleshooting

### `ModuleNotFoundError: No module named 'riemann_lab'`

Install the package from the repository root:

```bash
python -m pip install -e .
```

Or run commands from the repository root with the active virtual environment.

### `mpmath` is missing

Install the package dependencies:

```bash
python -m pip install -e .
```

`mpmath` is required for normal zero computation beyond bundled toy fixtures.

### Optional plotting, web, quantum, or ML dependencies are missing

Install the relevant extra:

```bash
python -m pip install -e .[visualization]
python -m pip install -e .[web]
python -m pip install -e .[quantum]
python -m pip install -e .[ml]
```

### A legacy script writes output in an unexpected location

Some legacy scripts were originally written as standalone examples and may use relative output paths. Prefer running them from the repository root or the directory documented in the script. Future work should route generated output through a dedicated artifacts directory.

### A finite verification passes but you expected a proof statement

That is intentional. Passing finite numerical checks means only that the computed finite sample satisfied the tested numerical condition. It is not a proof of RH.
