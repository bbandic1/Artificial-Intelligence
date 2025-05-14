# vrijeme_rules_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def ponesi_kabanicu(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('vrijeme', 'pada_kisa', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('vrijeme', 'puse_vjetar', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('vrijeme', 'ponesi',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def ponesi_kisobran(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('vrijeme', 'pada_kisa', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('vrijeme', 'puse_vjetar', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('vrijeme', 'ponesi',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def ponesi_nista(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('vrijeme', 'pada_kisa', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('vrijeme', 'puse_vjetar', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('vrijeme', 'ponesi',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('vrijeme_rules')
  
  fc_rule.fc_rule('ponesi_kabanicu', This_rule_base, ponesi_kabanicu,
    (('vrijeme', 'pada_kisa',
      (pattern.pattern_literal('true'),),
      False),
     ('vrijeme', 'puse_vjetar',
      (pattern.pattern_literal('true'),),
      False),),
    (pattern.pattern_literal('kabanicu'),))
  
  fc_rule.fc_rule('ponesi_kisobran', This_rule_base, ponesi_kisobran,
    (('vrijeme', 'pada_kisa',
      (pattern.pattern_literal('true'),),
      False),
     ('vrijeme', 'puse_vjetar',
      (pattern.pattern_literal('false'),),
      False),),
    (pattern.pattern_literal('kisobran'),))
  
  fc_rule.fc_rule('ponesi_nista', This_rule_base, ponesi_nista,
    (('vrijeme', 'pada_kisa',
      (pattern.pattern_literal('false'),),
      False),
     ('vrijeme', 'puse_vjetar',
      (pattern.pattern_literal('false'),),
      False),),
    (pattern.pattern_literal('nista'),))


Krb_filename = '..\\vrijeme_rules.krb'
Krb_lineno_map = (
    ((12, 16), (5, 5)),
    ((17, 21), (6, 6)),
    ((22, 23), (8, 8)),
    ((32, 36), (12, 12)),
    ((37, 41), (13, 13)),
    ((42, 43), (15, 15)),
    ((52, 56), (19, 19)),
    ((57, 61), (20, 20)),
    ((62, 63), (22, 22)),
)
