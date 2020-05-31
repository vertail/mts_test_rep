from api import get_task_status, create_task
from time import sleep
import uuid
import pytest
import hamcrest



"Блок тестов на корректные коды от ручек"
def test_create_task_202_status_code():
    create_task(check_code=202)

def test_get_task_202_status_code():
    task = create_task(check_code=202)
    get_task_status(task.json(), check_code=200)

def test_get_task_404_status_code():
    get_task_status(uuid.uuid4(), check_code=404)

def test_get_task_400_status_code():
    get_task_status('123', check_code=200)

"Тест на корректность взаимосвязанных процессов и проверок статусов по ним. created->running->finishing"
def test_task_processing():
    task = create_task(check_code=202)
    print('статус должэен быть Running')
    assert get_task_status(task.json(), check_code=200).json() == 'running'
    sleep(121)
    assert get_task_status(task.json(), check_code=200).json() == 'finished'
"на самом деле тут важно понимать как производиться процесс перевода задачи из статуса в статус Т.е. если процесс просто слипится на " \
"120 секунд а потом продолжает выполнение то тест можно считать корректным, если производиться разбор очередей по " \
"таймстампу воркером то на время выполнения перевода задачи в другой статус начнут влиять загрузка сервера и тест следует перевисать" \
"с учетом допустимых пределов" \


"тест на валидацию данных"
"coming soon"










