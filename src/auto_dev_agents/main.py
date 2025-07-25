#!/usr/bin/env python
import sys
import warnings
import os
import yaml
from datetime import datetime

from .crew import EngineeringTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Crear directorio de salida si no existe
os.makedirs('output', exist_ok=True)


def cargar_configuracion(path_config):
    with open(path_config, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def run():
    """
    Crea la tripulación usando la configuración de un archivo YAML
    """
    config = cargar_configuracion('prompt.yaml')
    # Se espera que el YAML tenga las claves: requirements, module_name, class_name
    inputs = {
        'requirements': config['requirements'],
        'module_name': config['module_name'],
        'class_name': config['class_name']
    }

    # Crear y ejecutar la crew
    result = EngineeringTeam().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()