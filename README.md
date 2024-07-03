# UNETI: POR FAVOR LEER README DIRIGIDO AL PROFESOR

 ## PROGRAMACION I_M2
 ## PROFESOR: CARLOS MÁRQUEZ
 ## ALUMNO: ERICK GILMORE
 ## CI: 27225952

### PROYECTO PAGINA WEB

Este repositorio contiene el proyecto del aplicativo web que sera evaluado 
durante este modulo de la materia.

Este es el primer commit del repositorio donde se muestra el frontend del aplicativo
con las tecnologias a evaluar de la Sesion didactica 1:

- HTML
- CSS
- BOOTSTRAP
- FLASK

Tome como tema de mi pagina el de simular la pagina web de la sucursal de BMW en 
Venezuela "NO EXISTE ;) TAL SUCURSAL"

Para llevar concordancia con el tema de un registro estudiantil, la pagina cuenta
con un apartado llamado Academy donde, estudiantes universitarios de las carreras
relacionadas con la informatica, electronica, mecatronica y mecanica podran postularse
para recibir formación y certificación tecnica de parte de los mejores tutores de la BMW.

# Para iniciar el aplicativo puede usar docker siguiendo los pasos:
### Clone el repositorio o descarguelo como ZIP y extraigalo
git clone https://github.com/Erickrgb22/CRUD_WEBAPP.git

# NOTA CREE UNA CARPETA EN LA RAIZ DEL PROYECTO CON NOMBRE "db" EN MINUSCULAS ANTES DE CONTINUAR DOCKER LA USA PARA GUARDAR LAS TABLAS 

### Con este comando construira el contenedor del aplicativo 
docker-compose build

### Con este comando creara 2 conenedores uno con el aplicativo y otro con su base de datos y estaria dispobible el aplicativo accede mediante:
localhost:5000

docker-compose up

# Puede iniciar el aplicativo solo con python y usando una base de datos externa (OPCIONAL)
Para ello debe ejecutar el script SQL que esta en la carpeta Scripts
para crear la tabla de estudiantes con el formato correcto sobre su base de datos MariaDB

Luego debe modificar el campo HOST dentro del archivo database.py, para que se connecte a la ip de su base de datos

Seguido de ese paso debe iniciar el venv de python que ejecutando "source .venv/bin/activate" usando bash en linux
Luego con python backend.py inicia el backend 

# Estructura de carpetas del proyecto
![2024-07-03-120138_hyprshot](https://github.com/Erickrgb22/E-SD1-PIM2_PROYECTOWEB_V27225952/assets/45826601/a22e4644-f8f4-4066-9240-d415bcfdc5e9)


# Archivos de Interes

### Backend de Flask: backend.py
### Conexion con SQL: database.py (no modificar si usa docker)
### Hoja de estilo CSS: /static/styes.css (Le faltan comentarios alli estan todas las animaciones que se ven en las vistas de la pagina con los @keywords)
### Pagina Inicial: /templates/index.html
### Pagina de Registro de Estudiantes: /templates/academy.html (Falto añadir verificacion de data y selecion de Cursos por lista desplegable)
### Script para crear tabla SQL: /scripts/init.sql
