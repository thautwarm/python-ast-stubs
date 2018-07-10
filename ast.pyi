import typing, abc
NoneType = None
class AST(abc.ABC):
    def __init__(self, *args, lineno: int=None, colno: int=None, **kwargs): pass
class alias(AST):
    asname: typing.Union[str, NoneType]
    name: typing.Union[str]
class Import(AST):
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
    names: typing.List[typing.Union[typing.Union[alias]]]
class ImportFrom(AST):
    lineno: typing.Union[int]
    level: typing.Union[int]
    col_offset: typing.Union[int]
    module: typing.Union[str, NoneType]
    names: typing.List[typing.Union[typing.Union[alias]]]
class Store(AST):
    pass
class Name(AST):
    ctx: typing.Union[Del, Load, Store]
    id: typing.Union[str]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Str(AST):
    s: typing.Union[str]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Load(AST):
    pass
class List(AST):
    elts: typing.List[typing.Union[typing.Union[Name, Str, Subscript, BinOp, Attribute]]]
    ctx: typing.Union[Load]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Assign(AST):
    value: typing.Union[Name, Str, Tuple, ListComp, Lambda, NameConstant, JoinedStr, Compare, Num, List, BoolOp, IfExp, Subscript, UnaryOp, Call, Dict, BinOp, Attribute, DictComp]
    targets: typing.List[typing.Union[typing.Union[Tuple, Subscript, Attribute, Name]]]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class arg(AST):
    annotation: typing.Union[Name, Str, Subscript, NoneType, Attribute]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
    arg: typing.Union[str]
class arguments(AST):
    defaults: typing.List[typing.Union[typing.Union[Tuple, Str, Name, Lambda, NameConstant, List, Attribute]]]
    kwonlyargs: typing.List[typing.Union[typing.Union[arg]]]
    kw_defaults: typing.List[typing.Union[typing.Union[NameConstant]]]
    vararg: typing.Union[arg, NoneType]
    kwarg: typing.Union[arg, NoneType]
    args: typing.List[typing.Union[typing.Union[arg]]]
class Expr(AST):
    value: typing.Union[YieldFrom, Str, Yield, Call]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Attribute(AST):
    value: typing.Union[Name, Str, Subscript, Call, Attribute]
    ctx: typing.Union[Load, Store]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
    attr: typing.Union[str]
class Call(AST):
    args: typing.List[typing.Union[typing.Union[Name, Str, Tuple, ListComp, Starred, Dict, Lambda, NameConstant, JoinedStr, IfExp, Num, List, BoolOp, UnaryOp, Subscript, Call, GeneratorExp, BinOp, Attribute, DictComp]]]
    func: typing.Union[Name, Subscript, Call, Attribute]
    keywords: typing.List[typing.Union[typing.Union[keyword]]]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class IfExp(AST):
    orelse: typing.Union[Tuple, Str, Name, Lambda, Compare, Num, List, Call, Dict, Attribute]
    test: typing.Union[Name, Compare, BoolOp, Call, Attribute]
    body: typing.Union[Name, Call, Compare, Attribute]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Return(AST):
    value: typing.Union[Name, Str, NoneType, ListComp, Tuple, Lambda, NameConstant, IfExp, Compare, JoinedStr, List, BoolOp, Subscript, UnaryOp, Call, Dict, BinOp, Attribute]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class FunctionDef(AST):
    body: typing.List[typing.Union[typing.Union[AugAssign, For, Import, AnnAssign, FunctionDef, ClassDef, While, Return, If, ImportFrom, Nonlocal, Pass, Try, Assert, Delete, With, Expr, Raise, Assign]]]
    returns: typing.Union[Name, Str, NameConstant, Subscript, NoneType, Attribute]
    lineno: typing.Union[int]
    decorator_list: typing.List[typing.Union[typing.Union[Attribute, Name, Call]]]
    col_offset: typing.Union[int]
    args: typing.Union[arguments]
    name: typing.Union[str]
