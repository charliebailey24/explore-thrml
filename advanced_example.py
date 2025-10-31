#!/usr/bin/env python3
"""
Advanced THRML Example: Exploring Components
This script demonstrates exploring the THRML library components.
"""

import thrml


def main():
    print("=" * 60)
    print("THRML Advanced Example: Exploring Components")
    print("=" * 60)
    
    print("\n1. Creating different types of nodes")
    
    # Create spin nodes (binary variables, typically -1/+1)
    num_spins = 5
    spin_nodes = [thrml.SpinNode() for _ in range(num_spins)]
    print(f"   Created {num_spins} SpinNodes")
    for i, node in enumerate(spin_nodes):
        print(f"      Node {i}: {node}")
    
    # Create categorical nodes (discrete variables)
    num_categorical = 3
    categorical_nodes = [thrml.CategoricalNode() for _ in range(num_categorical)]
    print(f"\n   Created {num_categorical} CategoricalNodes")
    for i, node in enumerate(categorical_nodes):
        print(f"      Node {i}: {node}")
    
    print("\n2. Understanding the THRML architecture")
    print("   Key concepts:")
    print("   - Nodes: Represent random variables")
    print("   - Factors: Define interactions between nodes")
    print("   - Samplers: Generate samples from distributions")
    print("   - Observers: Track state and statistics")
    print("   - Blocks: Group nodes for efficient sampling")
    
    print("\n3. Available node types:")
    print("   - SpinNode: Binary spin variables (-1/+1)")
    print("   - CategoricalNode: Discrete categorical variables")
    
    print("\n4. Available sampling components:")
    components = [
        ("BlockSamplingProgram", "Programs for block-based Gibbs sampling"),
        ("FactorSamplingProgram", "Programs for factor-based sampling"),
        ("SamplingSchedule", "Schedules for iterative sampling"),
        ("BlockGibbsSpec", "Specifications for block Gibbs sampling"),
    ]
    for name, desc in components:
        print(f"   - {name}: {desc}")
    
    print("\n5. Observer types for tracking:")
    observers = [
        ("StateObserver", "Tracks the state of the system"),
        ("MomentAccumulatorObserver", "Accumulates statistical moments"),
    ]
    for name, desc in observers:
        print(f"   - {name}: {desc}")
    
    print("\n" + "=" * 60)
    print("Example completed!")
    print("\nNext steps to explore:")
    print("  1. Check the documentation for detailed API reference")
    print("  2. Look at example models in the docs")
    print("  3. Use the Jupyter notebook for interactive exploration")
    print("\nDocumentation: https://docs.thrml.ai/en/latest/")
    print("=" * 60)


if __name__ == "__main__":
    main()


