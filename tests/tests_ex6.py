"""
Módulo de pruebas para el Ejercicio 6.
"""
import unittest
import pandas as pd
import sys
import os

# Truco para que Python encuentre la carpeta 'src' desde la carpeta 'tests'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from exercises.ex6 import fun_total_goals

class TestEx6(unittest.TestCase):
    """Clase que contiene los tests del Ejercicio 6."""
    
    def test_fun_total_goals(self):
        """Comprueba que la suma de goles locales, visitantes y totales es correcta."""
        # 1. Preparamos un DataFrame de prueba ("dummy data") muy sencillo
        datos_prueba = pd.DataFrame({
            'FTHG': [2, 1, 0],  # Goles en casa: 2 + 1 + 0 = 3
            'FTAG': [1, 0, 2]   # Goles fuera: 1 + 0 + 2 = 3
        })
        
        # 2. Ejecutamos la función que queremos probar
        home, away, total = fun_total_goals(datos_prueba)
        
        # 3. Comprobamos (assert) que el resultado es exactamente el esperado
        self.assertEqual(home, 3, "Los goles locales deberían ser 3")
        self.assertEqual(away, 3, "Los goles visitantes deberían ser 3")
        self.assertEqual(total, 6, "Los goles totales deberían ser 6")

if __name__ == '__main__':
    unittest.main()