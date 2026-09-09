# CNC Machining Parameter Calculator ⚙️

A simple Python-based calculator for calculating important CNC machining parameters such as spindle speed and feed rate.

## 📌 Project Overview

This project helps CNC machining users calculate basic machining parameters quickly and easily.

The calculator uses:

- Cutting Speed
- Tool Diameter
- Number of Teeth
- Feed per Tooth

to calculate:

- Spindle Speed (RPM)
- Feed Rate (mm/min)

## 🧮 Formulas Used

### Spindle Speed

```text
N = (1000 × V) / (π × D)