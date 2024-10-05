import test_pkg
import ast
import inspect


test_pkg.func()
print("---")


source = inspect.getsource(test_pkg)
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


root.body[0].body[0].body[0].value.s = "test2"
print(ast.dump(root.body[0].body[0].body[0]))


python_object = compile(root, '<string>', 'exec')
exec(python_object, test_pkg.__dict__)


test_pkg.func()
