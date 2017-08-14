
import json
import pandas as pd

from wnba.utils import check_status_code


class BaseEndpoint(object):

    def __init__(self, parent):
        """
        :param parent: API client.
        """
        self.client = parent

    def request(self, request_url, headers, params={}, data={}, session=None):
        """
        :param request_url: url to request data from.
        :param headers: request headers.
        :param params: Params to be used in request.
        :param data: data to be sent in request body.
        :param session: Requests session to be used, reduces latency.
        """
        session = session or self.client.session
        response = session.request('GET', request_url, params=params, data=json.dumps(data), headers=headers)
        if response.status_code == 400:
            response = session.request('GET', request_url, params=params, data=json.dumps(data), headers=headers)
        print(response.url)
        # check_status_code(response)
        return response.json()

    @staticmethod
    def process_response(response_json, idx_val, result_name):
        """
        Parse data received from wnba requests.

        :param response_json: data returned from requests to wnba.
        :type response_json: JSON
        :param idx_val: the index to retrieve from the returned data.
        :type idx_val: int
        :param result_name: json key to target for parsing results.
        :type result_name: str
        :returns: parsed nba data.
        :rtype: DataFrame

        """
        try:
            headers = response_json[result_name][idx_val]['headers']
            values = response_json[result_name][idx_val]['rowSet']
        except KeyError:
            headers = response_json[result_name]['headers']
            values = response_json[result_name]['rowSet']
        return pd.DataFrame(values, columns=headers)
