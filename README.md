# CSPC
# Lab A: Radioactive Decay Simulation

## Overview & My Process

In this lab, I worked on simulating radioactive decay using both Python loops and NumPy vectorization. Here is how I went through the tasks step-by-step:

### 1. Fixing the Tests (`test_decay.py`)
At first, `test_matches_law` was failing. I had to debug and fix two main things:
- **Time step issue**: The function in `decay.py` uses `dt = 0.05` seconds, not 1 second steps. I corrected the time array `t` by multiplying the step indices by `dt`.
- **Random seed issue**: The simulation was running 200 times with the default `seed=0`, which produced the exact same result every time instead of averaging different runs. I updated the code to pass `seed=i` for each run so the noise actually averages out.

After these fixes, all three `pytest` tests passed!

### 2. Speed Comparison (`speed.py`)
Next, I created `speed.py` to compare the performance between the pure Python loop (`simulate_loop`) and the NumPy version (`simulate`) for N0 = 200,000 atoms.

**Results:**
- `simulate_loop` (Python loop): ~1.5565 s
- `simulate` (NumPy vectorized): ~0.0002 s
- **Speed-up**: ~7105x faster

### Conclusion
NumPy vectorization is dramatically faster because it processes the entire array of atoms at once using optimized C code, whereas the Python loop iterates over every single surviving atom manually.