# Roadmap

This roadmap lists realistic improvements for the Riemann Zeta Computational Observatory. It is not a promise to prove the Riemann Hypothesis, and it deliberately avoids proof-like claims.

## Near-term documentation and usability

- Keep README, scientific notes, usage instructions, and references synchronized with the actual CLI.
- Add short examples for the main Python APIs in `riemann_lab.zeros`, `riemann_lab.primes`, and `riemann_lab.visualization`.
- Clarify which legacy scripts are maintained, experimental, or retained only for historical continuity.
- Add provenance notes for bundled zero fixtures and generated figures.

## Precision and numerical reliability

- Improve precision management across the package with consistent decimal-precision policies.
- Report precision, tolerance, and algorithm choices in generated output files.
- Add tests for edge cases in input validation, parsing, and formatting.
- Add warnings when requested precision or sample size is outside the range intended for small demonstrations.

## Zero datasets and caching

- Add an optional cache directory for computed zero ordinates.
- Separate generated caches from source-controlled fixtures.
- Document dataset provenance, precision, and generation commands.
- Provide cache invalidation rules when precision or algorithm settings change.

## Zeta-zero computations

- Keep the current `mpmath.zetazero` path for small educational examples.
- Explore Gram point experiments as an educational feature.
- Consider modest Riemann-Siegel style computations only if they can be implemented, tested, and documented responsibly.
- Avoid presenting any finite computation as a proof of RH.

## Prime-counting experiments

- Add reproducible plots comparing `π(x)`, `Li(x)`, and simpler approximations over finite ranges.
- Include error plots with clearly labelled axes and input ranges.
- Keep explicit-formula experiments carefully documented, especially any truncation choices involving zeros.

## Zero-spacing and statistics

- Add richer spacing summaries: histograms, empirical CDFs, simple moments, and nearest-neighbor spacing plots.
- Support height-dependent normalization for larger zero ranges.
- Add comparison utilities for common random-matrix reference curves where dependencies are available.
- Label all random-matrix comparisons as statistical analogies, not explanations or proofs.

## Visualization

- Improve zeta heatmaps and domain-coloring examples.
- Provide reusable plotting functions with explicit output paths.
- Add plot-regeneration commands for figures under `docs/images/`.
- Consider notebook examples that call the package API rather than duplicating logic.

## Benchmarks and reproducibility

- Add benchmark scripts for zero computation, prime sieving, spacing summaries, and plotting data preparation.
- Store benchmark metadata: Python version, dependency versions, machine information when appropriate, command line, precision, and input size.
- Keep generated benchmark output outside source directories by default.

## Web and interactive interfaces

- If the web calculator remains in scope, improve its input validation and documentation.
- Consider a small read-only dashboard for visual examples, with all mathematical caveats visible in the interface.
- Avoid making the web interface the primary source of scientific claims.

## Project organization

- Continue moving reusable code into `riemann_lab/`.
- Keep legacy scripts thin or mark them as archived examples.
- Separate source code, generated data, cached numerical results, notebooks, and publication-style documentation.
- Add contribution guidelines for numerical claims, documentation tone, and reproducibility expectations.

## Out of scope

The following are intentionally out of scope for this project roadmap:

- claiming a proof of RH;
- claiming machine-learning evidence for RH;
- claiming random-matrix analogies explain RH;
- reproducing specialist large-scale certified zero-verification projects without the required algorithms, data provenance, and independent validation.
