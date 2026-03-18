# deutsch_problem/kickback_comparison.py

from factories.basis_factory import X_BASIS
from factories.state_factory import get_cx_statevector

def run_analysis(control_state, target_state):
    """
    Function Constraints:
    Inputs: control_state (str), target_state (str)
    Outputs: Prints comparison of statevectors.
    What it does: Compares a pure X-basis state with its CX-evolved counterpart.
    """
    label = f"{control_state}{target_state}"
    
    # 1. Get the pre-oracle state directly from the basis factory
    pre_oracle = X_BASIS[label]
    
    # 2. Get the post-oracle state directly from the state factory
    post_oracle = get_cx_statevector(label)
    
    print(f"\n--- Testing |{label}> ---")
    print(f"Pre-CX:  {pre_oracle.draw('text')}")
    print(f"Post-CX: {post_oracle.draw('text')}")
    
    if pre_oracle.equiv(post_oracle):
        print("RESULT: No Change")
    else:
        print("RESULT: Phase Kickback Detected")

if __name__ == "__main__":
    run_analysis('-', '+') # No kickback
    run_analysis('+', '-') # Kickback occurs