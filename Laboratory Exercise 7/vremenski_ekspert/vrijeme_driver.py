import sys
import os
import time
import shutil
from pyke import knowledge_engine, goal, krb_traceback

engine = None
_initialized_kb_path = None

def initialize_engine_if_needed(kb_dir_from_notebook):
    global engine, _initialized_kb_path
    
    current_kb_path_abs = os.path.abspath(str(kb_dir_from_notebook))
    _initialized_kb_path = current_kb_path_abs 

    print(f"DEBUG [vrijeme_driver.py]: Inicijalizacija PyKE engine-a za {_initialized_kb_path}.", file=sys.stderr)
    
    compiled_krb_dir = os.path.join(_initialized_kb_path, 'compiled_krb')
    
    if not os.path.exists(compiled_krb_dir):
        try:
            os.makedirs(compiled_krb_dir)
            print(f"DEBUG [vrijeme_driver.py]: Kreiran direktorij: {compiled_krb_dir}", file=sys.stderr)
        except OSError as e:
            print(f"ERROR [vrijeme_driver.py]: Nije moguće kreirati {compiled_krb_dir}: {e}", file=sys.stderr)
            engine = None
            return False
    else:
        print(f"DEBUG [vrijeme_driver.py]: Direktorij {compiled_krb_dir} već postoji.", file=sys.stderr)

    init_py_path = os.path.join(compiled_krb_dir, "__init__.py")
    if not os.path.exists(init_py_path):
        try:
            with open(init_py_path, "w") as f:
                f.write("# PyKE compiled files package\n")
            print(f"DEBUG [vrijeme_driver.py]: Kreiran {init_py_path}", file=sys.stderr)
        except OSError as e:
            print(f"ERROR [vrijeme_driver.py]: Nije moguće kreirati {init_py_path}: {e}", file=sys.stderr)

    path_to_add_to_sys = _initialized_kb_path
    added_to_sys_path = False

    if path_to_add_to_sys not in sys.path:
        sys.path.insert(0, path_to_add_to_sys)
        added_to_sys_path = True
        print(f"DEBUG [vrijeme_driver.py]: Privremeno dodato u sys.path: {path_to_add_to_sys}", file=sys.stderr)
    
    try:
        print(f"DEBUG [vrijeme_driver.py]: Pozivanje knowledge_engine.engine sa putanjom: '{_initialized_kb_path}'", file=sys.stderr)
        # Kreiranje NOVE instance engine-a svaki put
        engine = knowledge_engine.engine(_initialized_kb_path) 
        print("DEBUG [vrijeme_driver.py]: PyKE engine uspješno inicijalizovan.", file=sys.stderr)
    except Exception as e_init: 
        print(f"FATAL ERROR [vrijeme_driver.py]: Nije moguće inicijalizovati PyKE engine: {e_init}", file=sys.stderr)
        print(f"Putanja proslijeđena engine-u: '{_initialized_kb_path}' ({type(_initialized_kb_path)})", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr) 
        engine = None 
    finally:

        if added_to_sys_path and path_to_add_to_sys in sys.path:
            try:
                sys.path.remove(path_to_add_to_sys)
                print(f"DEBUG [vrijeme_driver.py]: Uklonjeno iz sys.path: {path_to_add_to_sys}", file=sys.stderr)
            except ValueError:
                pass 
            
    return engine is not None

