# $Id: driver.py 6de8ee4e7d2d 2010-03-29 mtnyogi $
# coding=utf-8
# 
# Copyright © 2007-2008 Bruce Frederiksen
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

'''
    This example shows how people are related.  The primary data (facts) that
    are used to figure everything out are in family.kfb.

    There are four independent rule bases that all do the same thing.  The
    fc_example rule base only uses forward-chaining rules.  The bc_example
    rule base only uses backward-chaining rules.  The bc2_example rule base
    also only uses backward-chaining rules, but with a few optimizations that
    make it run 100 times faster than bc_example.  And the example rule base
    uses all three (though it's a poor use of plans).

    Once the pyke engine is created, all the rule bases loaded and all the
    primary data established as universal facts; there are five functions
    that can be used to run each of the three rule bases: fc_test, bc_test,
    bc2_test, test and general.
'''


import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal, contexts, pattern

# Compile and load .krb files in same directory that I'm in (recursively).
engine = knowledge_engine.engine(__file__)

# Goal for fc_test (Task 1.2)
fc_goal = goal.compile('family.how_related($person1, $person2, $relationship)')

# ---------- MODIFIED fc_test FOR ZADATAK 1.2 ----------
def fc_test(person1_arg, person2_arg):
    '''
        This function runs the forward-chaining example (fc_example.krb)
        and finds the relationship between person1_arg and person2_arg.
    '''
    engine.reset()
    print(f"Activating forward-chaining rules from 'fc_example' for fc_test ({person1_arg}, {person2_arg})...")
    start_time_activate = time.time()
    engine.activate('fc_example')
    activation_time = time.time() - start_time_activate
    print(f"Activation time: {activation_time:.2f}s")

    print(f"\nDoing proof for the relationship between {person1_arg} and {person2_arg}:")
    found_relationship = False
    prove_start_time = time.time()
    with fc_goal.prove(engine, person1=person1_arg, person2=person2_arg) as gen:
        for vars_found, plan in gen:
            relationship = vars_found.get('relationship')
            if relationship:
                print(f"{person1_arg} and {person2_arg} are related as: {relationship}")
                found_relationship = True
    prove_time = time.time() - prove_start_time
    if not found_relationship:
        print(f"No specific relationship found by 'how_related' between {person1_arg} and {person2_arg}.")
    print("\ndone with fc_test")
    print(f"Proof time for this pair: {prove_time:.2f}s")
# ---------- END OF fc_test MODIFICATION ----------


# ---------- FUNCTION FOR ZADATAK 1.3 ----------
brothers_of_person_goal = goal.compile('family.brother_of($person_is_brother, $their_sibling)')

def find_brothers_test(given_person_name):
    '''
    Finds all persons for whom 'given_person_name' is a brother.
    '''
    engine.reset()
    print(f"\nActivating forward-chaining rules from 'fc_example' for find_brothers_test ({given_person_name})...")
    start_time_activate = time.time()
    engine.activate('fc_example') 
    activation_time = time.time() - start_time_activate
    print(f"Activation time: {activation_time:.2f}s")

    print(f"\nFinding siblings for whom '{given_person_name}' is a brother:")
    found_any_siblings = False
    prove_start_time = time.time()
    with brothers_of_person_goal.prove(engine, person_is_brother=given_person_name) as gen:
        for vars_found, plan in gen:
            sibling = vars_found.get('their_sibling')
            if sibling:
                print(f"- {given_person_name} is a brother to: {sibling}")
                found_any_siblings = True
    prove_time = time.time() - prove_start_time
    if not found_any_siblings:
        print(f"No one found for whom '{given_person_name}' is a brother (either '{given_person_name}' is not male, has no siblings defined by rules, or the person does not exist).")
    print("\ndone with find_brothers_test")
    print(f"Proof time for this query: {prove_time:.2f}s")
# ---------- END OF find_brothers_test FUNCTION ----------


# ---------- NEW FUNCTION FOR ZADATAK 1.4 ----------
sisters_of_person_goal = goal.compile('family.sister_of($person_is_sister, $their_sibling)')

