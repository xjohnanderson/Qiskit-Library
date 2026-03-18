# factories/state_factory.py
# Script: Provides high-level methods to evolve basis states into specific oracle-transformed states.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from scripts.basis_factory import X_BASIS

def get_cz_statevector(label):
    """
    Function Constraint:
    Inputs: label (str) -> e.g., '++', '+-', '-+', or '--'
    Outputs: qiskit.quantum_info.Statevector
    What it does: Retrieves a pre-defined X-basis state and evolves it via a CZ gate.
    """
    initial_state = X_BASIS[label]
    qc = QuantumCircuit(2)
    qc.cz(0, 1)
    return initial_state.evolve(qc)

def get_cx_statevector(label):
    """
    Function Constraint:
    Inputs: label (str) -> e.g., '++', '+-', '-+', or '--'
    Outputs: qiskit.quantum_info.Statevector
    What it does: Retrieves a pre-defined X-basis state and evolves it via a CX gate.
    In the X-basis, this demonstrates phase kickback when the target is in the |-> state.
    """
    initial_state = X_BASIS[label]
    
    # Define the CX evolution (Control 0, Target 1)
    qc = QuantumCircuit(2)
    qc.cx(0, 1)
    
    return initial_state.evolve(qc)