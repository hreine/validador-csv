# -*- coding: utf-8 -*-
"""
Este módulo centraliza las definiciones de estructura para todos los archivos planos.
"""

# --- Configuraciones Ficticias ---

# 1. Estructura para fic-archivo-ok.csv y fic-archivo-err.csv
FIC_ARCHIVO_COLUMNAS = [
    'ID_FONDO', 'ID_CLASE', 'NUM_CUENTA', 'TIPO_DOC', 'NUM_DOC', 'COD_DIR', 'MONTO',
    'CANTIDAD', 'FECHA_APERTURA', 'FECHA_CIERRE', 'META_INVERSION', 'COD_ASESOR',
    'REFERENTE', 'ORIGEN_APERTURA', 'SUCURSAL', 'SUCURSAL_APERTURA', 'SUCURSAL_ACTUAL',
    'ESTADO_BLOQUEO', 'CAUSA_BLOQUEO', 'FECHA_VTO_ESTIMADA', 'FECHA_ULT_CIERRE', 'DIAS_ACTIVO'
]

FIC_ARCHIVO_ESPECIFICACIONES = {
    'ID_FONDO': ('varchar', True, 30),
    'ID_CLASE': ('varchar', True, 10),
    'NUM_CUENTA': ('varchar', True, 40),
    'TIPO_DOC': ('char', True, 10),
    'NUM_DOC': ('varchar', True, 30),
    'COD_DIR': ('int', True, None),
    'MONTO': ('decimal', True, (18, 2)),
    'CANTIDAD': ('decimal', True, (18, 6)),
    'FECHA_APERTURA': ('date', True, None),
    'FECHA_CIERRE': ('date', False, None),
    'META_INVERSION': ('int', True, None),
    'COD_ASESOR': ('varchar', False, 50),
    'REFERENTE': ('varchar', False, 50),
    'ORIGEN_APERTURA': ('varchar', True, 50),
    'SUCURSAL': ('varchar', True, None),
    'SUCURSAL_APERTURA': ('varchar', True, 6),
    'SUCURSAL_ACTUAL': ('varchar', True, 6),
    'ESTADO_BLOQUEO': ('bit', True, None),
    'CAUSA_BLOQUEO': ('int', False, None),
    'FECHA_VTO_ESTIMADA': ('date', False, None),
    'FECHA_ULT_CIERRE': ('date', False, None),
    'DIAS_ACTIVO': ('int', False, 4)
}

# --- Diccionario de Configuración Central ---
# Mapea un identificador de archivo a su configuración de validación.
VALIDATION_CONFIG = {
    'fic_ok': {
        'archivo': 'fic-archivo-ok.csv',
        'columnas': FIC_ARCHIVO_COLUMNAS,
        'especificaciones': FIC_ARCHIVO_ESPECIFICACIONES,
        'primary_key': 'NUM_CUENTA'
    },
    'fic_err': {
        'archivo': 'fic-archivo-err.csv',
        'columnas': FIC_ARCHIVO_COLUMNAS,
        'especificaciones': FIC_ARCHIVO_ESPECIFICACIONES,
        'primary_key': 'NUM_CUENTA'
    },
    'fic_err_header': {
        'archivo': 'fic-error-cabecera.csv',
        'columnas': FIC_ARCHIVO_COLUMNAS,
        'especificaciones': FIC_ARCHIVO_ESPECIFICACIONES,
        'primary_key': 'NUM_CUENTA'
    },
    'fic_err_datatype': {
        'archivo': 'fic-error-tipo-dato.csv',
        'columnas': FIC_ARCHIVO_COLUMNAS,
        'especificaciones': FIC_ARCHIVO_ESPECIFICACIONES,
        'primary_key': 'NUM_CUENTA'
    },
    'fic_err_mandatory': {
        'archivo': 'fic-error-obligatorio.csv',
        'columnas': FIC_ARCHIVO_COLUMNAS,
        'especificaciones': FIC_ARCHIVO_ESPECIFICACIONES,
        'primary_key': 'NUM_CUENTA'
    },
    'fic_err_pk': {
        'archivo': 'fic-error-pk.csv',
        'columnas': FIC_ARCHIVO_COLUMNAS,
        'especificaciones': FIC_ARCHIVO_ESPECIFICACIONES,
        'primary_key': 'NUM_CUENTA'
    }
}