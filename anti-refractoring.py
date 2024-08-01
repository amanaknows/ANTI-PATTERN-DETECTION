# anti_refactor.py

import random
import ast

def introduce_god_object(code):
    """Introduce a God Object anti-pattern"""
    tree = ast.parse(code)
    class_def = tree.body[0]
    for i in range(10):  # add 10 random methods
        method_name = f"method_{i}"
        method_def = ast.FunctionDef(
            name=method_name,
            args=ast.arguments(
                args=[],
                vararg=None,
                kwonlyargs=[]
            ),
            body=[ast.Pass()],
            decorator_list=[]
        )
        class_def.body.append(method_def)
    return ast.unparse(tree)

def add_duplicate_code(code):
    """Add duplicate code blocks"""
    tree = ast.parse(code)
    func_def = tree.body[0]
    duplicate_code = ast.parse("x = 5\ny = 10").body
    func_def.body.extend(duplicate_code)
    return ast.unparse(tree)

def create_long_method(code):
    """Create a long method"""
    tree = ast.parse(code)
    func_def = tree.body[0]
    long_method_body = [ast.Expr(ast.Num(n)) for n in range(100)]
    func_def.body.extend(long_method_body)
    return ast.unparse(tree)

def add_switch_statement_with_many_cases(code):
    """Add a switch statement with many cases"""
    tree = ast.parse(code)
    func_def = tree.body[0]
    switch_stmt = ast.parse("x = 5\nif x == 1: pass\nelif x == 2: pass\n...").body[0]
    for i in range(10):  # add 10 cases
        case_clause = ast.IfExp(
            test=ast.Compare(
                left=ast.Name(id="x", ctx=ast.Load()),
                ops=[ast.Eq()],
                comparators=[ast.Num(i)]
            ),
            body=ast.Pass(),
            orelse=None
        )
        switch_stmt.orelse = case_clause
    func_def.body.append(switch_stmt)
    return ast.unparse(tree)

def anti_refactor(code):
    """Apply anti-refactoring techniques to the code"""
    techniques = [
        introduce_god_object,
        add_duplicate_code,
        create_long_method,
        add_switch_statement_with_many_cases
    ]
    for _ in range(random.randint(1, 3)):  # apply 1-3 techniques
        technique = random.choice(techniques)
        code = technique(code)
    return code

# example usage
code = """
def my_function():
    x = 5
    y = 10
"""
anti_refactored_code = anti_refactor(code)
print(anti_refactored_code)