def dobij_preporuku():
    global engine
    if engine is None:
        print("ERROR [vrijeme_driver.py]: Engine nije inicijalizovan u dobij_preporuku.", file=sys.stderr)
        return "Greška: Engine nije inicijalizovan"

    print("Aktiviranje pravila iz 'vrijeme_rules.krb' (koristiće kompajlirane činjenice)...")
    try:
        engine.activate('vrijeme_rules')
        print("Pravila aktivirana.")
    except KeyError as ke:
        print(f"GREŠKA: Baza pravila 'vrijeme_rules' (iz vrijeme_rules.krb) nije pronađena: {ke}", file=sys.stderr)
        return f"Greška: Baza pravila '{ke}' nije pronađena"
    except Exception as e_activate:
        print(f"Greška prilikom aktivacije pravila: {e_activate}", file=sys.stderr)
        krb_traceback.print_exc(file=sys.stderr)
        return f"Greška aktivacije: {e_activate}"

    try:
        print("DEBUG [dobij_preporuku]: Provjera činjenica nakon aktivacije 'vrijeme_rules':", file=sys.stderr)
        facts_found_count = 0
        fc_goal_kisa = goal.compile("vrijeme.pada_kisa($val)")
        with fc_goal_kisa.prove(engine) as gen_kisa:
            if gen_kisa:
                for vars_kisa, plan_kisa in gen_kisa:
                    print(f"  DEBUG: Pronađena činjenica: vrijeme.pada_kisa({vars_kisa['val']})", file=sys.stderr)
                    facts_found_count +=1
        fc_goal_vjetar = goal.compile("vrijeme.puse_vjetar($val)")
        with fc_goal_vjetar.prove(engine) as gen_vjetar:
            if gen_vjetar:
                for vars_vjetar, plan_vjetar in gen_vjetar:
                    print(f"  DEBUG: Pronađena činjenica: vrijeme.puse_vjetar({vars_vjetar['val']})", file=sys.stderr)
                    facts_found_count +=1
        if facts_found_count == 0:
            print("  DEBUG: Nije pronađena nijedna očekivana činjenica (pada_kisa, puse_vjetar) nakon aktivacije!", file=sys.stderr)
    except Exception as e_debug_facts:
        print(f"  DEBUG: Greška pri provjeri činjenica: {e_debug_facts}", file=sys.stderr)

    print("Traženje preporuke...")
    preporuka_goal_syntax = 'vrijeme.ponesi($sta_poneti)'
    preporuka_goal = goal.compile(preporuka_goal_syntax)
    item_to_carry_from_goal = None

    try:
        with preporuka_goal.prove(engine) as gen:
            if gen is None:
                 print(f"WARNING [vrijeme_driver.py]: prove() vratio None za cilj '{preporuka_goal_syntax}'. Nijedno pravilo nije zadovoljeno.", file=sys.stderr)
            else:
                for vars_found, plan in gen:
                    item_to_carry_from_goal = vars_found.get('sta_poneti')
                    print(f"DEBUG [vrijeme_driver.py]: Pronađena preporuka iz pravila: {item_to_carry_from_goal}", file=sys.stderr)
                    break
    except Exception as e_prove:
        print(f"Greška prilikom izvršavanja prove() za cilj '{preporuka_goal_syntax}': {e_prove}", file=sys.stderr)
        krb_traceback.print_exc(file=sys.stderr)

    if item_to_carry_from_goal == "kabanicu":
        final_recommendation = "Kabanicu"
    elif item_to_carry_from_goal == "kisobran":
        final_recommendation = "Kišobran"
    elif item_to_carry_from_goal == "nista":
        final_recommendation = "Ništa"
    else:
        if item_to_carry_from_goal is not None:
            print(f"INFO [vrijeme_driver.py]: Pravilo je vratilo neočekivanu vrijednost '{item_to_carry_from_goal}'. Podrazumijevano 'Ništa'.", file=sys.stderr)
        else:
            print(f"INFO [vrijeme_driver.py]: Nijedno pravilo nije odredilo šta ponijeti (cilj nije uspio ili vratio None). Podrazumijevano 'Ništa'.", file=sys.stderr)
        final_recommendation = "Ništa"
    return final_recommendation

def testiraj_sistem(kb_path_from_notebook_arg, pada_kisa_cinjenica, puse_vjetar_cinjenica):
    global _initialized_kb_path, engine
    
    current_kb_abs = os.path.abspath(str(kb_path_from_notebook_arg))
    
    compiled_krb_to_delete = os.path.join(current_kb_abs, 'compiled_krb')
    if os.path.isdir(compiled_krb_to_delete):
        try:
            shutil.rmtree(compiled_krb_to_delete)
            print(f"DEBUG [testiraj_sistem]: OBRISAN direktorij: {compiled_krb_to_delete}", file=sys.stderr)
        except Exception as e_rm:
            print(f"ERROR [testiraj_sistem]: Nije moguće obrisati {compiled_krb_to_delete}: {e_rm}. Nastavljam bez brisanja.", file=sys.stderr)
    else:
        print(f"DEBUG [testiraj_sistem]: Direktorij {compiled_krb_to_delete} nije pronađen za brisanje (očekivano za prvi put ili ako je prethodno brisanje bilo neuspješno).", file=sys.stderr)

    print(f"\n--- Testiranje sa: Kiša pada = {pada_kisa_cinjenica}, Vjetar puše = {puse_vjetar_cinjenica} ---")
    kfb_sadrzaj = f"""
pada_kisa({str(pada_kisa_cinjenica).lower()})
puse_vjetar({str(puse_vjetar_cinjenica).lower()})
""" 
    kfb_fajl_putanja = os.path.join(current_kb_abs, "vrijeme.kfb")
    try:
        with open(kfb_fajl_putanja, "w") as f:
            f.write(kfb_sadrzaj.strip())
        print(f"DEBUG [vrijeme_driver.py]: Činjenice zapisane u {kfb_fajl_putanja} PRIJE inicijalizacije engine-a.", file=sys.stderr)
    except Exception as e_write_kfb:
        print(f"Greška prilikom pisanja u '{kfb_fajl_putanja}': {e_write_kfb}")
        return

    if not initialize_engine_if_needed(current_kb_abs): 
        print("Preporuka: Greška engine-a (nije inicijalizovan)") 
        return 
    
    if engine:
        print("DEBUG [vrijeme_driver.py]: Resetovanje PyKE engine-a (iako je vjerovatno već svjež).", file=sys.stderr)
        engine.reset() 
    else:
        print("ERROR [vrijeme_driver.py]: Engine nije dostupan za resetovanje nakon inicijalizacije.", file=sys.stderr)
        return

    if _initialized_kb_path is None:
        print("ERROR [testiraj_sistem]: _initialized_kb_path nije postavljen nakon inicijalizacije engine-a.", file=sys.stderr)
        return

    preporuka = dobij_preporuku()
    
    print(f"Preporuka: Trebate ponijeti -> {preporuka}")

if __name__ == "__main__":
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("Pokretanje testova direktno iz vrijeme_driver.py...")
    testiraj_sistem(current_script_dir, True, True)
    testiraj_sistem(current_script_dir, True, False)
    testiraj_sistem(current_script_dir, False, False)
    testiraj_sistem(current_script_dir, False, True)