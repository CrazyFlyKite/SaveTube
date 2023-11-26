import logging

from main import Main


def main() -> None:
    # Configure the logging format, date format, and set the logging level
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

    # Create an instance of the Main class with the specified parameters and run it
    app = Main('SaveTube', 250, 290)
    app.run()


if __name__ == '__main__':
    main()
