---
title: "Lecture 10"
kind: "page"
date: "1970-01-01"
slug: "lecture-10"
permalink: "/pages/lecture-10/"
lecture_rank: 100
lecture_number: 10
unit: 2
topic: "The Morris-Lecar model and phase plane"
---

# The Morris-Lecar model and phase plane

Public resources and restricted materials are identified below. [Access information](../about/#access-to-materials).

## Core Readings

- <strong>The Morris-Lecar Model.</strong> Chapter 14 of <em>Cellular Biophysics and Modeling: A primer on the computational biology of excitable cells.</em>
- McCormick 1998 "Membrane properties and neurotransmitter actions" (pp. 37-75 of "The Synaptic Organization of the Brain," edited by Gordon Shepard). This book chapter is an excellent review of material we have already covered in detail. The material that is new is in the second half (pp. 43-75), the most important of which (at this time) is the description of the 10-15 most important neuronal ionic currents (see pp. 46-57).
- Begin reading Ermentrout & Terman 2010 (pp. 49-63, that is, Sections 3.1 to 3.4). This chapter of their monograph, <em>Mathematical Foundations of Neuroscience,</em> discusses excitability and oscillations exhibited by the Morris-Lecar model, as well as phase planes, linear stability analysis, and several bifurcations that occur in ODE models with two state variables (e.g., the Hopf bifurcation, saddle-node on a limit cycle bifurcation, and saddle homoclinic bifurcation).

## Slides & Notes

- [Lecture slides — restricted PDF](https://github.com/gregconradismith/cellular-biophysics-and-modeling-private/blob/main/docs/wp-content/uploads/2025/10/Lecture10-IntroToMorrisLecarModel.pdf)

- [Supplementary slides: Morris-Lecar — part 1 — restricted PDF](https://github.com/gregconradismith/cellular-biophysics-and-modeling-private/blob/main/docs/wp-content/uploads/2024/10/Lecture12-1_MorrisLecar.pdf)

- [Supplementary slides: Morris-Lecar — part 2 — restricted PDF](https://github.com/gregconradismith/cellular-biophysics-and-modeling-private/blob/main/docs/wp-content/uploads/2024/10/Lecture12-2_MorrisLecar.pdf)

- [Supplementary slides: Morris-Lecar — part 3 — restricted PDF](https://github.com/gregconradismith/cellular-biophysics-and-modeling-private/blob/main/docs/wp-content/uploads/2024/10/Lecture12-3_MorrisLecar.pdf)

## Practice & Solutions

- [Supplementary exercises — restricted PDF](https://github.com/gregconradismith/cellular-biophysics-and-modeling-private/blob/main/docs/wp-content/uploads/2024/10/Lecture12_problemSet.pdf)

## Further Reading & Resources

- The observation that the Morris-Lecar model exhibited all these dynamical phenomena originated in a classic book chapter by Rinzel & Ermentrout 1998 (see <a href="../bibliography/">[Readings]</a>).
- <a href="https://www.compadre.org/osp/document/ServeFile.cfm?ID=12417&DocID=3122&Attachment=1">Explore the Morris-Lecar simulator at Open Source Physics.</a>

### Why does increased I_app raise the voltage nullcline?

In the Morris–Lecar model, increasing applied current raises the voltage nullcline when the vertical variable gates an outward potassium current. At fixed voltage, the extra applied current is balanced by increasing the gating variable.

More generally, suppose a current is g s(V − E), and other currents depend on V but not s. On the voltage nullcline,

<p>I<sub>app</sub> = g s(V − E) + I<sub>other</sub>, &nbsp; s = (I<sub>app</sub> − I<sub>other</sub>) / (g(V − E)).</p>

Thus, for fixed V ≠ E,

<p>∂s / ∂I<sub>app</sub> = 1 / (g(V − E)).</p>

For g > 0, the shift is upward when V > E and downward when V < E. At V = E, this rearrangement cannot determine s. Compare the (V, w) Morris–Lecar phase plane with the (V, h) phase plane for an inward low-threshold calcium current and post-inhibitory rebound.

[Restricted reading copies in the PDF companion](https://github.com/gregconradismith/cellular-biophysics-and-modeling-private/blob/main/docs/_materials/lecture-10.md) — private repository access required.

{% include restricted-resources.html lecture=page.lecture_number %}

{% include practice-links.html %}

## Continue Exploring

[Practice & Solutions](../practice/) · [Models & Games](../games/)
