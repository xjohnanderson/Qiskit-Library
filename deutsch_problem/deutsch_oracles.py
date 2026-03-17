# Script: Defines 2-qubit Deutsch oracles and demonstrates their effect on 
# phase states to verify balanced vs constant behavior.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from basis_states import X_BASIS  # Importing your condensed basis states

def get_oracle(case):
    # Function Constraints:
    # Inputs: case (str) -> 'c0', 'c1' (constant) or 'b0', 'b1' (balanced)
    # Outputs: qiskit.QuantumCircuit -> A 2-qubit oracle circuit
    # Logic: Implements f(x) mapping where the second qubit is the target.
    oracle_qc = QuantumCircuit(2, name=f"U_f_{case}")
    
    if case == 'c0':
        pass 
    elif case == 'c1':
        oracle_qc.x(1)
    elif case == 'b0':
        oracle_qc.cx(0, 1)
    elif case == 'b1':
        oracle_qc.x(0)
        oracle_qc.cx(0, 1)
        oracle_qc.x(0)
        
    return oracle_qc

# Verification using basis_states
# The Deutsch algorithm relies on the input state |+->
input_state = X_BASIS['+-']

for case in ['c0', 'c1', 'b0', 'b1']:
    oracle = get_oracle(case)
    # Evolve the |+-> state through the oracle
    final_state = input_state.evolve(oracle)
    
    # Logic: If constant, the first qubit stays |+>. If balanced, it flips to |->.
    # We check the first qubit's phase by looking at the resulting statevector.
    print(f"Case {case}: Resulting Statevector Label -> {final_state.draw('latex')}")