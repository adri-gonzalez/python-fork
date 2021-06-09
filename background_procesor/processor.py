import os
import uuid
import pickle
from time import time, sleep

TASK_DIR = '/tmp/.processor-task-queue'

if not os.path.isdir(TASK_DIR):
    os.makedirs(TASK_DIR)


def add_task(func, args=[]):
    """
    agregar tareas para poder procesarlas por el id
    :param func:
    :param args:
    :return:
    """
    if not callable(func):
        raise Exception('Funcion por parametros invalida')

    task_ids = os.listdir(TASK_DIR)

    while True:
        task_id = str(uuid.uuid4())
        if task_id not in task_ids:
            break

    with open(task_file(task_id), 'wb') as f:
        pickle.dump({
            'id': task_id,
            'function': func,
            'function_args': args,
            'status': 'IDLE',
            'result': '',
            'start_time': 0,
            'end_time': 0
        }, f)

    return task_id


def run_task(task_id):
    """
    Ejecutar una tarea aplicando forks
    :param task_id:
    :return:
    """
    task_exists(task_id)

    with open(task_file(task_id), 'rb') as f:
        task_data = pickle.load(f)

    pid = os.fork()
    if not pid:
        func = task_data['function']
        func_args = task_data['function_args']

        with open(task_file(task_id), 'wb') as f:
            task_data['status'] = 'RUNNING'
            pickle.dump(task_data, f)

        task_data['start_time'] = int(time())
        try:
            result = func(*func_args)
        except Exception as e:
            result = 'Exception: %s' % str(e)

        with open(task_file(task_id), 'wb') as f:
            task_data['result'] = result
            task_data['status'] = 'COMPLETE'
            task_data['end_time'] = int(time())

            pickle.dump(task_data, f)

        os._exit(0)


def task_ready(task_id):
    """
    validar que la tarea se ha realizado
    :param task_id:
    :return:
    """
    task_exists(task_id)
    task_data = task_details(task_id)
    if task_data['status'] == 'COMPLETE':
        return True

    return False


def task_details(task_id):
    """
    obtener los detalles de una tarea basado en el id
    :param task_id:
    :return:
    """
    task_exists(task_id)
    return read_task_file(task_id)


def remove_task(task_id):
    """
    matar la tarea basada en id
    :param task_id:
    :return:
    """
    os.remove(task_file(task_id))
    return


def read_task_file(task_id, t=2):
    """
    leer el archivo de la tarea
    :param task_id:
    :param t:
    :return:
    """
    c = 1
    while True:
        try:
            with open(task_file(task_id), 'rb') as f:
                return pickle.load(f)
        except:
            sleep(1)
            if c >= t:
                break
            c += 1
            continue

    raise Exception('Could not open task file')


def task_exists(task_id):
    """
    validar que la task existe
    :param task_id:
    :return:
    """
    if not os.path.isfile(task_file(task_id)):
        raise Exception('Inexistent task')


def task_file(task_id):
    """
    retornar el path de la task
    :param task_id:
    :return:
    """
    return '%s/%s.task' % (TASK_DIR, task_id)
