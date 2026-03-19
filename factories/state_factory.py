# factories/state_factory.py
# Script: Provides high-level methods to evolve basis states into specific oracle-transformed states.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from scripts.basis_factory import X_BASIS


def _evolve_x_basis(label, gate_type):
    """
    Function Constraint:
    Inputs: 
        - label (str): X-basis state label.
        - gate_type (str): 'cx' or 'cz'.
    Outputs: qiskit.quantum_info.Statevector
    What it does: Helper to evolve X_BASIS states by a specific gate.
    """
    initial_state = X_BASIS[label]
    qc = QuantumCircuit(2)
    
    if gate_type == 'cx':
        qc.cx(0, 1)
    elif gate_type == 'cz':
        qc.cz(0, 1)
    elif gate_type == 'cy':
        qc.cy(0, 1)
    else:
        print("Error missing case")
        
    return initial_state.evolve(qc)

def get_cz_statevector(label):
    """
    Function Constraint:
    Inputs: label (str)
    Outputs: qiskit.quantum_info.Statevector
    What it does: Evolves X-basis state via a CZ gate (Symmetric phase flip).
    """
    return _evolve_x_basis(label, 'cz')

def get_cx_statevector(label):
    """
    Function Constraint:
    Inputs: label (str)
    Outputs: qiskit.quantum_info.Statevector
    What it does: Evolves X-basis state via a CX gate (Directional phase kickback).
    """
    return _evolve_x_basis(label, 'cx')



def get_cy_statevector(label):
    """
    Function Constraint:
    Inputs: label (str)
    Outputs: qiskit.quantum_info.Statevector
    What it does: Evolves X-basis state via a CY gate (Complex phase rotation kickback).
    """
    return _evolve_x_basis(label, 'cy')