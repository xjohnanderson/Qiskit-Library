"""
Script: cz_entanglement.py
Description: This script demonstrates how the CZ gate processes two X-basis inputs 
to produce an entangled Statevector. It leverages the basis_factory for 
modular state preparation.
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from factories.basis_factory import X_BASIS

def compute_cz_state(sign_a: str, sign_b: str) -> Statevector:
    """
    Function Constraints:
    Inputs: sign_a (str), sign_b (str) -> '+' or '-'
    Outputs: Statevector
    Logic: Retrieves the requested 2-qubit X-basis state and applies a CZ gate
           to induce entanglement, returning the final Statevector.
    """
    # 1. Retrieve initial state from factory (e.g., '++', '+-', etc.)
    label = f"{sign_a}{sign_b}"
    initial_state = X_BASIS[label]
    
    # 2. Define CZ gate as an operator or via circuit
    qc = QuantumCircuit(2)
    qc.prepare_state(initial_state)
    qc.cz(0, 1)
    
    return Statevector.from_instruction(qc)

if __name__ == "__main__":
    # Example: Processing input states |-> and |->
    # In the X-basis, CZ acts as a phase-flip provider for the |-- > state
    result_vector = compute_cz_state('-', '-')
    
    print("Resulting Entangled Statevector:")
    print(result_vector)
    
    # Verification: Show probabilities
    print("\nProbabilities (Should remain 0.25 for all computational bases):")
    print(result_vector.probabilities_dict())