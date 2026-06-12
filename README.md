# PEC 4 - Análisis de La Liga (1995-2025)
Mateu Carbonell Merino

## Estructura y organización de carpetas
El proyecto sigue una estructura modular para separar la lógica y los datos -> 
* `src/`: Contiene el código fuente principal.
  * `main.py`: Ejecuta toda la PEC de forma incremental importando los módulos de cada ejercicio.
  * `config.py`: Variables globales del proyecto.
  * `exercises/`: Módulos con la lógica de cada ejercicio (ex1.py, ex2.py etc...).
  * `data/`: Contiene el dataset original CSV.
  * `img/`: Gráficas generadas por el código.
* `tests/`: Scripts de validación (unittest).
* `doc/`: Documentación generada con pydoc.
* `screenshots/`: Capturas de pantalla de pylint y de pydoc.

## Instalación del proyecto
Para ejecutar este proyecto de forma segura, se debe crear un entorno virtual limpio e instalar las dependencias:
1. Crear el entorno virtual: `python3 -m venv .venv`
2. Activar el entorno: `source .venv/bin/activate` en mi caso o `.venv\Scripts\activate` si el dispositivo es Windows.
3. Instalar dependencias: `pip install -r requirements.txt`

## Ejecución del proyecto
El archivo principal admite ejecución incremental mediante el argumento `-ex`. Para ejecutar, por ejemplo, hasta el ejercicio 5:
```bash
python src/main.py -ex 5
```

## Análisis estático (Linting)
Para comprobar el código con pylint, teniendo en cuenta las reglas del archivo `.pylintrc`:
```bash
pylint src/
```

## Generar Documentación
Para generar los archivos HTML con la documentación y moverlos a su carpeta:
```bash
python -m pydoc -w src/main.py src/config.py src/exercises/ex1.py src/exercises/ex2.py src/exercises/ex3.py src/exercises/ex4.py src/exercises/ex5.py src/exercises/ex6.py src/exercises/ex7.py
mv *.html doc/
```

## Ejecutar el Test
Para comprobar que la función de suma de goles del ejercicio 6 funciona correctamente:
```bash
python -m unittest tests/tests_ex6.py
```

## Comandos para subir a GitHub
Pasos en la terminal para subir este proyecto a un repositorio nuevo:
```bash
git init
git add .
git commit -m "Entrega PEC4"
git branch -M main
git remote add origin <URL_DEL_REPOSITORIO>
git push -u origin main
```