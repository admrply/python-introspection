from os import listdir
from os.path import isfile, join
import imp

def call_wiz_api(op, var, tok):
    print(f"Calling Wiz with {op} / {var} / token {tok}")

class GraphQLCalls(object):
    def __init__(self) -> None:
        self.__wiz_access_token = self.__get_wiz_access_token()
        self.__generate_methods()

    def __get_wiz_access_token(self):
        return "abc"
    
    def __make_method(self, op, var):
        def _method(self):
            call_wiz_api(op, var, self.__wiz_access_token)
        return _method


    def __generate_methods(self):
        templates = [f for f in listdir('templates') if isfile(join('templates', f))]
        for t in templates:
            with open(join('templates', t)) as tf:
                _template = imp.load_source(t, join('templates',t))
                _func_name = t.split('.')[0]
                _method = self.__make_method(_template.operation, _template.variables)
                setattr(GraphQLCalls, _func_name, _method)

gqlc = GraphQLCalls()
gqlc.one()
gqlc.two()
gqlc.three()
print("exit")