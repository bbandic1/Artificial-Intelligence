# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('vremenski_ekspert', '', 'vrijeme.kfb'):
           [1747228633.8583941, 'vrijeme.fbc'],
         ('vremenski_ekspert', '', 'vrijeme_rules.krb'):
           [1747228633.860394, 'vrijeme_rules_fc.py'],
        },
        compiler_version)

