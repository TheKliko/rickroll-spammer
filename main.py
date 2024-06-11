import webbrowser

URL: str = r'https://www.youtube.com/watch?v=dQw4w9WgXcQ'


def main() -> None:
    while True:
        webbrowser.open(url=URL, new=2, autoraise=True)


if __name__ == '__main__':
    main()
