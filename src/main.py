import logging

from app.container import ApplicationContainer

lg = logging.getLogger(__name__)


def start():
    lg.debug('start')
    container = ApplicationContainer()
    container.run()


if __name__ == '__main__':
    start()
