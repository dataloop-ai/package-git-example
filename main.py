import dtlpy as dl
import logging

logger = logging.getLogger(name=__name__)


class ServiceRunner(dl.BaseServiceRunner):
    """
    Package runner class
    """

    def __init__(self):
        print("init")

    def run(self, item):
        for i in range(10):
            print(i)
        print(item.name)
