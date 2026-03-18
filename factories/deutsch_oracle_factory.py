# factories/deutsch_oracle_factory.py

# Script: Generates 2-qubit QuantumCircuit objects for Deutsch oracles, 
# categorized into constant and balanced functional cases. 
# Includes a verification block for phase kickback behavior using external factories.

from qiskit import QuantumCircuit
from factories.basis_factory import X_BASIS

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
    # This block performs verification using the modular basis_factory.
    # It demonstrates phase kickback: for balanced oracles, the control qubit (0) 
    # should flip phase when the target is in the |-> state.
    
    # We use the '+-' state (|+> on q0, |-> on q1) to observe kickback.
    input_state = X_BASIS['+-']
    
    print("Verifying Phase Kickback (|+-> input):")
    print("-" * 40)
    for case, oracle in get_all_oracles().items():
        final_state = input_state.evolve(oracle)
        # For 'b0' and 'b1', the state should evolve toward |--> or -|--> 
        # (phase flip on the first qubit).
        print(f"Case {case}: Resulting Statevector -> {final_state.draw('latex')}")