def find_sisters_test(given_person_name):
    '''
    Finds all persons for whom 'given_person_name' is a sister.
    '''
    engine.reset()
    print(f"\nActivating forward-chaining rules from 'fc_example' for find_sisters_test ({given_person_name})...")
    start_time_activate = time.time()
    engine.activate('fc_example')
    activation_time = time.time() - start_time_activate
    print(f"Activation time: {activation_time:.2f}s")

    print(f"\nFinding siblings for whom '{given_person_name}' is a sister:")
    found_any_siblings = False
    prove_start_time = time.time()
    with sisters_of_person_goal.prove(engine, person_is_sister=given_person_name) as gen:
        for vars_found, plan in gen:
            sibling = vars_found.get('their_sibling')
            if sibling:
                print(f"- {given_person_name} is a sister to: {sibling}")
                found_any_siblings = True
    prove_time = time.time() - prove_start_time
    if not found_any_siblings:
        print(f"No one found for whom '{given_person_name}' is a sister (either '{given_person_name}' is not female, has no siblings defined by rules, or the person does not exist).")
    print("\ndone with find_sisters_test")
    print(f"Proof time for this query: {prove_time:.2f}s")
# ---------- END OF find_sisters_test FUNCTION ----------

# ---------- NEW FUNCTION FOR ZADATAK 1.e (Task 1.5) ----------
def find_all_siblings_for_person_test(given_person_name):
    '''
    Finds all persons for whom 'given_person_name' is either a brother or a sister.
    '''
    engine.reset()
    
    print(f"\nActivating forward-chaining rules from 'fc_example' for find_all_siblings_for_person_test ({given_person_name})...")
    start_time_activate = time.time()
    engine.activate('fc_example') # Ensures all rules, including gender, brother_of, sister_of, are processed
    activation_time = time.time() - start_time_activate
    print(f"Activation time: {activation_time:.2f}s")

    print(f"\nFinding all persons for whom '{given_person_name}' is a sibling (brother or sister):")
    
    found_any = False

    # --- Check if given_person_name is a brother to anyone ---
    # (Uses brothers_of_person_goal = goal.compile('family.brother_of($person_is_brother, $their_sibling)'))
    print(f"  Checking if '{given_person_name}' is a brother to anyone...")
    try:
        with brothers_of_person_goal.prove(engine, person_is_brother=given_person_name) as gen:
            for vars_found, plan in gen:
                sibling = vars_found.get('their_sibling')
                if sibling:
                    print(f"  - {given_person_name} is a BROTHER to: {sibling}")
                    found_any = True
    except Exception as e:
        print(f"    Error during brother check: {e}")


    # --- Check if given_person_name is a sister to anyone ---
    # (Uses sisters_of_person_goal = goal.compile('family.sister_of($person_is_sister, $their_sibling)'))
    print(f"  Checking if '{given_person_name}' is a sister to anyone...")
    try:
        with sisters_of_person_goal.prove(engine, person_is_sister=given_person_name) as gen:
            for vars_found, plan in gen:
                sibling = vars_found.get('their_sibling')
                if sibling:
                    print(f"  - {given_person_name} is a SISTER to: {sibling}")
                    found_any = True
    except Exception as e:
        print(f"    Error during sister check: {e}")

    if not found_any:
        print(f"'{given_person_name}' was not found to be a brother or a sister to anyone based on the defined rules.")
    
    print("\ndone with find_all_siblings_for_person_test")
    # engine.print_stats() # Optional
# ---------- END OF find_all_siblings_for_person_test FUNCTION ----------

