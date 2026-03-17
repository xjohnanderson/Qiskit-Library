from qiskit import QuantumCircuit
from qiskit.circuit.library import ZGate

# Phase Oracle
def phase_flip_oracle(num_qubits, target_state):
    qc = QuantumCircuit(num_qubits)
    mcz = ZGate().control(num_qubits - 1)
    qc.append(mcz, range(num_qubits))
    
    return qc

# Balanced Oracle
def balanced_oracle():
    qc = QuantumCircuit(2)
    qc.cx(0, 1)  # Performs |x>|y ^ x>
    return qc

