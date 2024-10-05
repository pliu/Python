import sys
from test_pkg import func


func.print_var()


from test_pkg import variable


variable.var = "test2"
func.print_var()


def uncache(exclude):
    """Remove package modules from cache except excluded ones.
    On next import they will be reloaded.

    Args:
        exclude (iter<str>): Sequence of module paths.
    """
    pkgs = []
    for mod in exclude:
        pkg = mod.split('.', 1)[0]
        pkgs.append(pkg)

    to_uncache = []
    for mod in sys.modules:
        if mod in exclude:
            continue

        if mod in pkgs:
            to_uncache.append(mod)
            continue

        for pkg in pkgs:
            if mod.startswith(pkg + '.'):
                to_uncache.append(mod)
                break

    for mod in to_uncache:
        del sys.modules[mod]


uncache(['test_pkg.variable'])


from test_pkg import func


func.print_var()
