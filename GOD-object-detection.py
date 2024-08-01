import ast

class AntiPatternDetector(ast.NodeVisitor):
    def __init__(self):
        self.god_objects = []

    def visit_ClassDef(self, node):
        method_count = 0
        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.FunctionDef):
                method_count += 1
        if method_count > 10:  # arbitrary threshold
            self.god_objects.append(node.name)

def detect_anti_patterns(code):
    tree = ast.parse(code)
    detector = AntiPatternDetector()
    detector.visit(tree)
    return detector.god_objects

# example usage
code = """
class GodObject:
    def method1(self):
        pass
    def method2(self):
        pass
    def method3(self):
        pass
    def method4(self):
        pass
    def method5(self):
        pass
    def method6(self):
        pass
    def method7(self):
        pass
    def method8(self):
        pass
    def method9(self):
        pass
    def method10(self):
        pass
    def method11(self):
        pass
"""

anti_patterns = detect_anti_patterns(code)
print("Detected anti-patterns:")
for pattern in anti_patterns:
    print(f"- God Object: {pattern}")
