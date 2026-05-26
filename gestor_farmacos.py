import csv
import json
from datetime import datetime
from typing import List, Dict, Optional

class GestorFarmacos:
    """
    Gestor de base de datos de fármacos aprobados.
    Permite buscar, agregar y exportar información de medicamentos.
    """
    
    def __init__(self, archivo_csv: str = 'datos_farmacos.csv'):
        """Inicializa el gestor con un archivo CSV."""
        self.archivo_csv = archivo_csv
        self.farmacos: List[Dict] = []
        self.cargar_datos()
    
    def cargar_datos(self) -> None:
        """Carga los datos del archivo CSV."""
        try:
            with open(self.archivo_csv, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.farmacos = list(reader)
            print(f"✓ {len(self.farmacos)} fármacos cargados correctamente.")
        except FileNotFoundError:
            print(f"Error: Archivo {self.archivo_csv} no encontrado.")
            self.farmacos = []
    
    def buscar_por_nombre(self, nombre: str) -> List[Dict]:
        """Busca fármacos por nombre comercial o genérico."""
        nombre_lower = nombre.lower()
        resultados = [f for f in self.farmacos 
                     if nombre_lower in f['nombre_comercial'].lower() 
                     or nombre_lower in f['nombre_generico'].lower()]
        return resultados
    
    def buscar_por_indicacion(self, indicacion: str) -> List[Dict]:
        """Busca fármacos por indicación terapéutica."""
        indicacion_lower = indicacion.lower()
        return [f for f in self.farmacos 
                if indicacion_lower in f['indicacion'].lower()]
    
    def buscar_por_laboratorio(self, laboratorio: str) -> List[Dict]:
        """Busca fármacos por laboratorio fabricante."""
        laboratorio_lower = laboratorio.lower()
        return [f for f in self.farmacos 
                if laboratorio_lower in f['laboratorio'].lower()]
    
    def obtener_por_id(self, id_farmaco: str) -> Optional[Dict]:
        """Obtiene un fármaco específico por ID."""
        for f in self.farmacos:
            if f['id'] == id_farmaco:
                return f
        return None
    
    def listar_todos(self) -> List[Dict]:
        """Lista todos los fármacos."""
        return self.farmacos
    
    def agregar_farmaco(self, nuevo_farmaco: Dict) -> bool:
        """Agrega un nuevo fármaco a la base de datos."""
        try:
            # Validar que tenga los campos requeridos
            campos_requeridos = ['nombre_comercial', 'nombre_generico', 'laboratorio', 
                               'indicacion', 'presentacion', 'dosis_recomendada']
            if not all(campo in nuevo_farmaco for campo in campos_requeridos):
                print("Error: Faltan campos requeridos.")
                return False
            
            # Asignar nuevo ID
            nuevo_id = str(int(max(f['id'] for f in self.farmacos)) + 1)
            nuevo_farmaco['id'] = nuevo_id
            nuevo_farmaco['fecha_aprobacion'] = datetime.now().strftime('%Y-%m-%d')
            
            self.farmacos.append(nuevo_farmaco)
            self.guardar_datos()
            print(f"✓ Fármaco agregado con ID: {nuevo_id}")
            return True
        except Exception as e:
            print(f"Error al agregar fármaco: {e}")
            return False
    
    def guardar_datos(self) -> bool:
        """Guarda los datos en el archivo CSV."""
        try:
            if not self.farmacos:
                return False
            
            campos = self.farmacos[0].keys()
            with open(self.archivo_csv, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
                writer.writerows(self.farmacos)
            print("✓ Datos guardados correctamente.")
            return True
        except Exception as e:
            print(f"Error al guardar datos: {e}")
            return False
    
    def exportar_a_json(self, archivo_salida: str = 'farmacos.json') -> bool:
        """Exporta los datos a formato JSON."""
        try:
            with open(archivo_salida, 'w', encoding='utf-8') as f:
                json.dump(self.farmacos, f, indent=2, ensure_ascii=False)
            print(f"✓ Datos exportados a {archivo_salida}")
            return True
        except Exception as e:
            print(f"Error al exportar a JSON: {e}")
            return False
    
    def estadisticas(self) -> Dict:
        """Genera estadísticas de la base de datos."""
        laboratorios = {}
        indicaciones = {}
        
        for f in self.farmacos:
            lab = f['laboratorio']
            ind = f['indicacion']
            laboratorios[lab] = laboratorios.get(lab, 0) + 1
            indicaciones[ind] = indicaciones.get(ind, 0) + 1
        
        return {
            'total_farmacos': len(self.farmacos),
            'total_laboratorios': len(laboratorios),
            'laboratorios': laboratorios,
            'total_indicaciones': len(indicaciones),
            'indicaciones': indicaciones
        }
    
    def mostrar_farmaco(self, farmaco: Dict) -> None:
        """Muestra información detallada de un fármaco."""
        print("\n" + "="*60)
        print(f"ID: {farmaco['id']}")
        print(f"Nombre Comercial: {farmaco['nombre_comercial']}")
        print(f"Nombre Genérico: {farmaco['nombre_generico']}")
        print(f"Laboratorio: {farmaco['laboratorio']}")
        print(f"Indicación: {farmaco['indicacion']}")
        print(f"Presentación: {farmaco['presentacion']}")
        print(f"Dosis: {farmaco['dosis_recomendada']}")
        print(f"Efectos Adversos: {farmaco['efectos_adversos']}")
        print(f"Contraindicaciones: {farmaco['contraindicaciones']}")
        print("="*60 + "\n")


def menu_interactivo():
    """Menú interactivo para gestionar fármacos."""
    gestor = GestorFarmacos()
    
    while True:
        print("\n📋 GESTOR DE FÁRMACOS APROBADOS")
        print("="*40)
        print("1. Buscar por nombre")
        print("2. Buscar por indicación")
        print("3. Buscar por laboratorio")
        print("4. Ver todos los fármacos")
        print("5. Ver estadísticas")
        print("6. Exportar a JSON")
        print("7. Agregar nuevo fármaco")
        print("8. Salir")
        print("="*40)
        
        opcion = input("Seleccione una opción (1-8): ").strip()
        
        if opcion == '1':
            nombre = input("Ingrese el nombre del fármaco: ").strip()
            resultados = gestor.buscar_por_nombre(nombre)
            if resultados:
                print(f"\n✓ Se encontraron {len(resultados)} resultado(s):")
                for f in resultados:
                    gestor.mostrar_farmaco(f)
            else:
                print("✗ No se encontraron resultados.")
        
        elif opcion == '2':
            indicacion = input("Ingrese la indicación: ").strip()
            resultados = gestor.buscar_por_indicacion(indicacion)
            if resultados:
                print(f"\n✓ Se encontraron {len(resultados)} resultado(s):")
                for f in resultados:
                    gestor.mostrar_farmaco(f)
            else:
                print("✗ No se encontraron resultados.")
        
        elif opcion == '3':
            laboratorio = input("Ingrese el laboratorio: ").strip()
            resultados = gestor.buscar_por_laboratorio(laboratorio)
            if resultados:
                print(f"\n✓ Se encontraron {len(resultados)} resultado(s):")
                for f in resultados:
                    gestor.mostrar_farmaco(f)
            else:
                print("✗ No se encontraron resultados.")
        
        elif opcion == '4':
            print("\n📋 LISTA DE TODOS LOS FÁRMACOS:")
            for f in gestor.listar_todos():
                print(f"ID: {f['id']} | {f['nombre_comercial']} ({f['nombre_generico']}) | {f['laboratorio']}")
        
        elif opcion == '5':
            stats = gestor.estadisticas()
            print("\n📊 ESTADÍSTICAS:")
            print(f"Total de fármacos: {stats['total_farmacos']}")
            print(f"Total de laboratorios: {stats['total_laboratorios']}")
            print(f"Total de indicaciones: {stats['total_indicaciones']}")
            print("\nFármacos por laboratorio:")
            for lab, cant in stats['laboratorios'].items():
                print(f"  - {lab}: {cant}")
        
        elif opcion == '6':
            gestor.exportar_a_json()
        
        elif opcion == '7':
            print("\n➕ AGREGAR NUEVO FÁRMACO")
            nuevo_farmaco = {
                'nombre_comercial': input("Nombre comercial: ").strip(),
                'nombre_generico': input("Nombre genérico: ").strip(),
                'laboratorio': input("Laboratorio: ").strip(),
                'indicacion': input("Indicación: ").strip(),
                'presentacion': input("Presentación: ").strip(),
                'dosis_recomendada': input("Dosis recomendada: ").strip(),
                'efectos_adversos': input("Efectos adversos: ").strip(),
                'contraindicaciones': input("Contraindicaciones: ").strip()
            }
            gestor.agregar_farmaco(nuevo_farmaco)
        
        elif opcion == '8':
            print("\n¡Hasta luego!")
            break
        
        else:
            print("✗ Opción no válida. Intente de nuevo.")


if __name__ == '__main__':
    menu_interactivo()
