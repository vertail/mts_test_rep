import requests
from functools import wraps

CONNECTION = 'https://demo-mtc.herokuapp.com'


def api_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('\n')
        check_code = kwargs.pop('check_code') if kwargs.get(
            'check_code') else None  # извлекаем для того чтоб дальше не передать в функцию
        result = func(*args, **kwargs)
        if check_code:
            print('Assert result and expected code: \n result_code: {} = expected code:{} '.format(result.status_code,
                                                                                                   check_code))
            assert (result.status_code == check_code)
        print('Call API:{}'.format(result.url))
        print('Result is: {}'.format(result.json()))
        return result

    return wrapper


@api_check
def create_task():
    result = requests.post("{}/task/".format(CONNECTION))
    return result


@api_check
def get_task_status(guid):
    result = requests.get("{}/task/{}".format(CONNECTION, guid))
    return result
