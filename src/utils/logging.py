import logging


class Logger:
    """
    Event and context logging decorator
    """

    def __init__(self, handler):
        self.handler = handler
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel('DEBUG')

    def __call__(self, event, context):
        if event:
            self.logger.debug('Got event: {}'.format(event))
        try:
            response = self.handler(event, context)
            self.logger.debug('Will respond with: {}'.format(response))
            return response
        except Exception:
            self.logger.exception('Exception raised in handler: \n')
            raise Exception('Exception raised in handler')
