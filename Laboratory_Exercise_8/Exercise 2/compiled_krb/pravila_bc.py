# pravila_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def ponesi_kabanicu(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('cinjenice_vremena', 'pada_kisa', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pravila.ponesi_kabanicu: got unexpected plan from when clause 1"
            with engine.prove('cinjenice_vremena', 'puse_vjetar', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pravila.ponesi_kabanicu: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ponesi_kisobran(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('cinjenice_vremena', 'pada_kisa', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pravila.ponesi_kisobran: got unexpected plan from when clause 1"
            with engine.prove('cinjenice_vremena', 'puse_vjetar', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pravila.ponesi_kisobran: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ponesi_nista(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('cinjenice_vremena', 'pada_kisa', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pravila.ponesi_nista: got unexpected plan from when clause 1"
            with engine.prove('cinjenice_vremena', 'puse_vjetar', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pravila.ponesi_nista: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('pravila')
  
  bc_rule.bc_rule('ponesi_kabanicu', This_rule_base, 'sta_ponijeti',
                  ponesi_kabanicu, None,
                  (pattern.pattern_literal('kabanicu'),),
                  (),
                  (pattern.pattern_literal('true'),))
  
  bc_rule.bc_rule('ponesi_kisobran', This_rule_base, 'sta_ponijeti',
                  ponesi_kisobran, None,
                  (pattern.pattern_literal('kisobran'),),
                  (),
                  (pattern.pattern_literal('true'),
                   pattern.pattern_literal('false'),))
  
  bc_rule.bc_rule('ponesi_nista', This_rule_base, 'sta_ponijeti',
                  ponesi_nista, None,
                  (pattern.pattern_literal('nista'),),
                  (),
                  (pattern.pattern_literal('false'),))


Krb_filename = '..\\pravila.krb'
Krb_lineno_map = (
    ((14, 18), (5, 5)),
    ((20, 25), (7, 7)),
    ((26, 31), (8, 8)),
    ((44, 48), (12, 12)),
    ((50, 55), (14, 14)),
    ((56, 61), (15, 15)),
    ((74, 78), (19, 19)),
    ((80, 85), (21, 21)),
    ((86, 91), (22, 22)),
)
