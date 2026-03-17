from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


 

def cz(a, b):
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