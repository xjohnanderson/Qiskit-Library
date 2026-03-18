from qiskit import QuantumCircuit

# Provides modular basis-state preparation and transformation methods for use across quantum algorithms
 
def encode_x_basis(qc, state_symbol, qubit_index):
    """
    Function Constraints:
    Inputs: 
        - qc (QuantumCircuit): The circuit to modify.
        - state_symbol (str): The desired state, either '+' or '-'.
        - qubit_index (int): The index of the qubit to initialize.
    Outputs: None (Modifies QuantumCircuit in-place).
    What it does: Maps a '+' or '-' symbol to the corresponding quantum 
    superposition state on the X-axis of the Bloch sphere.
    """
    if state_symbol == '-':
        qc.x(qubit_index)
    
    # Applying H to |0> creates |+>; applying H to |1> creates |->
    qc.h(qubit_index)



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