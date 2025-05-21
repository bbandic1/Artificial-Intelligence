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
         ('', '', 'pitanja.kqb'):
           [1747820317.4424481, 'pitanja.qbc'],
         ('', '', 'pravila_sa_pitanjima.krb'):
           [1747820317.4474478, 'pravila_sa_pitanjima_bc.py'],
        },
        compiler_version)

