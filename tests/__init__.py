"""Test configuration and utilities for special_relativity_grapher tests."""

import pytest
import numpy as np
import sys
import os

# Add the src directory to the path so we can import our package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Test tolerance for floating point comparisons
FLOAT_TOL = 1e-10
