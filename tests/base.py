import logging
import tracemalloc


def start_tests():
    tracemalloc.start()
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(name)s: %(message)s"
    )
