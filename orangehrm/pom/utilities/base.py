import logging


class Base:
    logging.basicConfig(filename="log.txt", filemode="w", format="%(asctime)s, %(message)s", level=logging.INFO)
