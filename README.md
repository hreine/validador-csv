# Validador de Archivos CSV

Este proyecto es una herramienta de línea de comandos en Python para validar la estructura y el contenido de archivos CSV contra un conjunto de reglas predefinidas.

## Aspectos Principales del Proyecto

*   **`validar_estructura.py`**: El script principal que se encarga de la lógica de validación.
*   **`estructuras.py`**: Define las estructuras de datos esperadas para los archivos CSV, incluyendo columnas, tipos de datos, y restricciones.
*   **`Archivos planos/`**: Directorio que contiene los archivos CSV de ejemplo para probar el validador.
*   **`Pipfile`**: Archivo de configuración para la gestión de dependencias con `pipenv`.

## Configuración del Entorno

1.  **Instalar `pipenv`**: Si no lo tienes instalado, puedes instalarlo con pip:
    ```bash
    pip install pipenv
    ```

2.  **Instalar dependencias**: Aunque este proyecto no tiene dependencias externas, puedes crear el entorno virtual con:
    ```bash
    pipenv install
    ```

## Uso y Pruebas

Para validar un archivo, ejecuta el script `validar_estructura.py` seguido del tipo de archivo a validar.

### 1. Probar un archivo CSV válido

Este caso utiliza el archivo `fic-archivo-ok.csv`, que cumple con todas las reglas de validación.

```bash
python validar_estructura.py fic_ok
```

**Salida esperada:**
```
Iniciando validación para el archivo: C:\...\Validador-Csv\Archivos planos\fic-archivo-ok.csv
La cabecera del archivo es válida.

--- Resumen de Validación ---
¡Validación completada con éxito! Se analizaron 4 filas sin errores.
--------------------------
```

### 2. Probar un archivo con error en la cabecera

Este caso utiliza `fic-error-cabecera.csv`, que tiene una cabecera incorrecta.

```bash
python validar_estructura.py fic_err_header
```

**Salida esperada:**
```
Iniciando validación para el archivo: C:\...\Validador-Csv\Archivos planos\fic-error-cabecera.csv

--- Resumen de Validación ---
Se encontraron errores en 1 de 1 filas analizadas.

Errores en la línea 1:
  - La cabecera no coincide. ...
--------------------------
```

### 3. Probar un archivo con campos obligatorios faltantes

Este caso utiliza `fic-error-obligatorio.csv`, donde faltan valores en campos que son obligatorios.

```bash
python validar_estructura.py fic_err_mandatory
```

**Salida esperada:**
```
Iniciando validación para el archivo: C:\...\Validador-Csv\Archivos planos\fic-error-obligatorio.csv
La cabecera del archivo es válida.

--- Resumen de Validación ---
Se encontraron errores en 1 de 2 filas analizadas.

Errores en la línea 2:
  - Columna 'ID_FONDO': Valor obligatorio ausente (valor: '')
  - Columna 'ID_CLASE': Valor obligatorio ausente (valor: '')
--------------------------
```

### 4. Probar un archivo con clave primaria duplicada

Este caso utiliza `fic-error-pk.csv`, que contiene valores duplicados en la columna definida como clave primaria.

```bash
python validar_estructura.py fic_err_pk
```

**Salida esperada:**
```
Iniciando validación para el archivo: C:\...\Validador-Csv\Archivos planos\fic-error-pk.csv
La cabecera del archivo es válida.

--- Resumen de Validación ---
Se encontraron errores en 1 de 4 filas analizadas.

Errores en la línea 3:
  - Llave primaria duplicada para la columna 'NUM_CUENTA': (valor: '111222333')
--------------------------
```

### 5. Probar un archivo con tipo de dato incorrecto

Este caso utiliza `fic-error-tipo-dato.csv`, que tiene un valor no numérico en una columna de tipo decimal.

```bash
python validar_estructura.py fic_err_datatype
```

**Salida esperada:**
```
Iniciando validación para el archivo: C:\...\Validador-Csv\Archivos planos\fic-error-tipo-dato.csv
La cabecera del archivo es válida.

--- Resumen de Validación ---
Se encontraron errores en 1 de 2 filas analizadas.

Errores en la línea 2:
  - Columna 'MONTO': No es un decimal válido (valor: 'esto no es un numero')
--------------------------
```
