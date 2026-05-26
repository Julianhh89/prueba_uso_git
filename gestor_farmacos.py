"""
Gestor de Base de Datos de Fármacos Aprobados
Script para gestionar, consultar y manipular la base de datos de fármacos
"""

import csv
import json
from typing import List, Dict
from pathlib import Path


class GestorFarmacos:
    """Clase para gestionar la base de datos de fármacos aprobados"""
    
    def __init__(self, archivo_csv: str = "datos_farmacos.csv"):
        """
        Inicializa el gestor con el archivo CSV de fármacos
        
        Args:
            archivo_csv: Ruta del archivo CSV con los datos
        """
        self.archivo_csv = archivo_csv
        self.farmacos: List[Dict] = []
        self.cargar_datos()
    
    def cargar_datos(self) -> None:
        """Carga los datos del archivo CSV"""
        try:
            with open(self.archivo_csv, 'r', encoding='utf-8') as f:
                lector = csv.DictReader(f)
                self.farmacos = list(lector)
            print(f"✓ Se cargaron {len(self.farmacos)} fármacos correctamente")
        except FileNotFoundError:
            print(f"✗ Error: No se encontró el archivo {self.archivo_csv}")
    
    def buscar_por_nombre(self, nombre: str) -> List[Dict]:
        """
        Busca fármacos por nombre comercial o genérico
        
        Args:
            nombre: Nombre a buscar
            
        Returns:
            Lista de fármacos coincidentes
        """
        nombre_lower = nombre.lower()
        resultados = [
            f for f in self.farmacos 
            if nombre_lower in f['nombre_comercial'].lower() or 
               nombre_lower in f['nombre_generico'].lower()
        ]
        return resultados
    
    def buscar_por_indicacion(self, indicacion: str) -> List[Dict]:
        """
        Busca fármacos por indicación terapéutica
        
        Args:
            indicacion: Indicación a buscar
            
        Returns:
            Lista de fármacos con esa indicación
        """
        indicacion_lower = indicacion.lower()
        resultados = [
            f for f in self.farmacos 
            if indicacion_lower in f['indicacion'].lower()
        ]
        return resultados
    
    def buscar_por_laboratorio(self, laboratorio: str) -> List[Dict]:
        """
        Busca fármacos por laboratorio
        
        Args:
            laboratorio: Nombre del laboratorio
            
        Returns:
            Lista de fármacos del laboratorio
        """
        laboratorio_lower = laboratorio.lower()
        resultados = [
            f for f in self.farmacos 
            if laboratorio_lower in f['laboratorio'].lower()
        ]
        return resultados
    
    def obtener_farmaco_por_id(self, farmaco_id: str) -> Dict:
        """
        Obtiene un fármaco por su ID
        
        Args:
            farmaco_id: ID del fármaco
            
        Returns:
            Diccionario con los datos del fármaco
        """
        for f in self.farmacos:
            if f['id'] == farmaco_id:
                return f
        return {}
    
    def listar_todos(self) -> None:
        """Lista todos los fármacos en la base de datos"""
        print("\n" + "="*80)
        print("FÁRMACOS APROBADOS EN BASE DE DATOS")
        print("="*80)
        for f in self.farmacos:
            print(f"\n[ID {f['id']}] {f['nombre_comercial']} ({f['nombre_generico']})")
            print(f"  Laboratorio: {f['laboratorio']}")
            print(f"  Indicación: {f['indicacion']}")
            print(f"  Presentación: {f['presentacion']}")
            print(f"  Dosis recomendada: {f['dosis_recomendada']}")
    
    def exportar_json(self, archivo_salida: str = "farmacos.json") -> None:
        """
        Exporta la base de datos a formato JSON
        
        Args:
            archivo_salida: Nombre del archivo JSON de salida
        """
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            json.dump(self.farmacos, f, ensure_ascii=False, indent=2)
        print(f"✓ Base de datos exportada a {archivo_salida}")
    
    def agregar_farmaco(self, datos_farmaco: Dict) -> None:
        """
        Agrega un nuevo fármaco a la base de datos
        
        Args:
            datos_farmaco: Diccionario con los datos del fármaco
        """
        self.farmacos.append(datos_farmaco)
        print(f"✓ Fármaco '{datos_farmaco['nombre_comercial']}' agregado correctamente")
    
    def obtener_estadisticas(self) -> Dict:
        """
        Obtiene estadísticas de la base de datos
        
        Returns:
            Diccionario con estadísticas
        """
        laboratorios = set(f['laboratorio'] for f in self.farmacos)
        indicaciones = set(f['indicacion'] for f in self.farmacos)
        
        return {
            'total_farmacos': len(self.farmacos),
            'laboratorios_unicos': len(laboratorios),
            'indicaciones_unicas': len(indicaciones),
            'laboratorios': list(laboratorios),
            'indicaciones': list(indicaciones)
        }


def main():
    """Función principal para demostrar el uso del gestor"""
    
    # Inicializar el gestor
    gestor = GestorFarmacos("datos_farmacos.csv")
    
    # Ejemplos de uso
    print("\n--- BÚSQUEDA POR NOMBRE ---")
    resultados = gestor.buscar_por_nombre("Aspirin")
    for f in resultados:
        print(f"✓ Encontrado: {f['nombre_comercial']} - {f['nombre_generico']}")
    
    print("\n--- BÚSQUEDA POR INDICACIÓN ---")
    resultados = gestor.buscar_por_indicacion("Hipertension")
    for f in resultados:
        print(f"✓ {f['nombre_comercial']}: {f['indicacion']}")
    
    print("\n--- BÚSQUEDA POR LABORATORIO ---")
    resultados = gestor.buscar_por_laboratorio("Pfizer")
    for f in resultados:
        print(f"✓ {f['nombre_comercial']} - Pfizer")
    
    print("\n--- ESTADÍSTICAS ---")
    stats = gestor.obtener_estadisticas()
    print(f"Total de fármacos: {stats['total_farmacos']}")
    print(f"Laboratorios únicos: {stats['laboratorios_unicos']}")
    print(f"Indicaciones únicas: {stats['indicaciones_unicas']}")
    
    # Listar todos
    gestor.listar_todos()
    
    # Exportar a JSON
    gestor.exportar_json()


if __name__ == "__main__":
    main()
