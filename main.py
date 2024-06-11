import webbrowser

URL: str = r'https://www.youtube.com/watch?v=dQw4w9WgXcQ'


def main() -> None:
    for i in range(15):
        webbrowser.open(url=URL, new=2, autoraise=True)


if __name__ == '__main__':
    main()