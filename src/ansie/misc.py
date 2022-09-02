import typing as t


def esc(*sequence: t.Tuple[str]) -> str:
    '''Builds ANSI ESC string.'''
    return ''.join((f'\x1B{it}' for it in sequence))


def csi(*sequence: t.Tuple[str]) -> str:
    '''Builds ANSI CSI string.'''
    return ''.join((f'\x1B[{it}' for it in sequence))


def style(*sequence: t.Tuple[str]) -> str:
    '''Builds ANSI CSI style string.'''
    return csi(f'{";".join(sequence)}m')


__all__ = [
    'esc',
    'csi',
    'style',
]
