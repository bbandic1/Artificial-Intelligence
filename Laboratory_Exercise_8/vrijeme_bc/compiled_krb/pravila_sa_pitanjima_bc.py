# pravila_sa_pitanjima_bc.py

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
        with engine.prove('pitanja', 'kisa', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pravila_sa_pitanjima.ponesi_kabanicu: got unexpected plan from when clause 1"
            with engine.prove('pitanja', 'vjetar', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pravila_sa_pitanjima.ponesi_kabanicu: got unexpected plan from when clause 2"
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
        with engine.prove('pitanja', 'kisa', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pravila_sa_pitanjima.ponesi_kisobran: got unexpected plan from when clause 1"
            with engine.prove('pitanja', 'vjetar', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pravila_sa_pitanjima.ponesi_kisobran: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ponesi_nista_zbog_vremena(rule, arg_patterns, arg_context):
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
        with engine.prove('pitanja', 'kisa', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pravila_sa_pitanjima.ponesi_nista_zbog_vremena: got unexpected plan from when clause 1"
            with engine.prove('pitanja', 'vjetar', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pravila_sa_pitanjima.ponesi_nista_zbog_vremena: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ponesi_cizme(rule, arg_patterns, arg_context):
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
        with engine.prove('pitanja', 'vanredna_situacija', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pravila_sa_pitanjima.ponesi_cizme: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ponesi_masku(rule, arg_patterns, arg_context):
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
        with engine.prove('pitanja', 'vanredna_situacija', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pravila_sa_pitanjima.ponesi_masku: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def nista_dodatno_zbog_situacije(rule, arg_patterns, arg_context):
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
        with engine.prove('pitanja', 'vanredna_situacija', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pravila_sa_pitanjima.nista_dodatno_zbog_situacije: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('pravila_sa_pitanjima')
  
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
  
  bc_rule.bc_rule('ponesi_nista_zbog_vremena', This_rule_base, 'sta_ponijeti',
                  ponesi_nista_zbog_vremena, None,
                  (pattern.pattern_literal('nista'),),
                  (),
                  (pattern.pattern_literal('false'),))
  
  bc_rule.bc_rule('ponesi_cizme', This_rule_base, 'sta_jos_ponijeti',
                  ponesi_cizme, None,
                  (pattern.pattern_literal('gumene_cizme'),),
                  (),
                  (pattern.pattern_literal(1),))
  
  bc_rule.bc_rule('ponesi_masku', This_rule_base, 'sta_jos_ponijeti',
                  ponesi_masku, None,
                  (pattern.pattern_literal('masku_za_lice'),),
                  (),
                  (pattern.pattern_literal(2),))
  
  bc_rule.bc_rule('nista_dodatno_zbog_situacije', This_rule_base, 'sta_jos_ponijeti',
                  nista_dodatno_zbog_situacije, None,
                  (pattern.pattern_literal('nista_dodatno'),),
                  (),
                  (pattern.pattern_literal(3),))


Krb_filename = '..\\pravila_sa_pitanjima.krb'
Krb_lineno_map = (
    ((14, 18), (5, 5)),
    ((20, 25), (7, 7)),
    ((26, 31), (8, 8)),
    ((44, 48), (11, 11)),
    ((50, 55), (13, 13)),
    ((56, 61), (14, 14)),
    ((74, 78), (17, 17)),
    ((80, 85), (19, 19)),
    ((86, 91), (20, 20)),
    ((104, 108), (24, 24)),
    ((110, 115), (26, 26)),
    ((128, 132), (29, 29)),
    ((134, 139), (31, 31)),
    ((152, 156), (34, 34)),
    ((158, 163), (36, 36)),
)
