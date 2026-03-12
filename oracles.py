from qiskit import QuantumCircuit
from qiskit.circuit.library import ZGate

def build_phase_flip_oracle(num_qubits, target_state):
    """
    Creates a phase oracle that flips the sign of the target_state.
    """
    qc = QuantumCircuit(num_qubits)
    
    # Identify which qubits are '0' and need an X-gate to match the target
    # In this example, we assume target_state is a binary string '111'
    # To target a state like '011', you'd apply X to q0 before the MCZ
    
    # Multi-controlled Z gate
    # For a 3-qubit system, this is an MCZ with 2 controls and 1 target
    mcz = ZGate().control(num_qubits - 1)
    qc.append(mcz, range(num_qubits))
    
    return qc

# Example usage for 3 qubits targeting state |111>
oracle = build_phase_flip_oracle(3, '111')
print(oracle.draw())