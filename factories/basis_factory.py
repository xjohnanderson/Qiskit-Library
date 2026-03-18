# factories/basis_factory.py

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


def get_2qubit_y_basis():
    # Function Constraints:
    # Inputs: None
    # Outputs: dict -> Keys 'rr', 'rl', 'lr', 'll' mapped to Statevector objects.
    # Logic: Generates Y-basis (Circular) states using H and S gates. 
    # 'r' corresponds to |i> and 'l' corresponds to |-i>.
    states = {}
    labels = ['rr', 'rl', 'lr', 'll']
    for label in labels:
        qc = QuantumCircuit(2)
        for i, char in enumerate(label):
            if char == 'l': 
                qc.x(i)
            # Map |0> -> |i> and |1> -> |-i>
            qc.h(i)
            qc.s(i)
        states[label] = Statevector.from_instruction(qc)
    return states

# Pre-initialized constants for instant import
Z_BASIS = get_2qubit_z_basis()
X_BASIS = get_2qubit_x_basis()
Y_BASIS = get_2qubit_y_basis()