#!/usr/bin/env python3
"""
Basic THRML Example
This script demonstrates basic usage of the THRML library from Extropics.

THRML is a library for thermodynamic computing and probabilistic graphical models.
"""

import thrml

def main():
    print("=" * 60)
    print("THRML Basic Example")
    print("=" * 60)
    
    # Example 1: Basic THRML setup
    print("\n1. Checking THRML version and basic setup")
    print(f"THRML module loaded successfully!")
    
    # Example 2: Explore available components
    print("\n2. Available THRML components:")
    components = [x for x in dir(thrml) if not x.startswith('_')]
    
    print("\nKey classes and types:")
    classes = [c for c in components if c[0].isupper() and 'Abstract' not in c]
    for cls in sorted(classes)[:10]:  # Show first 10
        print(f"  - {cls}")
    
    print("\nKey functions:")
    functions = [f for f in components if f[0].islower() and not f.startswith('_')]
    for func in sorted(functions)[:10]:  # Show first 10
        print(f"  - {func}")
    
    # Example 3: Demonstrate basic node creation
    print("\n3. Creating basic nodes:")
    
    # Create a spin node (binary -1/+1)
    spin_node = thrml.SpinNode()
    print(f"  - Created SpinNode: {spin_node}")
    
    # Create a categorical node
    categorical_node = thrml.CategoricalNode()
    print(f"  - Created CategoricalNode: {categorical_node}")
    
    print("\n" + "=" * 60)
    print("Example completed!")
    print("\nNext steps:")
    print("  1. Explore the Jupyter notebook for interactive examples")
    print("  2. Check the documentation: https://docs.thrml.ai/en/latest/")
    print("  3. Try building your own probabilistic models!")
    print("=" * 60)

if __name__ == "__main__":
    main()
