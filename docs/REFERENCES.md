# References and background topics

This repository avoids presenting an invented or inflated bibliography. The file `docs/references.bib` is a bibliography seed already present in the repository, but entries should be manually verified before use in formal writing.

The sections below list safe background areas and a small number of standard reference categories relevant to the project.

## How references should be used here

- Do not add a citation unless the source has been checked.
- Do not add DOIs, URLs, publication data, or author lists from memory if unsure.
- Prefer broad background descriptions when exact bibliographic details are not needed.
- Distinguish standard theory from numerical experiment, visualization, analogy, speculation, and future work.
- Do not cite machine-learning or random-matrix material as evidence for the Riemann Hypothesis.

## Repository bibliography seed

The repository currently includes `docs/references.bib`. It contains entries for several commonly discussed topics around the zeta function, prime counting, zero statistics, and expository material.

Before using those entries in a paper, report, or website, manually check:

- exact title;
- author names;
- publication venue;
- year;
- page range;
- URL status;
- whether the entry is a book, article, preprint, webpage, or lecture note.

## Suggested background topics

The following topics are appropriate background for this project:

- Riemann zeta function;
- analytic continuation and functional equation;
- Riemann Hypothesis;
- trivial and non-trivial zeros;
- critical strip and critical line;
- prime number theorem;
- logarithmic integral and prime-counting approximations;
- explicit formulas relating prime-counting functions and zeta zeros;
- numerical computation of zeta zeros;
- Gram points and Riemann-Siegel type methods;
- zero-spacing statistics;
- Montgomery pair correlation;
- random matrix theory analogy;
- quantum-chaos analogy;
- limitations of finite numerical verification;
- reproducibility in scientific Python.

## Standard kinds of sources to consult

For future documentation improvements, useful source categories include:

- introductory analytic number theory textbooks;
- specialized texts on the Riemann zeta function;
- survey articles on RH and zeta-zero computations;
- original or translated historical sources where appropriate;
- numerical computation papers and verified zero tables;
- documentation for numerical libraries used by this repository;
- reproducibility and scientific-computing best-practice guides.

## Notes on analogy and exploratory work

Random-matrix and quantum-chaos sources can motivate finite spacing comparisons, but they should be cited as analogy or statistical context. They should not be used as proof-like support for RH.

Machine-learning sources, if added, should be framed as computational experimentation or pedagogy. Predictive performance on finite zero sequences is not mathematical evidence for RH.
