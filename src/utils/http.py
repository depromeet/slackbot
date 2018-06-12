import json


class LambdaResponse:
    """
    Lambda HTTP Response generating decorator
    """

    def __init__(self, handler):
        self.handler = handler

    def __call__(self, event, context):
        response = self.handler(event, context)

        if 'statusCode' in response and \
                response['statusCode'] == 500:
            return response
        else:
            return {
                'statusCode': 200,
                'body': json.dumps(response)
            }


class ExceptionHandler:
    """
    Lambda HTTP 500 Response generating decorator when things are getting wrong...
    """

    def __init__(self, handler):
        self.handler = handler

    def __call__(self, event, context):
        try:
            response = self.handler(event, context)
            return response
        except Exception:
            return {
                'statusCode': 500,
                'body': 'something went wrong...'
            }