# ---------- NEW FUNCTION FOR ZADATAK 1.f (Task 1.6) ----------
def check_if_specific_siblings_test(person1_name, person2_name):
    '''
    Checks if person1_name and person2_name are siblings (one is a brother or sister to the other).
    Prints the relationship if found, otherwise prints nothing.
    '''
    engine.reset()
    
    # print(f"\nActivating forward-chaining rules for check_if_specific_siblings_test ({person1_name}, {person2_name})...")
    # Activation can be done once if facts don't change, or here for isolated test.
    # For this specific task, let's assume activation happens and we just prove.
    # If this is the only function called after loading driver, uncomment the activate line.
    # If other tests that call activate run first, this might not be needed again.
    # To be safe for an isolated test:
    engine.activate('fc_example') 
    
    # print(f"\nChecking if '{person1_name}' and '{person2_name}' are siblings...")
    
    relationship_found_and_printed = False

    # Check 1: Is person1_name a BROTHER to person2_name?
    # Uses: brothers_of_person_goal = goal.compile('family.brother_of($person_is_brother, $their_sibling)')
    try:
        with brothers_of_person_goal.prove(engine, person_is_brother=person1_name, their_sibling=person2_name) as gen:
            for vars_found, plan in gen: # Should only iterate once if specific pair matches
                print(f"{person1_name} is a BROTHER to {person2_name}.")
                relationship_found_and_printed = True
                break # Found one relationship type, that's enough
        if relationship_found_and_printed: return
    except Exception as e:
        # print(f"    Error during brother check (1): {e}")
        pass

    # Check 2: Is person1_name a SISTER to person2_name?
    # Uses: sisters_of_person_goal = goal.compile('family.sister_of($person_is_sister, $their_sibling)')
    try:
        with sisters_of_person_goal.prove(engine, person_is_sister=person1_name, their_sibling=person2_name) as gen:
            for vars_found, plan in gen:
                print(f"{person1_name} is a SISTER to {person2_name}.")
                relationship_found_and_printed = True
                break
        if relationship_found_and_printed: return
    except Exception as e:
        # print(f"    Error during sister check (1): {e}")
        pass
        
    # If no direct relationship from P1 to P2, check P2 to P1 for completeness,
    # although good brother_of/sister_of rules should make this redundant if they assert both directions
    # or if our goal was more general like family.siblings(P1, P2, type1, type2).
    # However, the task implies checking if one IS a brother/sister TO the other.
    # Our brother_of(X,Y) means X is brother TO Y.
    # So the above two checks are sufficient if the P1 is the one *being* the brother/sister.

    # The task phrasing "ukoliko se te dvije osobe brat/sestra sistem treba da to da i ispiše"
    # could mean "if A is brother/sister of B OR B is brother/sister of A".
    # Let's add the reverse checks to be thorough for that interpretation.

    # Check 3: Is person2_name a BROTHER to person1_name?
    try:
        with brothers_of_person_goal.prove(engine, person_is_brother=person2_name, their_sibling=person1_name) as gen:
            for vars_found, plan in gen:
                print(f"{person2_name} is a BROTHER to {person1_name}.")
                relationship_found_and_printed = True
                break
        if relationship_found_and_printed: return
    except Exception as e:
        # print(f"    Error during brother check (2): {e}")
        pass

    # Check 4: Is person2_name a SISTER to person1_name?
    try:
        with sisters_of_person_goal.prove(engine, person_is_sister=person2_name, their_sibling=person1_name) as gen:
            for vars_found, plan in gen:
                print(f"{person2_name} is a SISTER to {person1_name}.")
                relationship_found_and_printed = True
                break
        if relationship_found_and_printed: return
    except Exception as e:
        # print(f"    Error during sister check (2): {e}")
        pass

    # If relationship_found_and_printed is still False, nothing is printed, as per task requirement.
    # print("\ndone with check_if_specific_siblings_test") # Optional: for debugging completion
# ---------- END OF check_if_specific_siblings_test FUNCTION ----------

# ---------- NEW FUNCTION FOR ZADATAK 1.g (Task 1.7) Grandparents ----------
# The fact asserted by fc_example.krb is:
# family.child_parent($grandchild, $grandparent, (grand), $gp_actual_role_to_parent, $gc_actual_role_to_parent)
# We want to find $grandparent given $grandchild.
find_grandparents_goal = goal.compile(
    'family.child_parent($grandchild_name, $grandparent_found, (grand), $gp_role, $gc_role)'
)

