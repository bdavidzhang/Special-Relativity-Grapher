# Special Relativity Grapher Documentation

## Overview

The Special Relativity Grapher is an educational Python library designed to visualize the fundamental concepts of Einstein's special theory of relativity. It provides tools to create interactive simulations and animations that demonstrate effects like time dilation, length contraction, and the relativity of simultaneity.

## Key Features

- **Accurate Physics**: Implements proper Lorentz transformations and relativistic mechanics
- **Visual Learning**: Creates animated demonstrations of abstract concepts
- **Interactive Exploration**: Allows viewing the same scenario from different reference frames
- **Educational Focus**: Designed specifically for teaching and learning special relativity

## Core Concepts

### Natural Units
The library uses natural units where the speed of light c = 1. This simplifies calculations and allows velocities to be expressed as simple fractions (e.g., 0.8 means 80% the speed of light).

### Reference Frames
Central to special relativity is the concept that there is no preferred reference frame. The library allows you to:
- Define objects in their rest frames
- Transform between different inertial reference frames  
- Visualize how the same physical situation appears to different observers

### 4-Vectors
Spacetime events and object positions are represented as 4-vectors [t, x, y] where:
- t is the time coordinate
- x, y are spatial coordinates
- All transformations preserve the spacetime interval

### Objects vs Events
- **Objects**: Extended entities with multiple points (rods, trains, people)
- **Events**: Instantaneous occurrences at specific spacetime points (flashes, measurements)

## Physical Effects Demonstrated

### Time Dilation
Moving clocks run slower as observed from a stationary frame. The time dilation factor is γ = 1/√(1-v²/c²).

### Length Contraction  
Objects appear shorter in the direction of motion when observed from a frame in which they are moving. The contraction factor is 1/γ.

### Relativity of Simultaneity
Events that are simultaneous in one reference frame are generally not simultaneous in another moving frame.

### Classic Paradoxes
The library includes implementations of famous thought experiments:
- **Pole-in-Barn Paradox**: Demonstrates how length contraction and simultaneity work together
- **Twin Paradox**: Shows the role of acceleration in breaking symmetry

## Getting Started

See the main README.md for installation instructions and basic usage examples.

For a comprehensive tutorial, work through the `tutorial.ipynb` notebook which covers all major concepts with interactive examples.

## API Reference

Detailed API documentation is available in the docstrings of each module:
- `simulation.py`: Core simulation classes
- `transforms.py`: Relativistic transformation functions  
- `visualization.py`: Animation and plotting functions
- `utils.py`: Helper functions and utilities
