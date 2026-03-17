# deutsch_oracles.py

from qiskit import QuantumCircuit

def get_oracle(case):
    """
    Returns a 2-qubit Deutsch oracle based on the case:
    'c0' : Constant 0
    'c1' : Constant 1
    'b0' : Balanced (f(x) = x)
    'b1' : Balanced (f(x) = not x)
    """
    oracle_qc = QuantumCircuit(2, name=f"U_f_{case}")
    
    if case == 'c0':
        # f(x) = 0: Target remains y
        pass 
    elif case == 'c1':
        # f(x) = 1: Target becomes y ^ 1
        oracle_qc.x(1)
    elif case == 'b0':
        # f(x) = x: Target becomes y ^ x
        oracle_qc.cx(0, 1)
    elif case == 'b1':
        # f(x) = !x: Target becomes y ^ (!x)
        oracle_qc.x(0)
        oracle_qc.cx(0, 1)
        oracle_qc.x(0)
        
    return oracle_qc

# Example usage: 
# circuit = get_oracle('b1')
# print(circuit)