class Dict(AST):
    values: typing.List[typing.Union[typing.Union[Name, Str, ListComp, NameConstant, List, BoolOp, Call, BinOp, Attribute]]]
    keys: typing.List[typing.Union[typing.Union[Str, NameConstant, NoneType]]]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Tuple(AST):
    elts: typing.List[typing.Union[typing.Union[Name, Str, Tuple, Starred, NameConstant, Num, List, Ellipsis, BoolOp, Subscript, Call, BinOp, Attribute]]]
    ctx: typing.Union[Load, Store]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class comprehension(AST):
    target: typing.Union[Tuple, Name]
    iter: typing.Union[Name, Call, Attribute, List]
    ifs: typing.List[typing.Union[typing.Union[BoolOp, Name, Compare, Call]]]
    is_async: typing.Union[int]
class DictComp(AST):
    value: typing.Union[Name, Attribute]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
    generators: typing.List[typing.Union[typing.Union[comprehension]]]
    key: typing.Union[Name]
class For(AST):
    target: typing.Union[Name, Tuple, Attribute]
    body: typing.List[typing.Union[typing.Union[AugAssign, For, Return, If, Try, Expr, Assign]]]
    iter: typing.Union[Attribute, Name, Tuple, Call]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Or(AST):
    pass
class Not(AST):
    pass
class UnaryOp(AST):
    operand: typing.Union[Name, Num, BoolOp, Subscript, Call, Attribute]
    lineno: typing.Union[int]
    op: typing.Union[USub, Not]
    col_offset: typing.Union[int]
class BoolOp(AST):
    values: typing.List[typing.Union[typing.Union[Name, Str, Tuple, Compare, IfExp, List, BoolOp, UnaryOp, Subscript, Call, Dict, Attribute]]]
    op: typing.Union[Or, And]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class FormattedValue(AST):
    value: typing.Union[Attribute, Name, Call]
    conversion: typing.Union[int]
    format_spec: typing.Union[NoneType]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class JoinedStr(AST):
    values: typing.List[typing.Union[typing.Union[Str, FormattedValue]]]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class If(AST):
    body: typing.List[typing.Union[typing.Union[Break, For, AugAssign, Expr, AnnAssign, FunctionDef, ClassDef, Return, If, ImportFrom, Try, Assert, Pass, Continue, With, Raise, Assign]]]
    orelse: typing.List[typing.Union[typing.Union[AugAssign, AnnAssign, FunctionDef, Return, If, ImportFrom, Try, With, Continue, Expr, Raise, Assign]]]
    test: typing.Union[Name, Compare, BoolOp, UnaryOp, Subscript, Call, Attribute]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class YieldFrom(AST):
    value: typing.Union[Attribute, Name, Tuple, Call]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Is(AST):
    pass
class Ellipsis(AST):
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Compare(AST):
    ops: typing.List[typing.Union[typing.Union[NotIn, IsNot, Gt, GtE, Lt, Eq, Is, In, LtE, NotEq]]]
    comparators: typing.List[typing.Union[typing.Union[Tuple, Str, Name, NameConstant, Num, Ellipsis, UnaryOp, Subscript, Call, GeneratorExp, Attribute]]]
    left: typing.Union[Name, Str, NameConstant, Subscript, Call, BinOp, Attribute]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class NameConstant(AST):
    value: typing.Union[bool, NoneType]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class AnnAssign(AST):
    target: typing.Union[Name, Attribute]
    value: typing.Union[Name, NameConstant, IfExp, Subscript, Call, NoneType, BinOp, Attribute]
    annotation: typing.Union[Attribute, Name, Subscript, Str]
    simple: typing.Union[int]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Raise(AST):
    exc: typing.Union[Attribute, Name, Call, NoneType]
    cause: typing.Union[Name, NoneType]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Num(AST):
    n: typing.Union[int]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Index(AST):
    value: typing.Union[Name, Str, Tuple, NameConstant, Num, BoolOp, Subscript, UnaryOp, Call, BinOp, Attribute]
class Subscript(AST):
    value: typing.Union[Attribute, Name, Call]
    ctx: typing.Union[Del, Load, Store]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
    slice: typing.Union[Slice, Index]
class keyword(AST):
    value: typing.Union[Name, Str, Tuple, NameConstant, Num, List, BoolOp, Subscript, Call, BinOp, Attribute]
    arg: typing.Union[str, NoneType]
class ClassDef(AST):
    body: typing.List[typing.Union[typing.Union[AnnAssign, FunctionDef, ClassDef, Delete, Pass, Expr, Assign]]]
    name: typing.Union[str]
    bases: typing.List[typing.Union[typing.Union[Attribute, Name, Subscript, Call]]]
    keywords: typing.List[typing.Union[typing.Union[keyword]]]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
    decorator_list: typing.List[typing.Union[typing.Union[Name]]]
