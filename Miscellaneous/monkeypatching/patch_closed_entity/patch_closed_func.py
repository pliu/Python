import test_pkg
import ast
import inspect


a = test_pkg.Test()
a.func3()
print("---")


source = inspect.getsource(test_pkg.Test.func3)
print(source)
try:
    root = ast.parse(source)
except Exception as e:
    print(e)
print("---")


source = inspect.getsource(test_pkg.Test)
print(source)
print("---")


root = ast.parse(source)


for node in ast.iter_child_nodes(root):
    print(ast.dump(node))
print(root.body)
print("---")


for node in ast.iter_child_nodes(root.body[0]):
    print(ast.dump(node))
print(root.body[0].body)
print("---")


for node in ast.iter_child_nodes(root.body[0].body[0]):
    print(ast.dump(node))
print(root.body[0].body[0].body)
print("---")


def get_source(o):
    s = inspect.getsource(o).split('\n')
    indent = len(s[0]) - len(s[0].lstrip())
    return '\n'.join(i[indent:] for i in s)


def _():
    return "test2"


root2 = ast.parse(get_source(_))
root.body[0].body[0].body[0] = root2.body[0]
print(ast.dump(root.body[0].body[0]))


python_object = compile(root, '<string>', 'exec')
exec(python_object, test_pkg.__dict__)


a.func3()
b = test_pkg.Test()
b.func3()
