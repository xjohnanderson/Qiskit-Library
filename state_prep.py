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



