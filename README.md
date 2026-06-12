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