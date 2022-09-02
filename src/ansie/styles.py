import typing as t

from .misc import style


def reset_all() -> str:
    return style('0')


def reset_color(*, fg: bool = None, bg: bool = None) -> str:
    if (fg is None) and (bg is None):
        fg = bg = True

    sequence = []

    if fg: sequence.append('39')
    if bg: sequence.append('49')

    return style(*sequence)


class Style:
    def __init__(self, code: str, undo_code: str): 
        self._code = code
        self._undo_code = undo_code

    def undo(self) -> str:
        return style(self._undo_code)

    def __str__(self) -> str:
        return style(self._code)

    def __call__(self, string: str) -> str:
        return ''.join((str(self), string, self.undo(),))
    
    def __add__(self, other) -> t.Union['Union', str]:
        return Union(self) + other


class Union:
    def __init__(self, *styles: t.Tuple[Style]):
        self.styles = styles

    def undo(self) -> str:
        return ''.join(s.undo() for s in self.styles)

    def __str__(self):
        return ''.join(str(s) for s in self.styles)

    def __call__(self, string: str) -> str:
        return ''.join((str(self), string, self.undo(),))

    def __add__(self, other) -> t.Union['Union', str]:
        if isinstance(other, Style):
            return Union(*self.styles, other)
        elif isinstance(other, Union):
            return Union(*self.styles, *other.styles)
        elif isinstance(other, str):
            return str(self) + other
        else:
            raise TypeError()


bold = Style('1', '22')
dim = Style('2', '22')
italic = Style('3', '23')
underline = Style('4', '24')
blinking = Style('5', '25')
inverse = Style('7', '27')
invisible = Style('8', '28')
strikethrough = Style('9', '29')


class FGColor(Style):
    def __init__(self, code: str):
        super().__init__(code, '39')


class BGColor(Style):
    def __init__(self, code: str):
        super().__init__(code, '49')


class ColorMap:
   def __init__(self, fg: t.Union[str, FGColor], bg: t.Union[str, BGColor]):
        self.fg = FGColor(fg) if type(fg) is str else fg
        self.bg = BGColor(bg) if type(bg) is str else bg


black = ColorMap('30', '40')
red = ColorMap('31', '41')
green = ColorMap('32', '42')
yellow = ColorMap('33', '43')
blue = ColorMap('34', '44')
magenta = ColorMap('35', '45')
cyan = ColorMap('36', '46')
white = ColorMap('37', '47')


def color256(i: int) -> ColorMap:
    return ColorMap(f'38;5;{i}', f'48;5;{i}')


def rgb(r: int, g: int, b: int) -> ColorMap:
    return ColorMap(f'38;2:{r};{g};{b}', f'48;2;{r};{g};{b}')


__all__ = [
    'reset_all',
    'reset_color',

    'Style',
    'Union',
    
    'bold',
    'dim',
    'italic',
    'underline',
    'blinking',
    'inverse'
    'invisible',
    'strikethrough',

    'FGColor',
    'BGColor',
    'ColorMap',

    'black'
    'red',
    'green'
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white',
    'color256',
    'rgb',
]
