import json

if not hasattr(json, 'JSONDecodeError'):
    json.JSONDecodeError = ValueError
else:
    from json.decoder import JSONDecodeError


class WNBAError(Exception):
    pass


class ApiError(WNBAError):
    def __init__(self, response):
        self.response = response
        self.status_code = response.status_code
        try:
            error_data = response.json().get('errors')
            self.message = error_data[0].get('messages', 'UNKNOWN')

        except (KeyError, JSONDecodeError, TypeError):
            self.message = 'UNKNOWN'
            print(response)
        super(ApiError, self).__init__(self.message)

