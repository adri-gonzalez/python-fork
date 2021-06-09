from time import sleep
from background_procesor import processor


def long_task(arg1, arg2):
    sleep(5)
    return 'Tarea larga con argumentos %s, %s ha terminado!' % (arg1, arg2)


def test_run():
    task_id = processor.add_task(long_task, ['myarg1', 'myarg2'])
    processor.run_task(task_id)
    print('Tarea %s iniciada...' % task_id)

    # Hacer cosas mientras la tarea corre
    for _ in range(10):
        print('Realizar cosas mientras la tarea corre %i' % (_ + 1))
        sleep(0.1)

    while True:  # Esperar hasta que la tarea este completa
        # Hacer otras cosas mientras la tarea corree
        print('Esperando hasta que la tarea este finalizada...')
        sleep(0.5)
        if processor.task_ready(task_id):
            break

    task_details = processor.task_details(task_id)

    print(
        'Tomo %i segundos para que la tarea termine %s' % (
            task_details['end_time'] - task_details['start_time'],
            task_details['result']
        )
    )

    processor.remove_task(task_id)


test_run()
