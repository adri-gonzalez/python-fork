# Python os.fork()

## Que encontraremos aqui?

Dentro de python fork se encuentran los siguientes temas:

* 01-fork_method: explicacion programatica de que es/como funciona os.fork()
* 02-child_process: crear procesos hijos utilizando fork
* 03-multiple_process: crear multiples procesos utilizando fork y manejarlos con waitpid
* back_ground_procesor: Administrador de tareas/funciones utilizando procesos padres y procesos hijos
* web_server: un webserver para gestionar peticiones concurrentes utilizando os.fork

## BACKGROUND PROCCESSOR:

Para poder ejecutar el siguiente ejemplo pueden hacer lo siguiente

```
cd background_processor
python3 test_processor.py
```

## WEB SERVER

Dentro de este directorio encontraran:

* Un cliente client.py para simular las llamadas al web-server
* Un webserver simple que no soporta requests concurrentes simple_server.py
* Un webserver concurrente que utiliza fork para poder paralelizar las llamadas que recibe
* Un webserver concurrente, con manejo de errores, que tambien utiliza fork para poder paralelizar las llamadas que
  recibe

Para poder ejecutar el siguiente programa debemos primero en un terminal movernos al directorio del repositorio y correr
lo siguiente:


nos movemos al directiorio:
```
cd web_server
```

ejectuar el servidor simple:

```
python3 simple_server.py
```

ejectuar el servidor concurrente:

```
python3 concurrent_webserver.py
```

ejectuar el servidor concurrente con exepciones:

```
python3 concurrent_webserver_improved.py
```

una vez que tenemos nuestro server corriendo podemos correr el cliente para ver como os.fork maneja las diferentes
llamadas en paralelo:

```
python3 client.py --max-conns=1024 --max-clients=5
```
