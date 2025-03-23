# RiemannHypothesisExplorer

Welcome to **RiemannHypothesisExplorer**, an educational and practical project dedicated to exploring the Riemann Hypothesis, one of the most famous unsolved problems in mathematics. Authored by Murphy, this repository provides tools, visualizations, computations, and theoretical insights into the Riemann Hypothesis and its implications.

## Motivation

The Riemann Hypothesis, proposed by Bernhard Riemann in 1859, conjectures that all non-trivial zeros of the Riemann zeta function lie on the critical line where the real part is \( \frac{1}{2} \). This hypothesis has profound implications for the distribution of prime numbers and has connections to fields like cryptography, quantum physics, and mathematical physics. This project seeks to make the hypothesis accessible through educational resources, computational tools, and innovative approaches, targeting students, educators, and enthusiasts.

## Features

- **Educational Documentation**: A comprehensive PDF (`riemann_hypothesis.pdf`) introducing the Riemann Hypothesis, its mathematical foundations, historical context, numerical evidence, and significance. The document includes detailed sections on:
  - The Riemann zeta function and its properties.
  - Visualizations of the zeta function (magnitude and domain coloring).
  - Computation of non-trivial zeros and their distribution on the critical line.
  - Connection to prime number distribution, including the Prime Number Theorem.
  - Historical milestones and key contributors.
  - Interdisciplinary connections to quantum physics, mathematical physics, and cryptography.
  - Practical applications in technology, such as cryptography and signal processing.
  - Cultural impact and popular media references.
  - Modern approaches, including numerical computations, theoretical methods, quantum computing, and AI analysis.
  - A visually engaging section on the pair correlation of the Riemann zeros, with a plot comparing the zeros’ distribution to the Gaussian Unitary Ensemble (GUE) prediction.

- **Visualizations** :
  - Heatmap of the zeta function’s magnitude in the critical strip (`zeta_magnitude.png`).
  - Domain coloring of the zeta function in the complex plane (`domain_coloring.png`).
  - Plot of the first 10 non-trivial zeros on the critical line (`zeros_critical_line.png`).
  - Comparison of the prime counting function \( \pi(x) \) with its approximation \( \text{Li}(x) \) (`prime_counting.png`).
  - Pair correlation of the Riemann zeros compared to the GUE prediction (`pair_correlation.png`), generated using a Python script.

- **Zero Computations** :
  - Python scripts in the PDF to compute the Riemann zeta function and its non-trivial zeros using the `mpmath` library.

- **Prime Number Simulations** :
  - Detailed section in the PDF on the connection between the Riemann Hypothesis and prime number distribution, with a visualization (`prime_counting.png`).

- **Quantum Connections** :
  - In-depth exploration of the Riemann Hypothesis’s links to quantum physics, including the Hilbert-Pólya conjecture, quantum chaos, spectral theory, and quantum computing.
  - Pair correlation analysis showing the similarity between the Riemann zeros and quantum chaotic systems.

- **Theoretical Approaches** :
  - Discussion of modern theoretical methods, such as the Selberg trace formula, L-functions, and the de Bruijn-Newman constant.

- **AI Analysis** :
  - Overview of AI and machine learning approaches to study the Riemann zeros, including a 2021 study by Yang-Hui He and Kyu-Hwan Lee.

## Repository Structure

- **`docs/`** : Educational documentation and LaTeX source files for the Riemann Hypothesis guide.
  - [riemann_hypothesis.pdf](docs/riemann_hypothesis.pdf) : Compiled PDF document covering the Riemann Hypothesis, its mathematical foundations, visualizations, and interdisciplinary connections.
  - [references.bib](docs/references.bib) : Bibliography file containing references cited in the PDF.
  - **`images/`** : Visualization images used in the PDF.
    - [zeta_magnitude.png](docs/images/zeta_magnitude.png) : Heatmap of the Riemann zeta function’s magnitude in the critical strip.
    - [domain_coloring.png](docs/images/domain_coloring.png) : Domain coloring of the zeta function in the complex plane.
    - [zeros_critical_line.png](docs/images/zeros_critical_line.png) : Plot of the first 10 non-trivial zeros on the critical line.
    - [prime_counting.png](docs/images/prime_counting.png) : Comparison of the prime counting function \( \pi(x) \) with its approximation \( \text{Li}(x) \).
    - [pair_correlation.png](docs/images/pair_correlation.png) : Pair correlation of the Riemann zeros compared to the Gaussian Unitary Ensemble (GUE) prediction.
  - **`scripts/`** : Python scripts for generating visualizations used in the PDF.
    - [plot_zeta_magnitude.py](docs/scripts/plot_zeta_magnitude.py) : Script to generate the heatmap of the zeta function’s magnitude.
    - [plot_zeros_critical_line.py](docs/scripts/plot_zeros_critical_line.py) : Script to plot the non-trivial zeros on the critical line.
    - [plot_prime_counting.py](docs/scripts/plot_prime_counting.py) : Script to plot the prime counting function and its approximation.
    - [plot_domain_coloring.py](docs/scripts/plot_domain_coloring.py) : Script to generate the domain coloring plot of the zeta function.
    - [pair_correlation.py](docs/scripts/pair_correlation.py) : Script to compute and plot the pair correlation of the Riemann zeros.

