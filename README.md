# GNU Radio Projects for Wireless Communications

This repository contains implementations and simulations of wireless communication systems using GNU Radio. The focus is on understanding signal propagation, multipath effects, and power delay profiles in various environments.

## Contents

### 1. Free-Space Path Loss (Lab 2)
- **File**: `lab2 - Reciever.grc`
- **Description**: This simulation demonstrates the free-space path loss (FSPL) model, which predicts the reduction in signal power over distance in a line-of-sight (LOS) environment.
- **Objectives**:
  - Understand the FSPL formula derived from the Friis transmission equation.
  - Analyze signal power at various distances and frequencies.
- **Key Features**:
  - Adjustable frequency and distance.
  - Visualization of signal power in a LOS setup.

### 2. Two-Ray Ground Reflection Model (Lab 2)
- **File**: `lab2 - trasmitter.grc`
- **Description**: Implements the Two-Ray model, considering both the LOS and ground-reflected paths for signal propagation.
- **Objectives**:
  - Observe constructive and destructive interference patterns.
  - Explore the impact of antenna heights and reflection coefficients.
- **Key Features**:
  - Adjustable antenna height and reflection parameters.
  - Analysis of signal interference at different distances and frequencies.

### 3. Multi-Path Propagation Model (part 2)
- **File**: `Part2.grc`
- **Description**: Simulates a multi-path propagation environment with reflections from multiple surfaces, creating a more complex channel model.
- **Objectives**:
  - Study the effects of multipath on signal quality.
  - Analyze the delay spread and power distribution across paths.
- **Key Features**:
  - Multi-path simulation with adjustable parameters.
  - Visualization of delay profiles and signal power.

### 4. Ten-Ray Model Simulation (part 3)
- **File**: `Part3.grc`
- **Description**: Expands the two-ray model to a ten-ray model for urban environments, including reflections from walls and ground.
- **Objectives**:
  - Understand the effects of multiple reflections on signal propagation.
  - Evaluate the power delay profile (PDP) in a dense urban setup.
- **Key Features**:
  - Detailed ray tracing for complex environments.
  - Power and delay calculations for each ray.

### 5. Power Delay Profile Analysis
- **File**: `top_block.py`
- **Description**: Python-based analysis of power delay profiles, considering LOS and multipath components.
- **Objectives**:
  - Visualize the power contributions of each path.
  - Analyze the time delays introduced by multipath.
- **Key Features**:
  - Customizable parameters for detailed analysis.
  - Interactive visualization using PyQt.

## Usage

1. **Requirements**:
   - GNU Radio 3.7 or later.
   - Python 2.7 for running the Python scripts.
   - PyQt4 for GUI elements.

2. **Running the Simulations**:
   - Open the `.grc` files in GNU Radio Companion.
   - Adjust the parameters as needed (e.g., frequency, distance, antenna height).
   - Run the simulation and observe the outputs in the GUI.

3. **Python Scripts**:
   - Use `top_block.py` for advanced analysis.
   - Modify parameters directly in the script for customized results.

## References
- "Wireless Communications" by Andrea Goldsmith.
- Friis Transmission Equation and Free-Space Path Loss Model.
- Two-Ray and Multi-Path Propagation Models.

## Acknowledgments
This project is part of the Wireless Communications Laboratory course at the School of Electrical and Computer Engineering - Ben Gurion University
