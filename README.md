# RiemannHypothesisExplorer

A hands-on repository for studying the Riemann Hypothesis through computation, visualization, and small exploratory experiments.

This project is educational. It does **not** claim a proof of the Riemann Hypothesis. The code focuses on reproducible numerical checks (for finite ranges), plots, and short experiments that connect classical number theory ideas with modern computational tooling.

## What this repository currently does

- Computes non-trivial zeros with `mpmath` and verifies they are close to the critical line numerically.
- Builds visualizations of the zeta function and selected zero statistics.
- Compares prime-counting quantities such as `π(x)` and logarithmic-integral-style approximations.
- Includes exploratory modules on random-matrix / quantum-chaos analogies and a small ML workflow for zero-sequence prediction.
- Provides a simple Flask web calculator for evaluating `ζ(s)` at user-supplied complex inputs.

## Scope and caveats

- Numerical agreement for the first `N` zeros is evidence for those samples only.
- Theoretical sections summarize known ideas from the literature; they are not new results.
- ML scripts are exploratory and should not be interpreted as evidence for or against RH.

## Repository layout

```text
.
├── compute_zeros/
│   ├── zeta_zeros.py
│   ├── verify_critical_line.py
│   └── data/known_zeros.txt
├── docs/
│   ├── riemann_hypothesis.pdf
│   ├── references.bib
│   ├── images/
│   └── scripts/
├── machine_learning/
├── prime_distribution/
├── quantum_connections/
├── theoretical_approaches/
├── visualizations/
└── web_calculator/
```

## Quick start

### 1) Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Compute zeros and verify basic consistency

```bash
python compute_zeros/zeta_zeros.py
python compute_zeros/verify_critical_line.py --tolerance 1e-10 --comparison-limit 10
```

### 3) Run selected analysis scripts

```bash
python prime_distribution/prime_count.py
python quantum_connections/zeros_spacing.py
python visualizations/zeros_plot.py
```

### 4) Launch the web calculator

```bash
python web_calculator/app.py
```

Then open `http://127.0.0.1:5000`.

## Notes on generated files

Some scripts create output folders if needed (for example `compute_zeros/results/`).
If you run modules out of order, later scripts may fail because their expected input files are not present yet.

## Suggested workflow for new contributors

1. Start with `compute_zeros/` to generate baseline data.
2. Use `visualizations/` and `docs/scripts/` to reproduce plots.
3. Explore `prime_distribution/` and `quantum_connections/` for comparative experiments.
4. Treat `machine_learning/` as optional exploratory work.

## Contributing

Issues and pull requests are welcome, especially for:

- numerical stability improvements,
- clearer mathematical explanations,
- better reproducibility of plots and script outputs,
- cleanup of path handling and CLI ergonomics.

## License

This repository is distributed under the terms of the [MIT License](LICENSE).
