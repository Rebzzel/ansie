from .misc import esc, csi


def cursor_goto(column: int, row: int) -> str:
    return csi(f'{row};{column}H')


cursor_up = csi('1A')
cursor_down = csi('1B')
cursor_right = csi('1C')
cursor_left = csi('1D')


def cursor_save(*, dec: bool = None, sco: bool = None):
    if (dec is None) and (sco is None):
        dec = True
    
    sequence = []

    if dec: sequence += [ ' 7' ]
    if sco: sequence += [ '[s' ]

    return esc(*sequence)


def cursor_restore(*, dec: bool = None, sco: bool = None):
    if (dec is None) and (sco is None):
        dec = True

    sequence = []

    if dec: sequence += [ ' 8' ]
    if sco: sequence += [ '[u' ]

    return esc(*sequence)


clear_row = csi('2K')
clear_row_before_cursor = csi('1K')
clear_row_after_cursor = csi('0K')

clear_screen = csi('2J')
clear_screen_before_cursor = csi('1J')
clear_screen_after_cursor = csi('0J')


__all__ = [
    'cursor_goto',
    'cursor_up',
    'cursor_down',
    'cursor_right',
    'cursor_left',
    'cursor_save',
    'cursor_restore',
    
    'clear_row',
    'clear_row_before_cursor',
    'clear_row_after_cursor',
    
    'clear_screen',
    'clear_screen_before_cursor',
    'clear_screen_after_cursor',
]
