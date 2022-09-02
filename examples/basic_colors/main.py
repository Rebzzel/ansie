from ansie.styles import (
    black,
    red,
    green,
    yellow,
    blue,
    magenta,
    cyan,
    white,
)


colors = {
    'black': black,
    'red': red,
    'green': green,
    'yellow': yellow,
    'blue': blue,
    'magenta': magenta,
    'cyan': cyan,
    'white': white,
}


def main():
    for name, color in colors.items():
        print(
            color.fg(f'{name}.fg'.ljust(10)), 
            color.bg(f'{name}.bg'.ljust(10)),
        )


if __name__ == '__main__':
    main()
