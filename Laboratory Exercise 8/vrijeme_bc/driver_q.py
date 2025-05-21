import sys
import os
import shutil
from pyke import knowledge_engine, goal, krb_traceback

def initialize_engine_with_questions(kb_directory_path_abs):
    print(f"DEBUG [driver_q.py]: Initializing PyKE engine for {kb_directory_path_abs} (with questions).", file=sys.stderr)
    
    compiled_dir = os.path.join(kb_directory_path_abs, 'compiled_krb') 
    
    if os.path.isdir(compiled_dir):
        try:
            shutil.rmtree(compiled_dir)
            print(f"DEBUG [driver_q.py]: DELETED old compiled directory: {compiled_dir}", file=sys.stderr)
        except Exception as e_rm:
            print(f"ERROR [driver_q.py]: Could not delete {compiled_dir}: {e_rm}. Attempting to continue.", file=sys.stderr)
    
    if not os.path.exists(compiled_dir):
        try:
            os.makedirs(compiled_dir)
            print(f"DEBUG [driver_q.py]: Created directory: {compiled_dir}", file=sys.stderr)
        except OSError as e:
            print(f"ERROR [driver_q.py]: Could not create directory {compiled_dir}: {e}", file=sys.stderr)
            return None
            
    init_py_path = os.path.join(compiled_dir, "__init__.py")
    try:
        with open(init_py_path, "w") as f:
            f.write("# PyKE compiled files package\n")
        print(f"DEBUG [driver_q.py]: Ensured {init_py_path} exists.", file=sys.stderr)
    except OSError as e:
        print(f"WARNING [driver_q.py]: Could not create/ensure {init_py_path}: {e}. PyKE might still work.", file=sys.stderr)

    engine_instance = None
    path_added_to_sys = False
    # Dodajemo KB_DIRECTORY_PATH u sys.path da PyKE može naći kompajlirani paket 'compiled_krb'
    # Ovo je bitno ako PyKE interno importuje module iz compiled_krb koristeći relativne putanje
    # u odnosu na kb_directory_path_abs.
    if kb_directory_path_abs not in sys.path:
        sys.path.insert(0, kb_directory_path_abs)
        path_added_to_sys = True
        print(f"DEBUG [driver_q.py]: Added to sys.path: {kb_directory_path_abs}", file=sys.stderr)

    try:
        print(f"DEBUG [driver_q.py]: Calling knowledge_engine.engine with path: '{kb_directory_path_abs}'", file=sys.stderr)
        engine_instance = knowledge_engine.engine(kb_directory_path_abs)
        print("DEBUG [driver_q.py]: PyKE engine initialized successfully.", file=sys.stderr)
    except Exception as e_init:
        print(f"FATAL ERROR [driver_q.py]: Could not initialize PyKE engine: {e_init}", file=sys.stderr)
        krb_traceback.print_exc(file=sys.stderr)
        engine_instance = None 
    finally:
        if path_added_to_sys and kb_directory_path_abs in sys.path:
            try: 
                sys.path.remove(kb_directory_path_abs)
                print(f"DEBUG [driver_q.py]: Removed from sys.path: {kb_directory_path_abs}", file=sys.stderr)
            except ValueError: pass
            
    return engine_instance

