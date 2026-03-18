# kickback_comparison.py

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

def run_analysis(control_state, target_state):
    """
    Function Constraints:
    Inputs: 
        - control_state (str): '+' or '-' for qubit 0.
        - target_state (str): '+' or '-' for qubit 1.
    Outputs: Prints comparison of statevectors and kickback result.
    What it does: Simulates a balanced oracle to observe phase kickback.
    """
    qc = QuantumCircuit(2)
    
    # 1. Initialize Qubits using the library method
    encode_x_basis(qc, control_state, 0)
    encode_x_basis(qc, target_state, 1)
    
    pre_oracle = Statevector.from_instruction(qc)
    
    # 2. Apply Balanced Oracle (CX gate)
    # In the X-basis, CX acts as a phase-flipper if the target is in |->
    qc.cx(0, 1)
    
    post_oracle = Statevector.from_instruction(qc)
    
    # 3. Report Results
    print(f"\n--- Testing Control: |{control_state}>, Target: |{target_state}> ---")
    print(f"Pre-Oracle:  {pre_oracle.draw('text')}")
    print(f"Post-Oracle: {post_oracle.draw('text')}")
    
    if pre_oracle.equiv(post_oracle):
        print("RESULT: No Change (No Kickback)")
    else:
        # If target is |->, the control |+> will flip to |->
        print("RESULT: State Flipped (Phase Kickback occurred)")

if __name__ == "__main__":
    run_analysis('-', '+')
    
    # Standard Deutsch setup
    run_analysis('+', '-')
