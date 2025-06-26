import ast

with open("src/s0c0/main.py") as f:
    tree = ast.parse(f.read())

# 举例检查是否使用了函数定义（或其他如递归等）
functions = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
assert functions, "你需要定义至少一个函数"
print("✅ AST 检查通过")
