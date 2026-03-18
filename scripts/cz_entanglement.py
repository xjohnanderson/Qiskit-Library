# scripts/cz_entanglement.py

# This script demonstrates how the CZ gate processes two X-basis inputs 
# to produce an entangled Statevector. It maps the provided logic 
# into a modular function that can be imported into larger 
# quantum graph-state simulations.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def compute_cz_state(sign_a: str, sign_b: str) -> Statevector:
    # Initialize 2-qubit circuit
    qc = QuantumCircuit(2)
    
    # Prepare Qubit 0 in X-basis
    if sign_a == '-':
        qc.x(0)
    qc.h(0)
    
    # Prepare Qubit 1 in X-basis
    if sign_b == '-':
        qc.x(1)
    qc.h(1)
    
    # Apply Controlled-Z
    # Note: CZ is symmetric; qc.cz(0, 1) is identical to qc.cz(1, 0)
    qc.cz(0, 1)
    
    return Statevector.from_instruction(qc)

if __name__ == "__main__":
    # Example: Processing input states |-> and |->
    result_vector = compute_cz_state('-', '-')
    print("Resulting Entangled Statevector:")
    print(result_vector)
    
    # Show probabilities to demonstrate the state remains in superposition
    print("\nProbabilities:")
    print(result_vector.probabilities_dict())