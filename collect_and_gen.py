import ast
from Redy.Tools.PathLib import Path
from Redy.Opt import feature, ASTService
import Redy
import flask
from Redy.Magic.Classic import record
import linq
from toolz import compose, curry
import typing

import textwrap
from functools import reduce
import collections
import sys
sys.setrecursionlimit(3000)


class CollectASTTypeStub(ASTService):

    def __init__(self, ast_collection: collections.defaultdict):
        self._ = ast_collection

    def initialize_env(self, _) -> None:
        pass

    def is_depth_first(self):
        return False

    def get_dispatch(self, elem):
        return self.flat

    def flat(self, elem):
        ty = type(elem)
        self._[ty.__name__].update((field_name, create_tobj(v)) for field_name, v in elem.__dict__.items() if not field_name.startswith('__') and not isinstance(v, list) or v)
        return self.feature.ast_transform(elem)


def collect_ast():
    type_spec: dict = collections.defaultdict(set)

    def is_python(path: str):
        return path.endswith('.py') or Path(path).is_dir()

    all_python_files = linq.Flow(Path(Redy.__file__).parent().collect(is_python)).concat(Path(flask.__file__).parent().collect(is_python))._

    for each in all_python_files:
        with each.open('r', encoding='utf8') as file:
            try:
                ast_of_src_code = ast.parse(file.read())
                service = CollectASTTypeStub(type_spec)
                feature(service).just_apply_ast_transformation(ast_of_src_code)
            except SyntaxError:
                # other py version
                pass

    def snd(tp):
        return tp[1]

    stub_code = \
    (linq.Flow(type_spec)
         .map(lambda class_name, fields:
                linq.Flow(fields)
                    .group_by(lambda fst, snd: fst)
                    .map(lambda field_name, pairs:
                            '{}: {}'.format(
                            field_name,
                            compose(
                                str,
                                curry(reduce)(lambda a, b: a.union(b)),
                                curry(map)(snd))(pairs)))
                    .then(
                        compose(
                            'class {}(AST):\n'.format(class_name).__add__,
                            lambda _: textwrap.indent(_, " " * 4),
                            lambda any_code: any_code if any_code else 'pass',
                            '\n'.join))
                    ._)
         .then(
            compose(
                'import typing, abc\nNoneType = None\n'.__add__,
                'class AST(abc.ABC):\n    def __init__(self, *args, lineno: int=None, colno: int=None, **kwargs): pass\n'.__add__,
                '\n'.join
                )))._

    with Path('./').into('ast.pyi').open('w', encoding='utf8') as stub:
        stub.write(stub_code)

    with Path(ast.__file__).parent().into('ast.pyi').open('w', encoding='utf8') as stub:
        stub.write(stub_code)



def create_tobj(obj):
    if isinstance(obj, list):
        if not obj:
            return None
        return TObj(tuple(set(create_tobj(e) for e in obj)), ())
    return TObj((), (type(obj).__name__, ))


@record
class TObj:
    list_elem_ty_collect: ...
    single_ty_collect: ...

    def union(self, other: 'TObj'):
        if isinstance(self, str) and isinstance(other, str):
            return TObj((), tuple({self, other}))
        elif isinstance(self, str):
            return TObj(other.list_elem_ty_collect, tuple(set(other.single_ty_collect + (self,))))
        elif isinstance(other, str):
            return TObj(self.list_elem_ty_collect, tuple(set(self.single_ty_collect + (other,))))

        list_elems = set(self.list_elem_ty_collect + other.list_elem_ty_collect)
        other_elems = tuple(set(self.single_ty_collect + other.single_ty_collect))
        if list_elems:
            list_elems = reduce(TObj.union, list_elems)


        return TObj((list_elems, ) if list_elems else (),  other_elems if other_elems else ())

    def __str__(self):
        list_ty = []
        if self.list_elem_ty_collect:
            list_ty = ['typing.List[typing.Union[{}]]'.format(', '.join(map(str, self.list_elem_ty_collect)))]


        if self.single_ty_collect:
            return 'typing.Union[{}]'.format(', '.join(map(str, list(self.single_ty_collect) + list_ty)))

        return list_ty.pop()


collect_ast()




