#!/usr/bin/env python3
"""
Installation verification script for Special Relativity Grapher.

This script tests that the library is properly installed and can import
all required components.
"""

def test_imports():
    """Test that all library components can be imported."""
    print("Testing imports...")
    
    try:
        # Test main library import
        import special_relativity_grapher
        print("✓ Main library import successful")
        
        # Test core classes and functions
        from special_relativity_grapher import Simulation
        from special_relativity_grapher import getGamma, lorentzTranformPt, addVelocities
        from special_relativity_grapher import Minkowski, RelatavisticAnimation
        from special_relativity_grapher import trueCond
        print("✓ Core components import successful")
        
        # Test individual modules
        from special_relativity_grapher.simulation import Simulation
        from special_relativity_grapher.transforms import getGamma
        from special_relativity_grapher.visualization import Minkowski
        from special_relativity_grapher.utils import trueCond
        print("✓ Individual modules import successful")
        
        print(f"✓ Library version: {special_relativity_grapher.__version__}")
        print(f"✓ Authors: {', '.join(special_relativity_grapher.__authors__)}")
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    
    return True


def test_dependencies():
    """Test that required dependencies are available."""
    print("\nTesting dependencies...")
    
    required_packages = ['numpy', 'matplotlib', 'IPython']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package} available")
        except ImportError:
            print(f"✗ {package} missing")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\nMissing packages: {', '.join(missing_packages)}")
        print("Install with: pip install " + " ".join(missing_packages))
        return False
    
    return True


def test_basic_functionality():
    """Test basic functionality with a simple simulation."""
    print("\nTesting basic functionality...")
    
    try:
        from special_relativity_grapher import Simulation
        from special_relativity_grapher.utils import trueCond
        
        # Create a simple simulation
        sim = Simulation()
        print("✓ Simulation creation successful")
        
        # Add a simple object
        sim.addPt([0, 1, 2], [0, 0], [0, 0])
        print("✓ Object addition successful")
        
        # Run a basic simulation
        times, objects = sim.runSimulation([0, 0], 0.1, 0, 1, trueCond)
        print("✓ Simulation execution successful")
        
        # Verify results
        assert len(times) > 0, "No time steps generated"
        assert len(objects) == len(times), "Mismatch between times and objects"
        print("✓ Simulation results verified")
        
    except Exception as e:
        print(f"✗ Functionality test failed: {e}")
        return False
    
    return True


def main():
    """Run all verification tests."""
    print("Special Relativity Grapher - Installation Verification")
    print("=" * 55)
    
    success = True
    success &= test_imports()
    success &= test_dependencies() 
    success &= test_basic_functionality()
    
    print("\n" + "=" * 55)
    if success:
        print("✓ All tests passed! Installation successful.")
        print("\nNext steps:")
        print("- Try running the examples in the examples/ directory")
        print("- Open tutorial.ipynb for an interactive walkthrough")
        print("- Check the documentation in docs/README.md")
    else:
        print("✗ Some tests failed. Please check the installation.")
        print("\nTroubleshooting:")
        print("- Ensure all dependencies are installed: pip install -r requirements.txt")
        print("- For development: pip install -e .")
        print("- Check that Python path includes the src/ directory")
    
    return success


if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
