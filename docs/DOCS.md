# Documentation
1. [Styles and colors](#styles-and-colors)
2. [Screen](#screen)
3. [Misc](#misc)


## Styles and colors

Ansie implements super easy and super powerful work with styles and colors.

All you need to do is just choose style or color and wrap your string:
```py
from ansie.styles import bold, red
print(bold('Im bold'))
print(red.fg('Im red'))
```

Note: The color is actually map of foreground and background colors for which
we use `fg` and `bg`.

```py
print(red.fg('Im red foreground'))
print(red.bg('Im red background'))
```

You also can create your own color using `rgb` function:
```py
from ansie.styles import rgb
my_super_unusual_red = rgb(255, 0, 1)
print(my_super_unsual_red.bg('Wow!'))
```

Or/and create styles union:
```py
from ansie.styles import red, italic, rgb
my_super_unuasul_black = rgb(0, 1, 0)
my_style = red.bg + my_super_unusual_black.fg + italic
print(my_style('Here could be your ad :D'))
```

**Styles:**
- bold
- dim
- italic
- underline
- blinking
- inverse
- invisible
- strikethrough

**Colors:**
- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white
- color256(i)
- rgb(r, g, b)

## Screen
Unfinished yet :\

**Functions:**
- cursor\_goto(column, row)
- cursor\_up
- cursor\_down
- cursor\_right
- cursor\_left
- cursor\_save(\*, dec, sco)
- cursor\_restore(\*, dec, sco)
- clear\_row
- clear\_row\_before\_cursor
- clear\_row\_after\_cursor
- clear\_screen
- clear\_screen\_before\_cursor
- clear\_screen\_after\_cursor

## Misc

### Forerunner functions
Probably you want generate ESC codes by yourself, Ansie also can help you with
this.

- esc(\*sequence) - Generates ESC code.
```
>>> esc('one', 'two')
'\x1Bone\x1Btwo'
```
- csi(\*sequence) - Generates CSI code.
```
>>> csi('one', 'two')
'\x1B[one\x1B[two'
```
- style(\*sequence) - Generates Style code.
```
>>> style('one', 'two')
'\x1B[one;twom'
```
