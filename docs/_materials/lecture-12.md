---
title: "Lecture 12"
kind: "page"
date: "1970-01-01"
slug: "lecture-12"
permalink: "/pages/lecture-12/"
lecture_rank: 120
image: "/wp-content/uploads/2025/10/Lecture12-TheFitzhughNagumoModel-DepolarizingPulse.gif"
image_alt: "FitzHugh-Nagumo response to a depolarizing pulse"
lecture_number: 12
unit: 2
topic: "The Fitzhugh Nagumo Model, Linear Stability Analysis, and the Trace-Determinant Plane"
---

# The Fitzhugh Nagumo Model, Linear Stability Analysis, and the Trace-Determinant Plane

Public resources and restricted materials are identified below. [Access information](../about/#access-to-materials).

## Core Readings

- <strong>Linear Stability Analysis</strong>. Chapter 16 of <em>Cellular Biophysics and Modeling: A primer on the systems biology of excitable cells.</em> <a href="https://doi.org/10.1017/9780511793905">[DOI]</a>
- <span style="color: var(--color-text);"><strong>Type II Excitability And Oscillations</strong>. Chapter 17 of </span><em>Cellular Biophysics and Modeling: A primer on the systems biology of excitable cells.</em> <a href="https://doi.org/10.1017/9780511793905">[DOI]</a>
- Explore this <strong>MIT Mathlet on phase portraits of linear 2d systems of ODEs with Trace-Determinant Plane</strong>. <a href="http://mathlets.org/mathlets/linear-phase-portraits-matrix-entry/">[Mathlet]</a>

------------------------------------------------------------------------

## Slides & Notes

- [Lecture slides — restricted PDF](https://github.com/gregconradismith/cellular-biophysics-and-modeling-private/blob/main/docs/wp-content/uploads/2025/10/Lecture12-TheFitzhughNagumoModel.pdf)

- [Supplementary slides: FitzHugh-Nagumo — restricted PDF](https://github.com/gregconradismith/cellular-biophysics-and-modeling-private/blob/main/docs/wp-content/uploads/2024/10/Lecture14-(FitzhughNagumo).pdf)

## Recordings & Tutorials

- *The trace-determinant diagram *

<iframe width="560" height="315" src="https://www.youtube.com/embed/oEskbXrhkkk" title="The trace-determinant diagram" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Practice & Solutions

- [Supplementary exercises — restricted PDF](https://github.com/gregconradismith/cellular-biophysics-and-modeling-private/blob/main/docs/wp-content/uploads/2024/10/Lecture14-problemSet.pdf)

## Models & Demonstrations

------------------------------------------------------------------------

<figure class="wp-block-image size-full is-resized">
<a href="../../wp-content/uploads/2025/10/Lecture12-TheFitzhughNagumoModel-DepolarizingPulse.gif"><img src="../../wp-content/uploads/2025/10/Lecture12-TheFitzhughNagumoModel-DepolarizingPulse.gif" class="wp-image-863" style="width:720px;height:auto" /></a>
</figure>

------------------------------------------------------------------------

<figure class="wp-block-image size-full">
<a href="../../wp-content/uploads/2025/10/Lecture12-TheFitzhughNagumoModel-HyperpolarizingPulsePostAnodalBreakExcitation.gif"><img src="../../wp-content/uploads/2025/10/Lecture12-TheFitzhughNagumoModel-HyperpolarizingPulsePostAnodalBreakExcitation.gif" class="wp-image-864" /></a>
</figure>

------------------------------------------------------------------------

<figure class="wp-block-image size-full">
<a href="../../wp-content/uploads/2025/10/Lecture12-TheFitzhughNagumoModel-RelaxationOscillations.gif"><img src="../../wp-content/uploads/2025/10/Lecture12-TheFitzhughNagumoModel-RelaxationOscillations.gif" class="wp-image-866" /></a>
</figure>

------------------------------------------------------------------------

## Further Reading & Resources

- <strong>Excitable Systems and the Fitzhugh-Nagumo Equations</strong>. Sections 11.1-11.4 (pp. 227-241) of <em>A Primer on Mathematical Models in Biology</em> by Leah Edelstein-Keshet and Lee Segel.
- <strong>Fitzhugh's classic paper</strong> (1961).

### The sign of beta in the quadratic formula

For a two-dimensional linear system with coefficient matrix A, let β = tr(A) and γ = det(A). The characteristic polynomial is λ² − βλ + γ = 0, so

<p>λ = (β ± √(β² − 4γ)) / 2.</p>

The trace appears with a positive sign in the numerator because its coefficient in the characteristic polynomial is negative. Use this relation when checking a linear-stability calculation.

[Restricted reading copies in the PDF companion](https://github.com/gregconradismith/cellular-biophysics-and-modeling-private/blob/main/docs/_materials/lecture-12.md) — private repository access required.

{% include restricted-resources.html lecture=page.lecture_number %}

{% include practice-links.html %}

## Continue Exploring

[Practice & Solutions](../practice/) · [Models & Games](../games/)