def get_advice_task4(current_engine):
    if current_engine is None:
        print("ERROR [driver_q.py]: Engine is None.", file=sys.stderr)
        return "Greška: Engine nije dostupan", "Greška: Engine nije dostupan"

    print("\nMolimo odgovorite na sljedeća pitanja:")

    print("Activating rule base 'pravila_sa_pitanjima.krb'...")
    try:
        current_engine.activate('pravila_sa_pitanjima')
        print("Rule base 'pravila_sa_pitanjima' activated.")
    except Exception as e_activate:
        print(f"Error during rule base activation: {e_activate}", file=sys.stderr)
        krb_traceback.print_exc(file=sys.stderr)
        return f"Greška aktivacije: {e_activate}", f"Greška aktivacije: {e_activate}"

    # --- Prvi cilj: Savjet za vremenske prilike ---
    print("Traženje savjeta za vremenske prilike...", file=sys.stderr)
    # Ime baze pravila je 'pravila_sa_pitanjima'. Cilj definisan u 'use' je 'sta_ponijeti'.
    weather_advice_goal_syntax = 'pravila_sa_pitanjima.sta_ponijeti($item)'
    weather_advice_goal = goal.compile(weather_advice_goal_syntax)
    weather_item_to_carry = None
    try:
        with weather_advice_goal.prove(current_engine) as gen:
            if gen:
                for vars_found, _ in gen:
                    weather_item_to_carry = vars_found.get('item')
                    print(f"DEBUG [driver_q.py]: Weather advice found: {weather_item_to_carry}", file=sys.stderr)
                    break
            else:
                print("WARNING [driver_q.py]: No solution for weather advice goal (prove returned no generator).", file=sys.stderr)
    except Exception as e_prove_weather:
        print(f"Greška pri traženju savjeta za vrijeme: {e_prove_weather}", file=sys.stderr)
        krb_traceback.print_exc(file=sys.stderr)

    weather_recommendation = "Ništa" 
    if weather_item_to_carry == "kabanicu": weather_recommendation = "Kabanicu"
    elif weather_item_to_carry == "kisobran": weather_recommendation = "Kišobran"
    elif weather_item_to_carry == "nista": weather_recommendation = "Ništa"
    elif weather_item_to_carry:
        print(f"INFO [driver_q.py]: Weather rule returned unexpected: '{weather_item_to_carry}'. Defaulting to Ništa.", file=sys.stderr)
    else: 
        print(f"INFO [driver_q.py]: No specific weather rule matched. Defaulting to Ništa.", file=sys.stderr)


    # --- Drugi cilj: Savjet za vanredne situacije ---
    print("Traženje savjeta za vanredne situacije...", file=sys.stderr)
    # Ime baze pravila je 'pravila_sa_pitanjima'. Cilj definisan u 'use' je 'sta_jos_ponijeti'.
    emergency_advice_goal_syntax = 'pravila_sa_pitanjima.sta_jos_ponijeti($dodatna_stvar)'
    emergency_advice_goal = goal.compile(emergency_advice_goal_syntax)
    emergency_item_to_carry = None
    try:
        with emergency_advice_goal.prove(current_engine) as gen_emergency:
            if gen_emergency:
                for vars_found, _ in gen_emergency:
                    emergency_item_to_carry = vars_found.get('dodatna_stvar')
                    print(f"DEBUG [driver_q.py]: Emergency advice found: {emergency_item_to_carry}", file=sys.stderr)
                    break
            else:
                print("WARNING [driver_q.py]: No solution for emergency advice goal (prove returned no generator).", file=sys.stderr)
    except Exception as e_prove_emergency:
        print(f"Greška pri traženju savjeta za vanredne situacije: {e_prove_emergency}", file=sys.stderr)
        krb_traceback.print_exc(file=sys.stderr)
   
    emergency_recommendation = "Ništa dodatno" 
    if emergency_item_to_carry == "gumene_cizme": emergency_recommendation = "Gumene čizme"
    elif emergency_item_to_carry == "masku_za_lice": emergency_recommendation = "Masku za lice"
    elif emergency_item_to_carry == "nista_dodatno": emergency_recommendation = "Ništa dodatno"
    elif emergency_item_to_carry:
        print(f"INFO [driver_q.py]: Emergency rule returned unexpected: '{emergency_item_to_carry}'. Defaulting to Ništa dodatno.", file=sys.stderr)
    else: 
        print(f"INFO [driver_q.py]: No specific emergency rule matched. Defaulting to Ništa dodatno.", file=sys.stderr)

    return weather_recommendation, emergency_recommendation
   
def run_expert_system_task4(kb_dir_abs):
    print("--- Ekspertni sistem za vrijeme u doba korone (sa pitanjima) ---")
   
    engine_instance = initialize_engine_with_questions(kb_dir_abs)
    if not engine_instance:
        print("Neuspješna inicijalizacija ekspertnog sistema.")
        return
       
    # Nema potrebe za reset() jer je engine svjež svaki put za ovaj test driver
       
    weather_advice, emergency_advice = get_advice_task4(engine_instance)
       
    print("\n--- Preporuke ---")
    print(f"Zbog vremena: Trebate ponijeti -> {weather_advice}")
    print(f"Dodatno zbog situacije: Trebate ponijeti -> {emergency_advice}")
   
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Pokretanje interaktivnog ekspertnog sistema iz: {script_dir}")
    # Osigurajte da su pravila_sa_pitanjima.krb i pitanja.kqb u script_dir
    # i da nema drugih .krb/.kfb/.kqb datoteka koje mogu zbuniti PyKE.
    # Specifično, ako postoji 'pravila.krb' ili 'cinjenice_vremena.kfb' iz prethodnih
    # zadataka u istom direktoriju, to MOŽE izazvati probleme sa PyKE-ovim
    # skeniranjem i kompajliranjem. Najbolje je imati samo datoteke za trenutni zadatak.
    run_expert_system_task4(script_dir)