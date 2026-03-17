# kickback_comparison.py

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

def run_analysis(control_state, target_state):
    # Create 2-qubit circuit
    qc = QuantumCircuit(2)
    
    # 1. Initialize Control Qubit
    if control_state == '-':
        qc.x(0)
        qc.h(0)
    else: # '+'
        qc.h(0)
        
    # 2. Initialize Target Qubit
    if target_state == '+':
        qc.h(1)
    else: # '-'
        qc.x(1)
        qc.h(1)
    
    pre_oracle = Statevector.from_instruction(qc)
    
    # 3. Apply Balanced Oracle (f(x)=x)
    qc.cx(0, 1)
    
    post_oracle = Statevector.from_instruction(qc)
    
    print(f"\n--- Testing Control:|{control_state}>, Target:|{target_state}> ---")
    print(f"Pre-Oracle:  {pre_oracle.draw('text')}")
    print(f"Post-Oracle: {post_oracle.draw('text')}")
    
    # Check if state changed (ignoring global phase)
    if pre_oracle.equiv(post_oracle):
        print("RESULT: No Change (No Kickback)")
    else:
        print("RESULT: State Flipped (Phase Kickback occurred)")

if __name__ == "__main__":
    run_analysis('-', '+')
    
    # Standard Deutsch setup
    run_analysis('+', '-')
