# fc_example_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def son_of(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(4).as_data(context),
                        rule.pattern(5).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def daughter_of(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'daughter_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(4).as_data(context),
                        rule.pattern(5).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def infer_male(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('family', 'male',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def infer_female(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'daughter_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if print("DEBUG infer_female: Found daughter_of for", context.lookup_data('person')) :
          engine.assert_('family', 'female',
                         (rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def debug_is_norma_female_and_daughter(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'female', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'daughter_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if print("EXTREME DEBUG: YES, 'norma' is female AND daughter_of parents:", context.lookup_data('f'), context.lookup_data('m')):
              engine.assert_('family', 'norma_debug_passed',
                             ()),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def brothers(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'son_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('brother1') != context.lookup_data('brother2'):
              engine.assert_('family', 'siblings',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def sisters(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'daughter_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'daughter_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('sister1') != context.lookup_data('sister2'):
              engine.assert_('family', 'siblings',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def brother_and_sister(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'daughter_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('family', 'siblings',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),
                            rule.pattern(3).as_data(context),)),
            engine.assert_('family', 'siblings',
                           (rule.pattern(1).as_data(context),
                            rule.pattern(0).as_data(context),
                            rule.pattern(3).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def define_brother_of_sibling_son(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'male', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'son_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('family', 'son_of', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                if context.lookup_data('person_x') != context.lookup_data('person_y'):
                  engine.assert_('family', 'brother_of',
                                 (rule.pattern(0).as_data(context),
                                  rule.pattern(1).as_data(context),)),
                  rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def define_brother_of_sibling_daughter(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'male', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'son_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('family', 'daughter_of', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('family', 'brother_of',
                               (rule.pattern(0).as_data(context),
                                rule.pattern(1).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def define_sister_of_sibling_son(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'female', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'daughter_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if print("DEBUG sister_of (step A): Matched female_person=", context.lookup_data('person_x'), " who is daughter_of f=", context.lookup_data('f'), ", m=", context.lookup_data('m')):
              with knowledge_base.Gen_once if index == 2 \
                       else engine.lookup('family', 'son_of', context,
                                          rule.foreach_patterns(2)) \
                as gen_2:
                for dummy in gen_2:
                  if print("DEBUG sister_of_son (step B-SUCCESS): AND person_y=", context.lookup_data('person_y'), " is son of same parents f=", context.lookup_data('f'), ", m=", context.lookup_data('m')):
                    engine.assert_('family', 'sister_of',
                                   (rule.pattern(0).as_data(context),
                                    rule.pattern(1).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def define_sister_of_sibling_daughter(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'female', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'daughter_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if print("DEBUG sister_of (step A): Matched female_person=", context.lookup_data('person_x'), " who is daughter_of f=", context.lookup_data('f'), ", m=", context.lookup_data('m')):
              with knowledge_base.Gen_once if index == 2 \
                       else engine.lookup('family', 'daughter_of', context,
                                          rule.foreach_patterns(2)) \
                as gen_2:
                for dummy in gen_2:
                  if print("DEBUG sister_of_daughter (step B): AND person_y=", context.lookup_data('person_y'), " is daughter of same parents f=", context.lookup_data('f'), ", m=", context.lookup_data('m')):
                    if context.lookup_data('person_x') != context.lookup_data('person_y'):
                      if print("DEBUG sister_of_daughter (step C-SUCCESS): AND they are different people ($person_x != $person_y)"):
                        engine.assert_('family', 'sister_of',
                                       (rule.pattern(0).as_data(context),
                                        rule.pattern(1).as_data(context),)),
                        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def facts_for_bc_rules(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    engine.assert_('family', 'as_au',
                   (rule.pattern(0).as_data(context),
                    rule.pattern(1).as_data(context),)),
    engine.assert_('family', 'as_au',
                   (rule.pattern(2).as_data(context),
                    rule.pattern(3).as_data(context),)),
    engine.assert_('family', 'as_nn',
                   (rule.pattern(4).as_data(context),
                    rule.pattern(5).as_data(context),)),
    engine.assert_('family', 'as_nn',
                   (rule.pattern(6).as_data(context),
                    rule.pattern(7).as_data(context),)),
    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def niece_or_nephew_and_aunt_or_uncle(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'siblings', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('family', 'as_au', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('family', 'as_nn', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    mark4 = context.mark(True)
                    if rule.pattern(0).match_data(context, context,
                            ('great',) * len(context.lookup_data('depth'))):
                      context.end_save_all_undo()
                      engine.assert_('family', 'nn_au',
                                     (rule.pattern(1).as_data(context),
                                      rule.pattern(2).as_data(context),
                                      rule.pattern(0).as_data(context),
                                      rule.pattern(3).as_data(context),
                                      rule.pattern(4).as_data(context),)),
                      rule.rule_base.num_fc_rules_triggered += 1
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark4)
  finally:
    context.done()

def parent_and_child(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),
                        rule.pattern(4).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def grand_parent_and_child(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'child_parent', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('family', 'child_parent',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),
                            rule.pattern(3).as_data(context),
                            rule.pattern(4).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def great_grand_parent_and_child(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'child_parent', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('family', 'child_parent',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),
                            rule.pattern(3).as_data(context),
                            rule.pattern(4).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def first_cousins(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'siblings', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('family', 'child_parent', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('family', 'cousins',
                               (rule.pattern(0).as_data(context),
                                rule.pattern(1).as_data(context),
                                rule.pattern(2).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def nth_cousins(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'cousins', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('family', 'child_parent', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                mark3 = context.mark(True)
                if rule.pattern(0).match_data(context, context,
                        context.lookup_data('n') + 1):
                  context.end_save_all_undo()
                  engine.assert_('family', 'cousins',
                                 (rule.pattern(1).as_data(context),
                                  rule.pattern(2).as_data(context),
                                  rule.pattern(0).as_data(context),)),
                  rule.rule_base.num_fc_rules_triggered += 1
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
  finally:
    context.done()

def how_related_child_parent(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
          context.end_save_all_undo()
          engine.assert_('family', 'how_related',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),
                          rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
  finally:
    context.done()

def how_related_parent_child(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
          context.end_save_all_undo()
          engine.assert_('family', 'how_related',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),
                          rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
  finally:
    context.done()

def how_related_siblings(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'siblings', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('family', 'how_related',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def how_related_nn_au(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'nn_au', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
          context.end_save_all_undo()
          engine.assert_('family', 'how_related',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),
                          rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
  finally:
    context.done()

def how_related_au_nn(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'nn_au', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
          context.end_save_all_undo()
          engine.assert_('family', 'how_related',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),
                          rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
  finally:
    context.done()

def how_related_cousins(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'cousins', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                nth(context.lookup_data('n'))):
          context.end_save_all_undo()
          engine.assert_('family', 'how_related',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),
                          rule.pattern(3).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
  finally:
    context.done()

def how_related_removed_cousins(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'cousins', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            mark2 = context.mark(True)
            if rule.pattern(0).match_data(context, context,
                    nth(context.lookup_data('n'))):
              context.end_save_all_undo()
              mark3 = context.mark(True)
              if rule.pattern(1).match_data(context, context,
                      len(context.lookup_data('grand')) + 1):
                context.end_save_all_undo()
                engine.assert_('family', 'how_related',
                               (rule.pattern(2).as_data(context),
                                rule.pattern(3).as_data(context),
                                rule.pattern(4).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
              else: context.end_save_all_undo()
              context.undo_to_mark(mark3)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
  finally:
    context.done()

def how_related_cousins_removed(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'cousins', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'child_parent', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            mark2 = context.mark(True)
            if rule.pattern(0).match_data(context, context,
                    nth(context.lookup_data('n'))):
              context.end_save_all_undo()
              mark3 = context.mark(True)
              if rule.pattern(1).match_data(context, context,
                      len(context.lookup_data('grand')) + 1):
                context.end_save_all_undo()
                engine.assert_('family', 'how_related',
                               (rule.pattern(2).as_data(context),
                                rule.pattern(3).as_data(context),
                                rule.pattern(4).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
              else: context.end_save_all_undo()
              context.undo_to_mark(mark3)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_example')
  
  fc_rule.fc_rule('son_of', This_rule_base, son_of,
    (('family', 'son_of',
      (contexts.variable('child'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('father'),
     pattern.pattern_literal('father'),
     pattern.pattern_literal('son'),
     contexts.variable('mother'),
     pattern.pattern_literal('mother'),))
  
  fc_rule.fc_rule('daughter_of', This_rule_base, daughter_of,
    (('family', 'daughter_of',
      (contexts.variable('child'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('father'),
     pattern.pattern_literal('father'),
     pattern.pattern_literal('daughter'),
     contexts.variable('mother'),
     pattern.pattern_literal('mother'),))
  
  fc_rule.fc_rule('infer_male', This_rule_base, infer_male,
    (('family', 'son_of',
      (contexts.variable('person'),
       contexts.anonymous('_father'),
       contexts.anonymous('_mother'),),
      False),),
    (contexts.variable('person'),))
  
  fc_rule.fc_rule('infer_female', This_rule_base, infer_female,
    (('family', 'daughter_of',
      (contexts.variable('person'),
       contexts.anonymous('_father'),
       contexts.anonymous('_mother'),),
      False),),
    (contexts.variable('person'),))
  
  fc_rule.fc_rule('debug_is_norma_female_and_daughter', This_rule_base, debug_is_norma_female_and_daughter,
    (('family', 'female',
      (pattern.pattern_literal('norma'),),
      False),
     ('family', 'daughter_of',
      (pattern.pattern_literal('norma'),
       contexts.variable('f'),
       contexts.variable('m'),),
      False),),
    ())
  
  fc_rule.fc_rule('brothers', This_rule_base, brothers,
    (('family', 'son_of',
      (contexts.variable('brother1'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'son_of',
      (contexts.variable('brother2'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('brother1'),
     contexts.variable('brother2'),
     pattern.pattern_literal('brother'),))
  
  fc_rule.fc_rule('sisters', This_rule_base, sisters,
    (('family', 'daughter_of',
      (contexts.variable('sister1'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'daughter_of',
      (contexts.variable('sister2'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('sister1'),
     contexts.variable('sister2'),
     pattern.pattern_literal('sister'),))
  
  fc_rule.fc_rule('brother_and_sister', This_rule_base, brother_and_sister,
    (('family', 'son_of',
      (contexts.variable('brother'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'daughter_of',
      (contexts.variable('sister'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('brother'),
     contexts.variable('sister'),
     pattern.pattern_literal('sister'),
     pattern.pattern_literal('brother'),))
  
  fc_rule.fc_rule('define_brother_of_sibling_son', This_rule_base, define_brother_of_sibling_son,
    (('family', 'male',
      (contexts.variable('person_x'),),
      False),
     ('family', 'son_of',
      (contexts.variable('person_x'),
       contexts.variable('f'),
       contexts.variable('m'),),
      False),
     ('family', 'son_of',
      (contexts.variable('person_y'),
       contexts.variable('f'),
       contexts.variable('m'),),
      False),),
    (contexts.variable('person_x'),
     contexts.variable('person_y'),))
  
  fc_rule.fc_rule('define_brother_of_sibling_daughter', This_rule_base, define_brother_of_sibling_daughter,
    (('family', 'male',
      (contexts.variable('person_x'),),
      False),
     ('family', 'son_of',
      (contexts.variable('person_x'),
       contexts.variable('f'),
       contexts.variable('m'),),
      False),
     ('family', 'daughter_of',
      (contexts.variable('person_y'),
       contexts.variable('f'),
       contexts.variable('m'),),
      False),),
    (contexts.variable('person_x'),
     contexts.variable('person_y'),))
  
  fc_rule.fc_rule('define_sister_of_sibling_son', This_rule_base, define_sister_of_sibling_son,
    (('family', 'female',
      (contexts.variable('person_x'),),
      False),
     ('family', 'daughter_of',
      (contexts.variable('person_x'),
       contexts.variable('f'),
       contexts.variable('m'),),
      False),
     ('family', 'son_of',
      (contexts.variable('person_y'),
       contexts.variable('f'),
       contexts.variable('m'),),
      False),),
    (contexts.variable('person_x'),
     contexts.variable('person_y'),))
  
  fc_rule.fc_rule('define_sister_of_sibling_daughter', This_rule_base, define_sister_of_sibling_daughter,
    (('family', 'female',
      (contexts.variable('person_x'),),
      False),
     ('family', 'daughter_of',
      (contexts.variable('person_x'),
       contexts.variable('f'),
       contexts.variable('m'),),
      False),
     ('family', 'daughter_of',
      (contexts.variable('person_y'),
       contexts.variable('f'),
       contexts.variable('m'),),
      False),),
    (contexts.variable('person_x'),
     contexts.variable('person_y'),))
  
  fc_rule.fc_rule('facts_for_bc_rules', This_rule_base, facts_for_bc_rules,
    (),
    (pattern.pattern_literal('brother'),
     pattern.pattern_literal('uncle'),
     pattern.pattern_literal('sister'),
     pattern.pattern_literal('aunt'),
     pattern.pattern_literal('son'),
     pattern.pattern_literal('nephew'),
     pattern.pattern_literal('daughter'),
     pattern.pattern_literal('niece'),))
  
  fc_rule.fc_rule('niece_or_nephew_and_aunt_or_uncle', This_rule_base, niece_or_nephew_and_aunt_or_uncle,
    (('family', 'child_parent',
      (contexts.variable('nn'),
       contexts.variable('parent'),
       contexts.variable('depth'),
       contexts.anonymous('_'),
       contexts.variable('child_type'),),
      False),
     ('family', 'siblings',
      (contexts.variable('parent'),
       contexts.variable('au'),
       contexts.variable('sibling_type'),
       contexts.anonymous('_'),),
      False),
     ('family', 'as_au',
      (contexts.variable('sibling_type'),
       contexts.variable('au_type'),),
      False),
     ('family', 'as_nn',
      (contexts.variable('child_type'),
       contexts.variable('nn_type'),),
      False),),
    (contexts.variable('greats'),
     contexts.variable('nn'),
     contexts.variable('au'),
     contexts.variable('au_type'),
     contexts.variable('nn_type'),))
  
  fc_rule.fc_rule('parent_and_child', This_rule_base, parent_and_child,
    (('family', 'child_parent',
      (contexts.variable('child'),
       contexts.variable('parent'),
       contexts.variable('parent_type'),
       contexts.variable('child_type'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('parent'),
     pattern.pattern_literal(()),
     contexts.variable('parent_type'),
     contexts.variable('child_type'),))
  
  fc_rule.fc_rule('grand_parent_and_child', This_rule_base, grand_parent_and_child,
    (('family', 'child_parent',
      (contexts.variable('child'),
       contexts.variable('parent'),
       contexts.anonymous('_'),
       contexts.variable('child_type'),),
      False),
     ('family', 'child_parent',
      (contexts.variable('parent'),
       contexts.variable('grand_parent'),
       contexts.variable('parent_type'),
       contexts.anonymous('_'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('grand_parent'),
     pattern.pattern_literal(('grand',)),
     contexts.variable('parent_type'),
     contexts.variable('child_type'),))
  
  fc_rule.fc_rule('great_grand_parent_and_child', This_rule_base, great_grand_parent_and_child,
    (('family', 'child_parent',
      (contexts.variable('child'),
       contexts.variable('grand_child'),
       contexts.anonymous('_'),
       contexts.variable('child_type'),),
      False),
     ('family', 'child_parent',
      (contexts.variable('grand_child'),
       contexts.variable('grand_parent'),
       pattern.pattern_tuple((contexts.variable('a'),), contexts.variable('b')),
       contexts.variable('parent_type'),
       contexts.anonymous('_'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('grand_parent'),
     pattern.pattern_tuple((pattern.pattern_literal('great'), contexts.variable('a'),), contexts.variable('b')),
     contexts.variable('parent_type'),
     contexts.variable('child_type'),))
  
  fc_rule.fc_rule('first_cousins', This_rule_base, first_cousins,
    (('family', 'child_parent',
      (contexts.variable('cousin1'),
       contexts.variable('sibling1'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('family', 'siblings',
      (contexts.variable('sibling1'),
       contexts.variable('sibling2'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('family', 'child_parent',
      (contexts.variable('cousin2'),
       contexts.variable('sibling2'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (contexts.variable('cousin1'),
     contexts.variable('cousin2'),
     pattern.pattern_literal(1),))
  
  fc_rule.fc_rule('nth_cousins', This_rule_base, nth_cousins,
    (('family', 'child_parent',
      (contexts.variable('next_cousin1'),
       contexts.variable('cousin1'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('family', 'cousins',
      (contexts.variable('cousin1'),
       contexts.variable('cousin2'),
       contexts.variable('n'),),
      False),
     ('family', 'child_parent',
      (contexts.variable('next_cousin2'),
       contexts.variable('cousin2'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (contexts.variable('next_n'),
     contexts.variable('next_cousin1'),
     contexts.variable('next_cousin2'),))
  
  fc_rule.fc_rule('how_related_child_parent', This_rule_base, how_related_child_parent,
    (('family', 'child_parent',
      (contexts.variable('person1'),
       contexts.variable('person2'),
       contexts.variable('prefix'),
       contexts.variable('p2_type'),
       contexts.variable('p1_type'),),
      False),),
    (contexts.variable('relationship'),
     contexts.variable('person1'),
     contexts.variable('person2'),))
  
  fc_rule.fc_rule('how_related_parent_child', This_rule_base, how_related_parent_child,
    (('family', 'child_parent',
      (contexts.variable('person2'),
       contexts.variable('person1'),
       contexts.variable('prefix'),
       contexts.variable('p1_type'),
       contexts.variable('p2_type'),),
      False),),
    (contexts.variable('relationship'),
     contexts.variable('person1'),
     contexts.variable('person2'),))
  
  fc_rule.fc_rule('how_related_siblings', This_rule_base, how_related_siblings,
    (('family', 'siblings',
      (contexts.variable('person1'),
       contexts.variable('person2'),
       contexts.variable('p2_type'),
       contexts.variable('p1_type'),),
      False),),
    (contexts.variable('person1'),
     contexts.variable('person2'),
     pattern.pattern_tuple((contexts.variable('p1_type'), contexts.variable('p2_type'),), None),))
  
  fc_rule.fc_rule('how_related_nn_au', This_rule_base, how_related_nn_au,
    (('family', 'nn_au',
      (contexts.variable('person1'),
       contexts.variable('person2'),
       contexts.variable('prefix'),
       contexts.variable('p2_type'),
       contexts.variable('p1_type'),),
      False),),
    (contexts.variable('relationship'),
     contexts.variable('person1'),
     contexts.variable('person2'),))
  
  fc_rule.fc_rule('how_related_au_nn', This_rule_base, how_related_au_nn,
    (('family', 'nn_au',
      (contexts.variable('person2'),
       contexts.variable('person1'),
       contexts.variable('prefix'),
       contexts.variable('p1_type'),
       contexts.variable('p2_type'),),
      False),),
    (contexts.variable('relationship'),
     contexts.variable('person1'),
     contexts.variable('person2'),))
  
  fc_rule.fc_rule('how_related_cousins', This_rule_base, how_related_cousins,
    (('family', 'cousins',
      (contexts.variable('cousin1'),
       contexts.variable('cousin2'),
       contexts.variable('n'),),
      False),),
    (contexts.variable('nth'),
     contexts.variable('cousin1'),
     contexts.variable('cousin2'),
     pattern.pattern_tuple((contexts.variable('nth'), pattern.pattern_literal('cousins'),), None),))
  
  fc_rule.fc_rule('how_related_removed_cousins', This_rule_base, how_related_removed_cousins,
    (('family', 'child_parent',
      (contexts.variable('removed_cousin1'),
       contexts.variable('cousin1'),
       contexts.variable('grand'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('family', 'cousins',
      (contexts.variable('cousin1'),
       contexts.variable('cousin2'),
       contexts.variable('n'),),
      False),),
    (contexts.variable('nth'),
     contexts.variable('r1'),
     contexts.variable('removed_cousin1'),
     contexts.variable('cousin2'),
     pattern.pattern_tuple((contexts.variable('nth'), pattern.pattern_literal('cousins'), contexts.variable('r1'), pattern.pattern_literal('removed'),), None),))
  
  fc_rule.fc_rule('how_related_cousins_removed', This_rule_base, how_related_cousins_removed,
    (('family', 'cousins',
      (contexts.variable('cousin1'),
       contexts.variable('cousin2'),
       contexts.variable('n'),),
      False),
     ('family', 'child_parent',
      (contexts.variable('removed_cousin2'),
       contexts.variable('cousin2'),
       contexts.variable('grand'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (contexts.variable('nth'),
     contexts.variable('r1'),
     contexts.variable('cousin1'),
     contexts.variable('removed_cousin2'),
     pattern.pattern_tuple((contexts.variable('nth'), pattern.pattern_literal('cousins'), contexts.variable('r1'), pattern.pattern_literal('removed'),), None),))

def nth(n):
    if n % 10 not in (1, 2, 3) or 10 < n % 100 < 20: return "%dth" % n
    if n % 10 == 1: return "%dst" % n
    if n % 10 == 2: return "%dnd" % n
    if n % 10 == 3: return "%drd" % n
def add_prefix(prefix, x, y):
    if not prefix: return (x, y)
    return (prefix + (x,), prefix + (y,))

Krb_filename = '..\\fc_example.krb'
Krb_lineno_map = (
    ((12, 16), (9, 9)),
    ((17, 21), (11, 11)),
    ((22, 26), (12, 12)),
    ((35, 39), (16, 16)),
    ((40, 44), (18, 18)),
    ((45, 49), (19, 19)),
    ((58, 62), (24, 24)),
    ((63, 64), (26, 26)),
    ((73, 77), (30, 30)),
    ((78, 78), (31, 31)),
    ((79, 80), (33, 33)),
    ((89, 93), (38, 38)),
    ((94, 98), (39, 39)),
    ((99, 99), (40, 40)),
    ((100, 101), (42, 42)),
    ((110, 114), (48, 48)),
    ((115, 119), (49, 49)),
    ((120, 120), (50, 50)),
    ((121, 125), (52, 52)),
    ((134, 138), (56, 56)),
    ((139, 143), (57, 57)),
    ((144, 144), (58, 58)),
    ((145, 149), (60, 60)),
    ((158, 162), (64, 64)),
    ((163, 167), (65, 65)),
    ((168, 172), (67, 67)),
    ((173, 177), (68, 68)),
    ((186, 190), (75, 75)),
    ((191, 195), (76, 76)),
    ((196, 200), (77, 77)),
    ((201, 201), (78, 78)),
    ((202, 204), (80, 80)),
    ((213, 217), (84, 84)),
    ((218, 222), (85, 85)),
    ((223, 227), (86, 86)),
    ((228, 230), (88, 88)),
    ((239, 243), (95, 95)),
    ((244, 248), (96, 96)),
    ((249, 249), (97, 97)),
    ((250, 254), (98, 98)),
    ((255, 255), (99, 99)),
    ((256, 258), (101, 101)),
    ((267, 271), (105, 105)),
    ((272, 276), (106, 106)),
    ((277, 277), (107, 107)),
    ((278, 282), (108, 108)),
    ((283, 283), (109, 109)),
    ((284, 284), (110, 110)),
    ((285, 285), (111, 111)),
    ((286, 288), (113, 113)),
    ((297, 299), (121, 121)),
    ((300, 302), (122, 122)),
    ((303, 305), (123, 123)),
    ((306, 308), (124, 124)),
    ((317, 321), (128, 128)),
    ((322, 326), (129, 129)),
    ((327, 331), (130, 130)),
    ((332, 336), (131, 131)),
    ((339, 339), (132, 132)),
    ((341, 346), (134, 134)),
    ((357, 361), (138, 138)),
    ((362, 367), (140, 140)),
    ((376, 380), (144, 144)),
    ((381, 385), (145, 145)),
    ((386, 391), (147, 148)),
    ((400, 404), (152, 152)),
    ((405, 409), (153, 154)),
    ((410, 415), (156, 157)),
    ((424, 428), (161, 161)),
    ((429, 433), (162, 162)),
    ((434, 438), (163, 163)),
    ((439, 442), (165, 165)),
    ((451, 455), (169, 169)),
    ((456, 460), (170, 170)),
    ((461, 465), (171, 171)),
    ((468, 468), (172, 172)),
    ((470, 473), (174, 174)),
    ((484, 488), (178, 178)),
    ((491, 491), (179, 179)),
    ((493, 496), (181, 181)),
    ((507, 511), (185, 185)),
    ((514, 514), (186, 186)),
    ((516, 519), (188, 188)),
    ((530, 534), (192, 192)),
    ((535, 538), (194, 194)),
    ((547, 551), (198, 198)),
    ((554, 554), (199, 199)),
    ((556, 559), (201, 201)),
    ((570, 574), (205, 205)),
    ((577, 577), (206, 206)),
    ((579, 582), (208, 208)),
    ((593, 597), (212, 212)),
    ((600, 600), (213, 213)),
    ((602, 605), (215, 215)),
    ((616, 620), (219, 219)),
    ((621, 625), (220, 220)),
    ((628, 628), (221, 221)),
    ((632, 632), (222, 222)),
    ((634, 637), (224, 225)),
    ((650, 654), (229, 229)),
    ((655, 659), (230, 230)),
    ((662, 662), (231, 231)),
    ((666, 666), (232, 232)),
    ((668, 671), (234, 235)),
)
