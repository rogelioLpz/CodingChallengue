# Coding Challenge: Rogelio Lòpez
API Rest creada en Flask (python) con conexiòn a PostgreSQL.
Solucion emaquetada en docker utilizando docker-compose


### Prerequisitos

Tener instalado [Docker](https://docs.docker.com/install/) y [Docker Compose](https://docs.docker.com/compose/install/)


### Iniciar proyecto

Contruir imagenes propias requeridas para docker compose 

```
docker-compose build
```

Posteriormente iniciar los servicios

```
docker-compose up
```

## Validar servicios

Una vez que los servicios esten activos y listos para aceptar peticiones es posible validarlos


### API Rest Flask (Python)

Realizar una solicitud GET al servicio expuesto en la red Docker creada.

```
GET: http://172.28.1.2:5000/api/v1/puzzle_queens/4
```

El parametro "4" indica el nùmero de reinas que se deseen colocar.


El resultado  muestra el nùmero de soluciones al problema de las n reinas y una lista con las soluciones.

```
{
	"n_solutions":2,
	"solutions":[
		{"0":1,"1":3,"2":0,"3":2},
		{"0":2,"1":0,"2":3,"3":1}
	]
}
```

En la distribuciòn del tablero de las soluciones se indica la fila y columna de cada reina (Indices inician en 0)

### Validar Base de Datos

Conectarse con el cliente de su preferencia a la BD. Ejemplo con psql

```
psql 'host=172.28.1.3 port=5432 dbname=cuenca_db user=rlopez'
```

Utilzando el password "admin" ejecutar la siguiente consulta


```
select * from "SolucionReina";
```

Las soluciones de las ejecuciones del servicio deben encontrarse ahora en BD


### Persistencia de datos
Destruir los servicios docker con el siguiente comando

```
docker-compose down
```

Volver a generar servicios con el comando

```
docker-compose up
```

Conectarse nuevamente a BD y comprobar existencia de los datos previos


## Pruebas Unitarias manuales

Dentro del directorio ejecutar el comando

```
python -m unittest
```

Observar la ejecuciòn correcta de las pruebas (Número de soluciones del algoritmo)