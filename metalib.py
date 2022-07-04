import inspect
import sys

def get_funcs(module,exclude=None):
    '''returns all functions in a module
    can supply a list of chars to exclude that start with this charc
    eg if module contains functions: _a, a then exlude = '_' will return only a'''
    func_descs = inspect.getmembers(sys.modules[module], predicate=inspect.isfunction)
    funcs = [func_desc[0] for func_desc in func_descs] #removes function addr that is returned above
    if exclude:
        return [func for func in funcs for exc in exclude if not func.startswith(exc)]
    return funcs

def print_funcs(meta_lib):
    '''
    Returns a text string which enables all functions (excluding '_')
    to be printed
    Pass in name used for metalib
    Usage in importing module:
    import lib.metalib as _meta
    exec(_meta.print_funcs('_meta'))
    '''
    return f'''for f in {meta_lib}.get_funcs(__name__,exclude=['_']):
    exec(f"print('{{f}}(): ',{{f}}.__doc__)")
'''