- **`visualizations/`** : Scripts for generating visualizations of the Riemann zeta function and its zeros (Topic 1).
  - [domain_coloring.py](visualizations/domain_coloring.py) : Script to generate the domain coloring plot of the zeta function.
  - [zeros_plot.py](visualizations/zeros_plot.py) : Script to plot the non-trivial zeros on the critical line.
  - [zeta_function_3d.py](visualizations/zeta_function_3d.py) : Script to create a 3D plot of the zeta function.
  - **`dashboard/`** : Interactive dashboard for visualizations.
    - [app.py](visualizations/dashboard/app.py) : Dash application for interactive visualization of the zeta function and its zeros.

- **`compute_zeros/`** : Scripts for computing the non-trivial zeros of the Riemann zeta function (Topic 2).
  - [verify_critical_line.py](compute_zeros/verify_critical_line.py) : Script to verify that computed zeros lie on the critical line.
  - [zeta_zeros.py](compute_zeros/zeta_zeros.py) : Script to compute the non-trivial zeros using the `mpmath` library.
  - **`data/`** : Directory for storing computed and known zero data.
    - [known_zeros.txt](compute_zeros/data/known_zeros.txt) : File containing known non-trivial zeros for comparison.
  - **`results/`** : Directory for storing computed zeros.
    - [zeros_found.txt](compute_zeros/results/zeros_found.txt) : File containing computed zeros.

- **`prime_distribution/`** : Scripts for simulating prime number distributions and their relation to the Riemann Hypothesis (Topic 3).
  - [error_analysis.py](prime_distribution/error_analysis.py) : Script to analyze the error in the prime counting function approximation.
  - [prime_count.py](prime_distribution/prime_count.py) : Script to compute and plot the prime counting function \( \pi(x) \).
  - [riemann_approx.py](prime_distribution/riemann_approx.py) : Script to compute Riemann’s approximation to the prime counting function.
  - **`visualizations/`** : Visualizations of the error in prime counting approximations.
    - [prime_error_plot.py](prime_distribution/visualizations/prime_error_plot.py) : Script to plot the error between exact and approximated \( \pi(x) \).

- **`quantum_connections/`** : Scripts exploring the Riemann Hypothesis’s connections to quantum physics (Topic 4).
  - [quantum_chaos.py](quantum_connections/quantum_chaos.py) : Script to simulate quantum chaotic systems and compare with the Riemann zeros.
  - [zeros_spacing.py](quantum_connections/zeros_spacing.py) : Script to analyze the spacing distribution of the Riemann zeros.
  - **`visualizations/`** : Visualizations of spacing distributions.
    - [spacing_comparison.py](quantum_connections/visualizations/spacing_comparison.py) : Script to compare the spacing distributions of the Riemann zeros and quantum systems.

- **`theoretical_approaches/`** : Scripts for theoretical methods to study the Riemann Hypothesis (Topic 6).
  - [de_bruijn_newman.py](theoretical_approaches/de_bruijn_newman.py) : Script to explore the de Bruijn-Newman constant.
  - [literature_review.md](theoretical_approaches/literature_review.md) : Markdown file summarizing key theoretical approaches.

- **`machine_learning/`** : Scripts for AI analysis of the non-trivial zeros (Topic 7).
  - [data_preparation.py](machine_learning/data_preparation.py) : Script to prepare the zeros data for training.
  - [lstm_model.py](machine_learning/lstm_model.py) : Script to train an LSTM model to predict zeros.
  - **`visualizations/`** : Visualizations of machine learning predictions.
    - [prediction_plot.py](machine_learning/visualizations/prediction_plot.py) : Script to visualize the predictions of the LSTM model.

- [requirements.txt](requirements.txt) : Python dependencies for running the scripts.
- [README.md](README.md) : Project overview, motivation, and instructions.

## Prerequisites

- **LaTeX Distribution**: To compile the PDF (`riemann_hypothesis.tex`), install a LaTeX distribution like TeX Live or MiKTeX.
  - **On Windows**: Install MiKTeX ([https://miktex.org/download](https://miktex.org/download)).
  - **On Linux/Mac**: Install TeX Live (`sudo apt install texlive-full` on Ubuntu).
- **Python**: To run the script for generating `pair_correlation.png`, install Python 3 and the required libraries:
  - Install Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
  - Install required libraries:
    ```bash
    pip install numpy matplotlib mpmath

  ## How to Use This Repository ?
1. **Clone the repository** :
   ```bash
   git clone https://github.com/muerfi/QuantumBB84.git
   cd RiemannHypothesisExplorer