class Pass(AST):
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class ExceptHandler(AST):
    body: typing.List[typing.Union[typing.Union[Import, FunctionDef, ClassDef, Return, If, ImportFrom, Pass, Continue, Expr, Raise, Assign]]]
    name: typing.Union[str, NoneType]
    type: typing.Union[Tuple, Name, NoneType]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Try(AST):
    body: typing.List[typing.Union[typing.Union[For, AugAssign, Import, FunctionDef, Return, If, ImportFrom, Try, With, Expr, Assign]]]
    finalbody: typing.List[typing.Union[typing.Union[Expr, Assert, Assign, If]]]
    handlers: typing.List[typing.Union[typing.Union[ExceptHandler]]]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Gt(AST):
    pass
class NotEq(AST):
    pass
class Module(AST):
    body: typing.List[typing.Union[typing.Union[Import, FunctionDef, ClassDef, If, ImportFrom, Try, Delete, Expr, Assign]]]
class And(AST):
    pass
class Eq(AST):
    pass
class Lambda(AST):
    body: typing.Union[Name, NameConstant, Compare, Call]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
    args: typing.Union[arguments]
class Starred(AST):
    value: typing.Union[Name, Subscript, Call, GeneratorExp, Attribute]
    ctx: typing.Union[Load, Store]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class While(AST):
    test: typing.Union[Name, Compare, Num, Call, Attribute]
    body: typing.List[typing.Union[typing.Union[Pass, Expr, If, Assign]]]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Break(AST):
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Add(AST):
    pass
class BinOp(AST):
    right: typing.Union[Name, Str, Tuple, Num, List, BoolOp, Subscript, Call, Dict, BinOp, Attribute]
    left: typing.Union[Tuple, Str, Name, ListComp, Num, List, Subscript, Call, BinOp, Attribute]
    op: typing.Union[Add, BitAnd, Sub, FloorDiv, BitXor, Mult, Mod]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class ListComp(AST):
    elt: typing.Union[Name, Subscript, Call, Attribute]
    generators: typing.List[typing.Union[typing.Union[comprehension]]]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class withitem(AST):
    optional_vars: typing.Union[Name, NoneType]
    context_expr: typing.Union[Attribute, Name, Call]
class With(AST):
    body: typing.List[typing.Union[typing.Union[For, Return, If, ImportFrom, Try, Expr, Raise, Assign]]]
    items: typing.List[typing.Union[typing.Union[withitem]]]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Yield(AST):
    value: typing.Union[Name, Tuple, NameConstant, Subscript, Call, BinOp, Attribute]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Nonlocal(AST):
    names: typing.List[typing.Union[typing.Union[str]]]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class AugAssign(AST):
    target: typing.Union[Name, Subscript, Attribute]
    value: typing.Union[Name, Num, Call, BinOp, Attribute]
    op: typing.Union[BitOr, Sub, Add]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class GeneratorExp(AST):
    elt: typing.Union[Tuple, Name, IfExp, Compare, Subscript, Call, BinOp]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
    generators: typing.List[typing.Union[typing.Union[comprehension]]]
class Continue(AST):
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class NotIn(AST):
    pass
class In(AST):
    pass
class IsNot(AST):
    pass
class FloorDiv(AST):
    pass
class Sub(AST):
    pass
class Slice(AST):
    lower: typing.Union[Name, Call, Num, NoneType]
    step: typing.Union[UnaryOp, NoneType]
    upper: typing.Union[UnaryOp, Num, NoneType]
class BitOr(AST):
    pass
class USub(AST):
    pass
class BitXor(AST):
    pass
class Mult(AST):
    pass
class Lt(AST):
    pass
class Del(AST):
    pass
class Delete(AST):
    targets: typing.List[typing.Union[typing.Union[Name, Subscript]]]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
class Mod(AST):
    pass
class Assert(AST):
    msg: typing.Union[Str, BinOp, NoneType]
    lineno: typing.Union[int]
    col_offset: typing.Union[int]
    test: typing.Union[Compare, Call]
class GtE(AST):
    pass
class LtE(AST):
    pass
class BitAnd(AST):
    pass