# In vrijeme_driver.py

import sys
import os
import time
from pyke import knowledge_engine, goal, krb_traceback

# Global engine variable, initially None
engine = None
KB_DIRECTORY_PATH = None # Store the path globally once set

def initialize_engine_if_needed(kb_dir_from_notebook):
    global engine, KB_DIRECTORY_PATH
    if engine is None: 
        KB_DIRECTORY_PATH = os.path.abspath(str(kb_dir_from_notebook))

        print(f"DEBUG [vrijeme_driver.py]: Initializing PyKE engine.", file=sys.stderr)
        print(f"DEBUG [vrijeme_driver.py]: Using source directory: {KB_DIRECTORY_PATH}", file=sys.stderr)
        
        compiled_krb_dir = os.path.join(KB_DIRECTORY_PATH, 'compiled_krb')
        # Ensure compiled_krb directory exists
        if not os.path.exists(compiled_krb_dir):
            try:
                os.makedirs(compiled_krb_dir)
                print(f"DEBUG [vrijeme_driver.py]: Created directory: {compiled_krb_dir}", file=sys.stderr)
            except OSError as e:
                print(f"ERROR [vrijeme_driver.py]: Could not create {compiled_krb_dir}: {e}", file=sys.stderr)
        else:
            print(f"DEBUG [vrijeme_driver.py]: Directory {compiled_krb_dir} already exists.", file=sys.stderr)

        # The target package name PyKE will use for the compiled files from KB_DIRECTORY_PATH.
        # It's often relative to the source, or a dot implies relative to the compiled root.
        # Let's try making it simple. PyKE will create a sub-package within compiled_krb.
        # We want compiled files to go into 'compiled_krb' within our KB_DIRECTORY_PATH.
        # PyKE's engine expects search_paths to be a sequence.
        # Each item can be a string (a source dir) or a (source_dir, target_pkg_name_str) tuple.
        # The target_pkg_name_str is what PyKE will try to import later.
        # Let's try providing the *compiled directory itself* as a potential hint.

        # PyKE's engine expects a sequence of search paths.
        # Each search path can be a string (directory) or a tuple:
        # (directory, target_package_name_string)
        # or (directory, (target_package_name_string, target_package_directory))
        
        # The issue seems to be with PyKE trying to import a package named '.compiled_krb'
        # and then get its __file__ attribute, which fails.

        # Let's give it the source directory and tell it the name of the package
        # it should create for the compiled files *within* that source directory's
        # 'compiled_krb' subdirectory.
        # The target package name should be relative to a Python path entry.
        # Since KB_DIRECTORY_PATH will contain compiled_krb, the package name
        # for compiled files could be something like 'compiled_krb.generated_rules'

        # What if we just give it the source path and ensure compiled_krb exists?
        # The engine is supposed to handle creating .compiled_krb relative to the source path.

        # Let's simplify and go back to the most basic call, ensuring compiled_krb exists.
        # The error trace points to PyKE's target_pkg.py, line 102:
        # self.directory = os.path.dirname(import_(self.package_name).__file__)
        # Here, self.package_name is likely '.compiled_krb' (a default).
        # The problem is import_('.compiled_krb').__file__ is None.

        # This indicates the dynamically created/found '.compiled_krb' package is not
        # being recognized by Python's import system as having a file location.

        # This might be a deeper Python 3.11 + PyKE 1.1.1 incompatibility on Windows
        # related to dynamic module loading and __file__ attributes.

        # WORKAROUND ATTEMPT:
        # Try to add the 'compiled_krb' directory to sys.path temporarily
        # BEFORE initializing the engine, so that when PyKE tries to import '.compiled_krb',
        # Python might find it as a top-level package.

        added_compiled_path = False
        if compiled_krb_dir not in sys.path:
            sys.path.insert(0, compiled_krb_dir) # Add to front of path
            added_compiled_path = True
            print(f"DEBUG [vrijeme_driver.py]: Temporarily added to sys.path: {compiled_krb_dir}", file=sys.stderr)
        
        try:
            print(f"DEBUG [vrijeme_driver.py]: Calling knowledge_engine.engine with search path: '{KB_DIRECTORY_PATH}'", file=sys.stderr)
            engine = knowledge_engine.engine(KB_DIRECTORY_PATH) 
            print("DEBUG [vrijeme_driver.py]: PyKE engine initialized successfully.", file=sys.stderr)
        except Exception as e_init: 
            print(f"FATAL ERROR [vrijeme_driver.py]: Could not initialize PyKE engine: {e_init}", file=sys.stderr)
            print(f"Value and type of KB_DIRECTORY_PATH passed to engine was: '{KB_DIRECTORY_PATH}' ({type(KB_DIRECTORY_PATH)})", file=sys.stderr)
            import traceback
            traceback.print_exc(file=sys.stderr) 
            engine = None 
        finally:
            # Clean up sys.path if we modified it
            if added_compiled_path and compiled_krb_dir in sys.path:
                try:
                    sys.path.remove(compiled_krb_dir)
                    print(f"DEBUG [vrijeme_driver.py]: Removed from sys.path: {compiled_krb_dir}", file=sys.stderr)
                except ValueError:
                    pass # Should not happen if added_compiled_path is True
            
    return engine is not None

