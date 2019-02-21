import ast
import operator as op

operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}

def evaluate_expression(math_expr):
    return evaluate(ast.parse(math_expr, mode='eval').body)

def evaluate(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        return operators[type(node.op)](evaluate(node.left), evaluate(node.right))
    elif isinstance(node, ast.UnaryOp):
        return operators[type(node.op)](evaluate(node.operand))
    else:
        raise TypeError(node)

if __name__ == "__main__":
    print(evaluate_expression('-1 + (2 + 3)'))