from letter_generator import name_generator, surname_generator


def main():
    for x in range(10):
        print(f'{name_generator()} {surname_generator()}')


if __name__ == '__main__':
    main()
