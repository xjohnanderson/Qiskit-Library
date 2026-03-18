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
    Transforms a qubit from the computational basis (|0> or |1>) 
    into the X-basis states |+> or |-> on the Bloch sphere based on the 
    provided state_symbol.
    """
    if state_symbol == '-':
        qc.x(qubit_index)
    
    # Applying H to |0> creates |+>; applying H to |1> creates |->
    qc.h(qubit_index)



