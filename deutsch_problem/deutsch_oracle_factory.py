# deutsch_oracle_factory.py

# Script: Generates 2-qubit QuantumCircuit objects for Deutsch oracles, 
# categorized into constant and balanced functional cases. 
# Includes a verification block for phase kickback behavior.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def get_deutsch_oracle(case):
    # Function Constraints:
    # Inputs: case (str) -> Key representing function type ('c0', 'c1', 'b0', 'b1').
    # Outputs: qiskit.QuantumCircuit -> 2-qubit circuit implementing the oracle.
    # Logic: Maps |x, y> to |x, y ⊕ f(x)> based on constant or balanced f(x).
    oracle_qc = QuantumCircuit(2, name=f"U_f_{case}")
    
    if case == 'c0':
        # f(x) = 0
        pass 
    elif case == 'c1':
        # f(x) = 1
        oracle_qc.x(1)
    elif case == 'b0':
        # f(x) = x
        oracle_qc.cx(0, 1)
    elif case == 'b1':
        # f(x) = NOT x
        oracle_qc.x(0)
        oracle_qc.cx(0, 1)
        oracle_qc.x(0)
        
    return oracle_qc

def get_all_oracles():
    # Function Constraints:
    # Inputs: None
    # Outputs: dict -> Dictionary mapping case labels to their respective QuantumCircuits.
    # Logic: Iterates through standard cases to provide a complete oracle set.
    cases = ['c0', 'c1', 'b0', 'b1']
    return {case: get_deutsch_oracle(case) for case in cases}

if __name__ == "__main__":
    # This block only runs when the script is executed directly, not when imported.
    # Verification using basis_states (Assumes basis_states.py is in the same directory)
    try:
        from basis_states import X_BASIS
        input_state = X_BASIS['+-']
        
        print("Verifying Phase Kickback (|+-> input):")
        for case, oracle in get_all_oracles().items():
            final_state = input_state.evolve(oracle)
            print(f"Case {case}: Resulting Statevector -> {final_state.draw('latex')}")
    except ImportError:
        print("basis_states.py not found. Skipping verification.")
