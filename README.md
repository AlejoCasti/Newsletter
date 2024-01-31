# Periodico a la mano

En este proyecto se trabaja el envio de periodico por medio de correos electronicos. Desde el administrador se puede crear un periodico, establecer los correos receptores y un archivo adjunto de máximo 10MB (PNG, PDF).
Tambien se listan los correos y tienen la opción de ser enviados despues de su creación.\n
Tambien se pueden ver datos básicos como correos enviados, usuarios activos, desuscripciones y tasa de desuscripción.

## Técnica

Las técnologias que se utilizan son:
### Front
Se utiliza Javascript junto con un framework Vue js. Desde el front se hizo integración con AWS S3 para almacenamiento de archivos.

### Back
Con el fin de satisfacer uno de los requerimientos se hace con Python y un framework Django.
Se utiliza la libreria Rest framework para la creación del Api. Por otro lado se hace integración con AWS SES para el envío de correo pero no da un buen resultado y se termina utilizando una conexión con la dirección personal de gmail.
## :warning: Importante: El correo puede llegar a spam.

Para Base de datos se utiliza postgres con un modelo muy sencillo.
![Screenshot 2024-01-31 at 6 10 43 PM](https://github.com/AlejoCasti/Newsletter/assets/37104762/65183f0e-4320-42bf-a58a-f1181146bf2b)

## Instalación
Necesario tener docker para su ejecución

1. Clona este repositorio: `git clone https://github.com/AlejoCasti/Newsletter.git`
2. Ve al directorio del proyecto: `cd Newsletter`
3. Renombra el archivo .env-template a .env
4. Ejecuta el docker compose: `docker compose up`

### Puertos
Front = 5173
Back = 8000
DB = 5432