def find_grandparents_test(given_grandchild_name):
    '''
    Finds all grandparents of the 'given_grandchild_name'.
    '''
    engine.reset()
    
    # print(f"\nActivating forward-chaining rules for find_grandparents_test ({given_grandchild_name})...")
    # Activation needs to happen to assert the (grand) level child_parent facts.
    # If called after other tests that already activated, this might be redundant but ensures facts are present.
    engine.activate('fc_example') 
    # activation_time = time.time() - start_time_activate # Optional timing
    # print(f"Activation time: {activation_time:.2f}s")

    print(f"\nFinding grandparents of '{given_grandchild_name}':")
    
    found_any_gp = False
    prove_start_time = time.time()
    with find_grandparents_goal.prove(engine, grandchild_name=given_grandchild_name) as gen:
        for vars_found, plan in gen:
            grandparent = vars_found.get('grandparent_found')
            # gp_role = vars_found.get('gp_role') # e.g., 'father' or 'mother' (role of GP to intermediate parent)
            # gc_role = vars_found.get('gc_role') # e.g., 'son' or 'daughter' (role of GC to intermediate parent)
            if grandparent:
                # We can determine if it's grandfather or grandmother if we also have gender facts for the grandparent
                # For now, let's just list them as grandparents.
                print(f"- {grandparent} is a grandparent of {given_grandchild_name}.")
                # To be more specific (grandfather/grandmother), we'd need another prove call for family.male($grandparent) or family.female($grandparent)
                found_any_gp = True
    
    prove_time = time.time() - prove_start_time

    if not found_any_gp:
        print(f"No grandparents found for '{given_grandchild_name}' based on the rules.")
    
    print("\ndone with find_grandparents_test")
    print(f"Proof time for this query: {prove_time:.2f}s")
# ---------- END OF find_grandparents_test FUNCTION ----------



# --- Original bc_test, bc2_test, test, general, make_pattern functions follow ---
# --- NO CHANGES NEEDED TO THESE FOR THESE TASKS ---

def bc_test(person1 = 'bruce'):
    engine.reset()
    start_time = time.time()
    engine.activate('bc_example')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time
    print("doing proof")
    try:
        with engine.prove_goal(
               'bc_example.how_related($person1, $person2, $relationship)',
               person1=person1) \
          as gen:
            for vars, plan in gen:
                print("%s, %s are %s" % \
                        (person1, vars['person2'], vars['relationship']))
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print()
    print("done")
    engine.print_stats()
    print("bc time %.2f, %.0f goals/sec" % \
          (prove_time, engine.get_kb('bc_example').num_prove_calls / prove_time))

def bc2_test(person1 = 'bruce'):
    engine.reset()
    start_time = time.time()
    engine.activate('bc2_example')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time
    print("doing proof")
    try:
        with engine.prove_goal(
               'bc2_example.how_related($person1, $person2, $relationship)',
               person1=person1) \
          as gen:
            for vars, plan in gen:
                print("%s, %s are %s" % \
                        (person1, vars['person2'], vars['relationship']))
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print()
    print("done")
    engine.print_stats()
    print("bc time %.2f, %.0f goals/sec" % \
          (prove_time,
           engine.get_kb('bc2_example').num_prove_calls / prove_time))

def test(person1 = 'bruce'):
    engine.reset()
    start_time = time.time()
    engine.activate('example') # This function uses 'example.krb'
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time
    print("doing proof")
    try:
        with engine.prove_goal(
               'example.how_related($person1, $person2)', # Goal from 'example.krb'
               person1=person1) \
          as gen:
            for vars, plan in gen:
                print("%s, %s are %s" % (person1, vars['person2'], plan()))
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print()
    print("done")
    engine.print_stats()
    print("fc time %.2f, %.0f asserts/sec" % \
          (fc_time, engine.get_kb('family').get_stats()[2] / fc_time))
    print("bc time %.2f, %.0f goals/sec" % \
          (prove_time, engine.get_kb('example').num_prove_calls / prove_time))
    print("total time %.2f" % (fc_time + prove_time))

def general(person1 = None, person2 = None, relationship = None):
    engine.reset()
    start_time = time.time()
    engine.activate('bc2_example')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time
    print("doing proof")
    args = {}
    if person1: args['person1'] = person1
    if person2: args['person2'] = person2
    if relationship: args['relationship'] = relationship
    try:
        with engine.prove_goal(
               'bc2_example.how_related($person1, $person2, $relationship)',
               **args
        ) as gen:
            for vars, plan in gen:
                print("%s, %s are %s" % (vars['person1'],
                                         vars['person2'],
                                         vars['relationship']))
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print()
    print("done")
    engine.print_stats()
    print("bc time %.2f, %.0f goals/sec" % \
          (prove_time,
           engine.get_kb('bc2_example').num_prove_calls / prove_time))

import types

def make_pattern(x):
    if isinstance(x, str):
        if x[0] == '$': return contexts.variable(x[1:])
        return pattern.pattern_literal(x)
    if isinstance(x, (tuple, list)):
        return pattern.pattern_tuple(tuple(make_pattern(element)
                                             for element in x))
    return pattern.pattern_literal(x)