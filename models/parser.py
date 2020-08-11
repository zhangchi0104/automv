import ast

from models.conditions import ConjunctionCondition, ContainsCondition, ExtensionCondition


class RuleParser(ast.NodeVisitor):

    def __init__(self):
        super().__init__()

    def visit_Expr(self, node: ast.Expr):
        res = self.visit(node.value)
        return res

    def visit_BinOp(self, node: ast.BinOp):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if isinstance(node.op, ast.BitAnd):
            return ConjunctionCondition([left, right], 'and')
        if isinstance(node.op, ast.BitOr):
            return ConjunctionCondition([left, right], 'or')

    def visit_Call(self, node: ast.Call):
        ctor = self.visit(node.func)
        args = [arg.id for arg in node.args]
        return ctor(args)

    def visit_Name(self, node: ast.Name):
        if node.id == "extensions":
            return ExtensionCondition

        if node.id == "contains":
            return ContainsCondition

    def visit_Module(self, node: ast.Module):
        return self.visit(node.body[0])

    def parse(self, expr: str):
        return self.visit(ast.parse(expr))
