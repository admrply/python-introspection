from os import listdir
from os.path import isfile, join
import imp
from typing import Callable, Protocol
import types

def call_api(op, var, tok):
    print(f"Calling Wiz with {op} / {var} / token {tok}")

class GraphQLCalls(object):
    one: Callable[[], None]
    two: Callable[[], None]
    three: Callable[[], None]
    blahblah: Callable[[], None]

    def __init__(self) -> None:
        self.__wiz_access_token = self.__get_access_token()
        self.__generate_methods()

    def __get_access_token(self):
        return "abc"
    
    def __make_method(self, op, var):
        def _method():
            call_api(op, var, self.__wiz_access_token)
        return _method


    def __generate_methods(self):
        templates = [f for f in listdir('templates') if isfile(join('templates', f))]
        for t in templates:
            _template = imp.load_source(t, join('templates',t))
            _func_name = t.split('.')[0]
            _method = self.__make_method(_template.operation, _template.variables)
            setattr(GraphQLCalls, _func_name, _method)


gqlc = GraphQLCalls()
gqlc.one()
gqlc.two()
gqlc.three()
gqlc.blahblah()
gqlc.mutate_something()

