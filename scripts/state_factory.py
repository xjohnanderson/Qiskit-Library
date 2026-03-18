# scripts/state_factory.py

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def get_cz_statevector(label):
    """
    Function Constraint:
    Inputs: label (str) -> e.g., '++', '+-', '-+', or '--'
    Outputs: qiskit.quantum_info.Statevector -> The entangled state.
    Logic: Retrieves a pre-defined X-basis state and evolves it 
    via a Controlled-Z gate.
    """
    # Retrieve the state from the existing X_BASIS dictionary
    initial_state = X_BASIS[label]
    
    # Evolve the statevector using the CZ operator directly
    return initial_state.evolve(QuantumCircuit(2).cz(0, 1))