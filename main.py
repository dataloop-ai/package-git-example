import dtlpy as dl
import logging

logger = logging.getLogger(name=__name__)


class ServiceRunner(dl.BaseServiceRunner):
    """
    Package runner class
    """

    def __init__(self):
        print('This print is from the init of the service.')

    def run(self, item):
        """
        This is the main function for this FaaS

        :param item: dl.Item
        :return:
        """
        print('This is a print from an execution that runs on the item: {}'.format(item.name))
        logger.warning('We can also use logger for different debug levels')
