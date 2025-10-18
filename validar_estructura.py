# -*- coding: utf-8 -*-
"""
Script parametrizado para validar la estructura y tipos de datos de archivos planos CSV.
"""
import csv
import os
import argparse
from datetime import datetime
from estructuras import VALIDATION_CONFIG

def validate_int(value, is_mandatory, max_len):
    """Valida si un valor es un entero válido con una longitud máxima."""
    if not value and not is_mandatory:
        return True, ""
    if not value and is_mandatory:
        return False, "Valor obligatorio ausente"
    try:
        value_str = str(value).strip()
        int(value_str)
        if max_len and len(value_str) > max_len:
            return False, f"Excede longitud máxima de {max_len}"
        return True, ""
    except (ValueError, TypeError):
        return False, "No es un entero válido"

def validate_decimal(value, is_mandatory, precision):
    """Valida si un valor cumple con una precisión decimal específica."""
    if not value and not is_mandatory:
        return True, ""
    if not value and is_mandatory:
        return False, "Valor obligatorio ausente"
    try:
        cleaned_value = str(value).strip()
        if ',' in cleaned_value and '.' not in cleaned_value:
            cleaned_value = cleaned_value.replace(',', '.')
        
        float(cleaned_value)
        parts = cleaned_value.split('.')
        integer_part_len = len(parts[0])
        decimal_part_len = len(parts[1]) if len(parts) > 1 else 0
        total_precision, scale = precision
        if integer_part_len > (total_precision - scale) or decimal_part_len > scale:
            return False, f"No cumple con la precisión Decimal({total_precision}, {scale})"
        return True, ""
    except (ValueError, TypeError):
        return False, "No es un decimal válido"

def validate_date(value, is_mandatory, date_format=None):
    """Valida si un valor tiene un formato de fecha correcto."""
    final_format = date_format if date_format is not None else '%Y-%m-%d'
    if not value and not is_mandatory:
        return True, ""
    if not value and is_mandatory:
        return False, "Valor obligatorio ausente"
    try:
        datetime.strptime(str(value), final_format)
        return True, ""
    except (ValueError, TypeError):
        return False, f"Formato de fecha inválido, se esperaba {final_format}"

def validate_varchar(value, is_mandatory, max_len):
    """Valida si un valor es una cadena de texto con una longitud máxima."""
    if not value and not is_mandatory:
        return True, ""
    if not value and is_mandatory:
        return False, "Valor obligatorio ausente"
    value_str = str(value)
    if max_len and len(value_str) > max_len:
        return False, f"Excede longitud máxima de {max_len}"
    return True, ""

def validate_bit(value, is_mandatory, max_len):
    """Valida si un valor es un bit (0 o 1)."""
    if not value and not is_mandatory:
        return True, ""
    if not value and is_mandatory:
        return False, "Valor obligatorio ausente"
    if str(value).strip() not in ('0', '1'):
        return False, "Valor debe ser 0 o 1"
    return True, ""

VALIDATORS = {
    'int': validate_int,
    'decimal': validate_decimal,
    'date': validate_date,
    'varchar': validate_varchar,
    'char': validate_varchar,
    'bit': validate_bit
}

def validate_csv(file_path, expected_columns, column_specs, primary_key=None):

    """

    Función principal que orquesta la validación de un archivo CSV.

    Recibe como parámetros la configuración de validación.

    """

    errors = []

    total_rows = 0

    primary_key_values = set()

    pk_col_index = -1



    if primary_key and primary_key in expected_columns:

        pk_col_index = expected_columns.index(primary_key)



    if not os.path.exists(file_path):

        print(f"Error: El archivo '{file_path}' no fue encontrado.")

        return



    with open(file_path, 'r', encoding='utf-8') as csvfile:

        reader = csv.reader(csvfile, delimiter=';')



        # 1. Validar cabecera

        try:

            header = next(reader)

            total_rows += 1



            if header != expected_columns:

                errors.append((1, [f"La cabecera no coincide. Esperado: {expected_columns}, Encontrado: {header}"]))

        except StopIteration:

            errors.append((1, ["Error: El archivo CSV está vacío."]))

            print_summary(errors, 0)

            return



        if any(e for line, e in errors if line == 1):

            print_summary(errors, total_rows)

            return

        else:

            print("La cabecera del archivo es válida.")



        # 2. Validar filas de datos

        for i, row in enumerate(reader, start=2):

            total_rows = i

            row_errors = []

            if len(row) != len(expected_columns):

                row_errors.append(f"Número incorrecto de columnas. Se esperaban {len(expected_columns)}, pero se encontraron {len(row)}.")

                errors.append((i, row_errors))

                continue



            # Validar llave primaria duplicada

            if pk_col_index != -1:

                pk_value = row[pk_col_index]

                if pk_value in primary_key_values:

                    row_errors.append(f"Llave primaria duplicada para la columna '{primary_key}': (valor: '{pk_value}')")

                else:

                    primary_key_values.add(pk_value)



            for col_name, value in zip(expected_columns, row):

                spec = column_specs[col_name]

                validator = VALIDATORS[spec[0]]

                is_valid, msg = validator(value, spec[1], spec[2])

                if not is_valid:

                    row_errors.append(f"Columna '{col_name}': {msg} (valor: '{value}')")



            if row_errors:

                errors.append((i, row_errors))



    print_summary(errors, total_rows)





def print_summary(errors, total_rows):

    """Imprime un resumen de los errores encontrados."""

    print("\n--- Resumen de Validación ---")

    if not errors:

        print(f"¡Validación completada con éxito! Se analizaron {total_rows} filas sin errores.")

    else:

        print(f"Se encontraron errores en {len(errors)} de {total_rows} filas analizadas.")

        for line_num, line_errors in errors[:10]: # Aumentado a 10 errores

            print(f"\nErrores en la línea {line_num}:")

            for error in line_errors:

                print(f"  - {error}")

        if len(errors) > 10:

            print(f"\n... y {len(errors) - 10} más filas con errores.")

    print("--------------------------")





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validador de estructura para archivos planos CSV.")
    parser.add_argument(
        'tipo_archivo',
        choices=VALIDATION_CONFIG.keys(),
        help=f"El tipo de archivo a validar. Opciones: {list(VALIDATION_CONFIG.keys())}"
    )
    args = parser.parse_args()

    config = VALIDATION_CONFIG[args.tipo_archivo]
    file_to_validate = config['archivo']
    expected_cols = config['columnas']
    col_specs = config['especificaciones']
    primary_key_col = config.get('primary_key') # Usar .get para evitar errores si no existe

    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, 'Archivos planos', file_to_validate)

        print(f"Iniciando validación para el archivo: {csv_path}")
        validate_csv(csv_path, expected_cols, col_specs, primary_key=primary_key_col)

    except NameError:
        # Manejo para entornos donde __file__ no está definido (ej. un notebook interactivo)
        # Asumimos que el script se ejecuta desde el directorio raíz del proyecto.
        csv_path = os.path.join('Archivos planos', file_to_validate)
        if os.path.exists(csv_path):
            print(f"Iniciando validación para el archivo: {csv_path}")
            validate_csv(csv_path, expected_cols, col_specs, primary_key=primary_key_col)
        else:
            print(f"Error: No se pudo encontrar el archivo {csv_path}. Asegúrate de ejecutar desde el directorio raíz del proyecto.")