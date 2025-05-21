import sys
import os
import shutil
from pyke import knowledge_engine, goal, krb_traceback

def initialize_engine(kb_directory_path_abs):
    """
    Initializes a FRESH PyKE engine for the given knowledge base directory.
    """
    print(f"DEBUG [driver.py]: Initializing PyKE engine for {kb_directory_path_abs}.", file=sys.stderr)
    
    compiled_dir = os.path.join(kb_directory_path_abs, 'compiled_krb')
    
    if not os.path.exists(compiled_dir):
        try:
            os.makedirs(compiled_dir)
            print(f"DEBUG [driver.py]: Created directory: {compiled_dir}", file=sys.stderr)
            with open(os.path.join(compiled_dir, "__init__.py"), "w") as f:
                f.write("# PyKE compiled files\n")
            print(f"DEBUG [driver.py]: Created {os.path.join(compiled_dir, '__init__.py')}", file=sys.stderr)
        except OSError as e:
            print(f"ERROR [driver.py]: Could not create {compiled_dir}: {e}", file=sys.stderr)
            return None
    
    current_engine_instance = None 
    path_added_to_sys = False
    if kb_directory_path_abs not in sys.path:
        sys.path.insert(0, kb_directory_path_abs)
        path_added_to_sys = True

    try:
        print(f"DEBUG [driver.py]: Calling knowledge_engine.engine with path: '{kb_directory_path_abs}'", file=sys.stderr)
        current_engine_instance = knowledge_engine.engine(kb_directory_path_abs)
        print("DEBUG [driver.py]: PyKE engine initialized successfully.", file=sys.stderr)
    except Exception as e_init:
        print(f"FATAL ERROR [driver.py]: Could not initialize PyKE engine: {e_init}", file=sys.stderr)
        krb_traceback.print_exc(file=sys.stderr)
        current_engine_instance = None
    finally:
        if path_added_to_sys and kb_directory_path_abs in sys.path:
            try:
                sys.path.remove(kb_directory_path_abs)
            except ValueError:
                pass
    return current_engine_instance

def get_advice_with_bc(current_engine_instance): 
    if current_engine_instance is None:
        print("ERROR [driver.py]: Engine is None in get_advice_with_bc.", file=sys.stderr)
        return "Error: Engine not available"

    print("Activating rule base 'pravila.krb' (this should also make facts from 'cinjenice_vremena.kfb' available)...")
    try:
        current_engine_instance.activate('pravila') # Aktivira samo pravila.krb
        print("Rule base 'pravila' activated.")
    except Exception as e_activate:
        print(f"Error during rule base activation: {e_activate}", file=sys.stderr)
        krb_traceback.print_exc(file=sys.stderr)
        return f"Error activating rule base 'pravila': {e_activate}"

    try:
        print("DEBUG [get_advice_with_bc]: Checking facts after activation 'pravila':", file=sys.stderr)
        facts_found_count = 0
        fc_goal_kisa = goal.compile("cinjenice_vremena.pada_kisa($val)")
        with fc_goal_kisa.prove(current_engine_instance) as gen_kisa:
            if gen_kisa:
                for vars_kisa, _ in gen_kisa:
                    print(f"  DEBUG: Found fact: cinjenice_vremena.pada_kisa({vars_kisa['val']})", file=sys.stderr)
                    facts_found_count += 1
        fc_goal_vjetar = goal.compile("cinjenice_vremena.puse_vjetar($val)")
        with fc_goal_vjetar.prove(current_engine_instance) as gen_vjetar:
            if gen_vjetar:
                for vars_vjetar, _ in gen_vjetar:
                    print(f"  DEBUG: Found fact: cinjenice_vremena.puse_vjetar({vars_vjetar['val']})", file=sys.stderr)
                    facts_found_count += 1
        if facts_found_count < 2: 
            print("  WARNING: Not all expected facts found after activation! Check .kfb content and rule references.", file=sys.stderr)
    except Exception as e_debug_facts:
        print(f"  DEBUG: Error checking facts: {e_debug_facts}", file=sys.stderr)

    print("Seeking advice using backward chaining...")
    advice_goal_syntax = 'pravila.sta_ponijeti($item)' 
    advice_goal = goal.compile(advice_goal_syntax)
    item_to_carry = None

    try:
        with advice_goal.prove(current_engine_instance) as gen:
            if gen:
                for vars_found, _ in gen:
                    item_to_carry = vars_found.get('item')
                    print(f"DEBUG [driver.py]: Advice found through rules: {item_to_carry}", file=sys.stderr)
                    break
            else:
                print(f"WARNING [driver.py]: prove() returned no generator for goal '{advice_goal_syntax}'.", file=sys.stderr)
    except Exception as e_prove:
        print(f"Error during prove() for goal '{advice_goal_syntax}': {e_prove}", file=sys.stderr)
        krb_traceback.print_exc(file=sys.stderr)

    if item_to_carry == "kabanicu":
        return "Kabanicu"
    elif item_to_carry == "kisobran":
        return "Kišobran"
    elif item_to_carry == "nista":
        return "Ništa"
    else:
        if item_to_carry:
            print(f"INFO [driver.py]: Rule returned unexpected value '{item_to_carry}'. Defaulting to 'Ništa'.", file=sys.stderr)
        else:
            print(f"INFO [driver.py]: No rule determined what to carry. Defaulting to 'Ništa'.", file=sys.stderr)
        return "Ništa"

def run_test_scenario(kb_dir_abs, is_raining, is_windy):
    print(f"\n--- Testing with: Raining = {is_raining}, Windy = {is_windy} (BC) ---")

    compiled_dir_to_delete = os.path.join(kb_dir_abs, 'compiled_krb')
    if os.path.isdir(compiled_dir_to_delete):
        try:
            shutil.rmtree(compiled_dir_to_delete)
            print(f"DEBUG [driver.py]: DELETED directory: {compiled_dir_to_delete}", file=sys.stderr)
        except Exception as e_rm:
            print(f"ERROR [driver.py]: Could not delete {compiled_dir_to_delete}: {e_rm}.", file=sys.stderr)
    
    kfb_content = f"pada_kisa({str(is_raining).lower()})\npuse_vjetar({str(is_windy).lower()})\n"
    kfb_file_path = os.path.join(kb_dir_abs, "cinjenice_vremena.kfb") 
    try:
        with open(kfb_file_path, "w") as f:
            f.write(kfb_content)
        print(f"DEBUG [driver.py]: Facts written to {kfb_file_path} BEFORE engine initialization.", file=sys.stderr)
    except Exception as e_write_kfb:
        print(f"Error writing to '{kfb_file_path}': {e_write_kfb}", file=sys.stderr)
        return

    test_engine_instance = initialize_engine(kb_dir_abs)
    if not test_engine_instance:
        print("Recommendation: Engine initialization error")
        return

    print("DEBUG [driver.py]: Resetting PyKE engine (even though it's a new instance).", file=sys.stderr)
    test_engine_instance.reset() 

    advice = get_advice_with_bc(test_engine_instance) 
    print(f"Recommendation: You should take -> {advice}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Running tests from: {script_dir}")

    run_test_scenario(script_dir, True, True)
    run_test_scenario(script_dir, True, False)
    run_test_scenario(script_dir, False, False)
    run_test_scenario(script_dir, False, True)