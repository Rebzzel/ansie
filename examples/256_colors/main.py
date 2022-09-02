from ansie.styles import color256


def main():
    for i in range(256):
        print(color256(i).bg(f'{i:>3}'), end=' ')
        if (i + 1) % 16 == 0:
            print('')


if __name__ == '__main__':
    main()