def dobij_preporuku():
    global engine 
    if engine is None:
        print("ERROR [vrijeme_driver.py]: Engine not initialized in dobij_preporuku. Call initialize_engine_if_needed first.", file=sys.stderr)
        return "Greška: Engine nije inicijalizovan"
            
    engine.reset()
    print("Aktiviranje pravila iz 'vrijeme_rules.krb'...")
    try:
        engine.activate('vrijeme_rules') 
        print("Pravila aktivirana.")
    except KeyError as ke: 
        print(f"GREŠKA: Rule base 'vrijeme_rules' nije pronađen. Provjerite .krb fajl i da li je kompajliran: {ke}", file=sys.stderr)
        return f"Greška: Rule base '{ke}' nije pronađen" # More specific error
    except Exception as e:
        print(f"Greška prilikom aktivacije pravila: {e}")
        return f"Greška aktivacije: {e}"

    print("Traženje preporuke...")
    preporuka_goal = goal.compile('vrijeme.ponesi($sta_poneti)')
    item_to_carry = "Ništa (pravilo nije pronašlo preporuku)" 

    try:
        with preporuka_goal.prove(engine) as gen:
            for vars_found, plan in gen:
                item_to_carry = vars_found.get('sta_poneti')
                break 
    except Exception as e:
        print(f"Greška prilikom izvršavanja prove() za cilj: {e}")
        return f"Greška prove: {e}" 

    if item_to_carry == "kabanicu":
        return "Kabanicu"
    elif item_to_carry == "kisobran":
        return "Kišobran"
    elif item_to_carry == "nista": 
        return "Ništa"
    else: 
        return f"Ništa (nedefinisano: '{item_to_carry}')"

def testiraj_sistem(kb_path_from_notebook, pada_kisa_cinjenica, puse_vjetar_cinjenica):
    global KB_DIRECTORY_PATH 
    
    if not initialize_engine_if_needed(kb_path_from_notebook):
        # initialize_engine_if_needed will print the FATAL ERROR if it fails
        print("Preporuka: Greška engine-a (nije inicijalizovan)") 
        return 

    print(f"\n--- Testiranje sa: Kiša pada = {pada_kisa_cinjenica}, Vjetar puše = {puse_vjetar_cinjenica} ---")
    
    kfb_sadrzaj = f"""
pada_kisa({str(pada_kisa_cinjenica)})
puse_vjetar({str(puse_vjetar_cinjenica)})
"""
    kfb_fajl_putanja = os.path.join(KB_DIRECTORY_PATH, "vrijeme.kfb")

    try:
        with open(kfb_fajl_putanja, "w") as f:
            f.write(kfb_sadrzaj)
    except Exception as e:
        print(f"Greška prilikom pisanja u '{kfb_fajl_putanja}': {e}")
        return

    preporuka = dobij_preporuku()
    
    print(f"Preporuka: Trebate ponijeti -> {preporuka}")


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    testiraj_sistem(current_dir, True, True)
    testiraj_sistem(current_dir, True, False)
    testiraj_sistem(current_dir, False, False)
    testiraj_sistem(current_dir, False, True)