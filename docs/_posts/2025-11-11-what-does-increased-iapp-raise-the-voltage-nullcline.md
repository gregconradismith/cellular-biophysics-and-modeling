---
title: "Why does increased I_app raise the voltage nullcline?"
kind: "post"
date: "2025-11-11"
slug: "what-does-increased-iapp-raise-the-voltage-nullcline"
permalink: "/posts/what-does-increased-iapp-raise-the-voltage-nullcline/"
render_with_liquid: false
---

In the Morris-Lecar model, increasing Iapp raises the voltage nullcline, because the vertical axis (w) is the gating variable for an outward current (IK). If you are on the voltage nullcline, and keep V fixed, increasing Iapp is balanced by increasing w. This is described carefully on p. 248-249 of the textbook (Chapter 14).

A good exercise is to consider the (V,h) phase plane for post-inhibitory rebound bursting. In this case, increasing Iapp lowers the voltage nullcline, because the vertical axis (h) is the gating variable for an inward current (the low-threshold calcium current, IT).

In both cases, if you are on the voltage nullcline, then

Iapp = g\*s\*(V - E) + Iother

where g is the conductance of the current of interest, s is its gating variable, and E is its reversal potential, and Iother represents any other membrane currents (which will depend on V but not s). Rearrange the above equation as follows,

s = (Iapp - Iother)/(g\*(V-E)),

and calculate the derivative of s as a function of Iapp,

ds/dIapp = 1/(g\*(V-E)).

This equation shows that when Iapp is increased (depolarizing), the voltage nullcline goes "up" (in the direction of increasing s) **provided** V\>E, that is, when the current g\*(V-E) is positive (outward). Of course, if Iapp is decreased (hyperpolarizing), then the nullcline goes down.

If V\<E (inward current), ds/dIapp is negative, meaning that s decreases when Iapp increases. And the reverse: s increases when Iapp decreases.
