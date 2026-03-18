# scripts/basis_factory.py

# Script: Provides high-level access to common 2-qubit statevectors to reduce boilerplate code

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def get_2qubit_z_basis():
    # Function Constraints:
    # Inputs: None
    # Outputs: dict -> Keys '00', '01', '10', '11' mapped to Statevector objects.
    # Logic: Returns the computational basis states for a 2-qubit system.
    return {f"{i:02b}": Statevector.from_label(f"{i:02b}") for i in range(4)}

def get_2qubit_x_basis():
    # Function Constraints:
    # Inputs: None
    # Outputs: dict -> Keys '++', '+-', '-+', '--' mapped to Statevector objects.
    # Logic: Generates X-basis (Phase) states by applying Hadamard transforms.
    states = {}
    for label in ['++', '+-', '-+', '--']:
        qc = QuantumCircuit(2)
        for i, char in enumerate(label):
            if char == '-': qc.x(i)
            qc.h(i)
        states[label] = Statevector.from_instruction(qc)
    return states



def get_cz_statevector(a, b):
    # Input: a (str), b (str) -> '+' or '-' representing the initial phase of each qubit.
    # Output: qiskit.quantum_info.Statevector -> The resulting 2-qubit entangled state.
    # Description: Initializes two qubits in the X-basis based on input signs, 
    # entangles them via a Controlled-Z (CZ) gate, and computes the system statevector.
   
    qc = QuantumCircuit(2)
    
    # Initialize qubits based on input (+ or -)
    if a == '-':
        qc.x(0)
    qc.h(0)
    
    if b == '-':
        qc.x(1)
    qc.h(1)
    
    # Apply CZ
    qc.cz(0, 1)
    
    return Statevector.from_instruction(qc)

# Pre-initialized constants for instant import
Z_BASIS = get_2qubit_z_basis()
X_BASIS = get_2qubit_x_basis()