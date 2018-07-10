import ast

def some_func(node: ast.With):
    node.items[0].context_expr.