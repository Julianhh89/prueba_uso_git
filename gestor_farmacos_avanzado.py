"""
Gestor Avanzado de Base de Datos de Fármacos - REPOSICIONAMIENTO
Script para gestionar, analizar y buscar fármacos con información para reposicionamiento
Versión 2.0 - Funciones avanzadas
"""

import csv
import json
import pandas as pd
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from collections import Counter
import re

class GestorFarmacosAvanzado:
    """
    Gestor avanzado de base de datos de fármacos aprobados.
    Especializado en análisis para reposicionamiento (drug repositioning)
    """
    
    def __init__(self, archivo_csv: str = 'farmacos_completa.csv'):
        """Inicializa el gestor con datos completos de fármacos."""
        self.archivo_csv = archivo_csv
        self.farmacos: List[Dict] = []
        self.df = None
        self.cargar_datos()
    
    def cargar_datos(self) -> None:
        """Carga los datos del archivo CSV."""
        try:
            with open(self.archivo_csv, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.farmacos = list(reader)
            self.df = pd.DataFrame(self.farmacos)
            print(f"✓ Se cargaron {len(self.farmacos)} fármacos correctamente")
        except FileNotFoundError:
            print(f"Error: Archivo {self.archivo_csv} no encontrado.")
            self.farmacos = []
    
    # ========== BÚSQUEDAS BÁSICAS ==========
    
    def buscar_por_nombre(self, nombre: str) -> List[Dict]:
        """Busca fármacos por nombre comercial o genérico."""
        nombre_lower = nombre.lower()
        return [f for f in self.farmacos 
                if nombre_lower in f['nombre_comercial'].lower() 
                or nombre_lower in f['nombre_generico'].lower()]
    
    def buscar_por_indicacion(self, indicacion: str) -> List[Dict]:
        """Busca fármacos por indicación terapéutica (principal o secundaria)."""
        indicacion_lower = indicacion.lower()
        return [f for f in self.farmacos 
                if indicacion_lower in f['indicacion_principal'].lower()
                or indicacion_lower in f['indicaciones_secundarias'].lower()]
    
    def buscar_por_laboratorio(self, laboratorio: str) -> List[Dict]:
        """Busca fármacos por laboratorio."""
        laboratorio_lower = laboratorio.lower()
        return [f for f in self.farmacos 
                if laboratorio_lower in f['laboratorio'].lower()]
    
    def buscar_por_clase_terapeutica(self, clase: str) -> List[Dict]:
        """Busca fármacos por clase terapéutica."""
        clase_lower = clase.lower()
        return [f for f in self.farmacos 
                if clase_lower in f['clase_terapeutica'].lower()]
    
    # ========== ANÁLISIS DE REPOSICIONAMIENTO ==========
    
    def farmacos_con_potencial_reposicionamiento(self) -> List[Dict]:
        """Retorna fármacos con potencial de reposicionamiento documentado."""
        return [f for f in self.farmacos 
                if f['potencial_reposicionamiento'] != 'No aplica']
    
    def analizar_mecanismo_de_accion(self, mecanismo: str) -> List[Dict]:
        """Encuentra fármacos que comparten mecanismos de acción similares."""
        mecanismo_lower = mecanismo.lower()
        return [f for f in self.farmacos 
                if mecanismo_lower in f['mecanismo_accion'].lower()]
    
    def farmacos_por_vias_metabolicas_comunes(self) -> Dict[str, List[Dict]]:
        """Agrupa fármacos por vías metabólicas similares (CYP450)."""
        grupos_metabolicos = {}
        for farmaco in self.farmacos:
            cyp = re.findall(r'CYP\d[A-Z]\d+', farmaco['farmacocinética'])
            for enzyme in cyp:
                if enzyme not in grupos_metabolicos:
                    grupos_metabolicos[enzyme] = []
                grupos_metabolicos[enzyme].append(farmaco)
        return grupos_metabolicos
    
    def interacciones_potenciales_con(self, nombre_farmaco: str) -> List[Tuple[str, str]]:
        """Identifica posibles interacciones de un fármaco con otros."""
        farmaco = self.buscar_por_nombre(nombre_farmaco)
        if not farmaco:
            return []
        
        farmaco = farmaco[0]
        interacciones_registradas = farmaco['interacciones_importantes'].split('; ')
        farmacos_similares = []
        
        for f in self.farmacos:
            if f['nombre_comercial'] != farmaco['nombre_comercial']:
                for interaccion in interacciones_registradas:
                    if interaccion.lower() in f['nombre_generico'].lower():
                        farmacos_similares.append((f['nombre_comercial'], interaccion))
        
        return farmacos_similares
    
    # ========== ANÁLISIS DE INDICACIONES SECUNDARIAS ==========
    
    def buscar_indicacion_secundaria(self, indicacion: str) -> List[Dict]:
        """Busca fármacos cuya indicación secundaria podría ser de interés."""
        indicacion_lower = indicacion.lower()
        return [f for f in self.farmacos 
                if indicacion_lower in f['indicaciones_secundarias'].lower()]
    
    def indicaciones_no_aprobadas_por_uso_compasivo(self) -> Dict[str, List[str]]:
        """Agrupa posibles usos compasivos por indicación."""
        usos_potenciales = {}
        palabras_clave_reposicionamiento = ['cáncer', 'alzheimer', 'parkinson', 'covid', 'sepsis', 
                                            'inflamación', 'diabetes', 'fibrosis', 'autoinmune']
        
        for farmaco in self.farmacos:
            reposicionamiento = farmaco['potencial_reposicionamiento'].lower()
            for palabra in palabras_clave_reposicionamiento:
                if palabra in reposicionamiento:
                    if palabra not in usos_potenciales:
                        usos_potenciales[palabra] = []
                    usos_potenciales[palabra].append(farmaco['nombre_comercial'])
        
        return usos_potenciales
    
    # ========== ANÁLISIS CLÍNICO AVANZADO ==========
    
    def perfil_seguridad(self, nombre_farmaco: str) -> Dict:
        """Analiza el perfil de seguridad de un fármaco."""
        farmaco = self.buscar_por_nombre(nombre_farmaco)
        if not farmaco:
            return {}
        
        farmaco = farmaco[0]
        efectos = farmaco['efectos_adversos'].split('; ')
        contraindicaciones = farmaco['contraindicaciones'].split('; ')
        
        return {
            'nombre': farmaco['nombre_comercial'],
            'efectos_adversos_principales': efectos[:3],
            'contraindicaciones': contraindicaciones,
            'via_administracion': farmaco['via_administracion'],
            'riesgo_general': 'ALTO' if len(efectos) > 5 else 'MODERADO' if len(efectos) > 3 else 'BAJO'
        }
    
    def farmacos_para_poblaciones_especiales(self, poblacion: str) -> List[Dict]:
        """Recomienda fármacos seguros para poblaciones especiales."""
        poblacion_lower = poblacion.lower()
        
        restricciones = {
            'embarazo': 'embarazo',
            'lactancia': 'lactancia',
            'renal': 'insuficiencia renal',
            'hepatica': 'hepática',
            'ancianos': 'anciano'
        }
        
        if poblacion_lower not in restricciones:
            return []
        
        restriccion = restricciones[poblacion_lower]
        no_recomendados = [f for f in self.farmacos 
                          if restriccion.lower() in f['contraindicaciones'].lower()]
        
        return [f for f in self.farmacos if f not in no_recomendados]
    
    # ========== ANÁLISIS DE DATOS ==========
    
    def estadisticas_completas(self) -> Dict:
        """Genera estadísticas completas de la base de datos."""
        laboratorios = Counter(f['laboratorio'] for f in self.farmacos)
        clases = Counter(f['clase_terapeutica'] for f in self.farmacos)
        vias = Counter(f['via_administracion'] for f in self.farmacos)
        
        farmacos_reposicionamiento = len(self.farmacos_con_potencial_reposicionamiento())
        
        return {
            'total_farmacos': len(self.farmacos),
            'laboratorios_unicos': len(laboratorios),
            'clases_terapeuticas': len(clases),
            'farmacos_reposicionamiento': farmacos_reposicionamiento,
            'porcentaje_reposicionamiento': f"{(farmacos_reposicionamiento/len(self.farmacos)*100):.1f}%",
            'laboratorios_top_5': dict(laboratorios.most_common(5)),
            'clases_top_5': dict(clases.most_common(5)),
            'vias_administracion': dict(vias)
        }
    
    # ========== EXPORTACIÓN Y REPORTES ==========
    
    def exportar_para_analisis(self, formato: str = 'json') -> str:
        """Exporta datos en diferentes formatos para análisis."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if formato == 'json':
            archivo = f"farmacos_analisis_{timestamp}.json"
            with open(archivo, 'w', encoding='utf-8') as f:
                json.dump(self.farmacos, f, indent=2, ensure_ascii=False)
        
        elif formato == 'csv':
            archivo = f"farmacos_analisis_{timestamp}.csv"
            if self.df is not None:
                self.df.to_csv(archivo, encoding='utf-8', index=False)
        
        print(f"✓ Datos exportados a {archivo}")
        return archivo
    
    def generar_reporte_reposicionamiento(self) -> str:
        """Genera reporte detallado de oportunidades de reposicionamiento."""
        reporte = []
        reporte.append("="*80)
        reporte.append("REPORTE DE OPORTUNIDADES DE REPOSICIONAMIENTO DE FÁRMACOS")
        reporte.append(f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        reporte.append("="*80)
        
        stats = self.estadisticas_completas()
        reporte.append(f"\n📊 ESTADÍSTICAS GENERALES:")
        reporte.append(f"  Total de fármacos: {stats['total_farmacos']}")
        reporte.append(f"  Con potencial reposicionamiento: {stats['farmacos_reposicionamiento']} ({stats['porcentaje_reposicionamiento']})")
        
        reporte.append(f"\n💊 FÁRMACOS CON POTENCIAL DE REPOSICIONAMIENTO:")
        for farmaco in self.farmacos_con_potencial_reposicionamiento():
            reporte.append(f"\n  • {farmaco['nombre_comercial']} ({farmaco['nombre_generico']})")
            reporte.append(f"    Indicación actual: {farmaco['indicacion_principal']}")
            reporte.append(f"    Potencial: {farmaco['potencial_reposicionamiento']}")
            reporte.append(f"    Mecanismo: {farmaco['mecanismo_accion']}")
        
        reporte_txt = "\n".join(reporte)
        archivo = f"reporte_reposicionamiento_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(reporte_txt)
        
        print(f"✓ Reporte generado: {archivo}")
        return reporte_txt
    
    def mostrar_farmaco_detallado(self, nombre: str) -> None:
        """Muestra información detallada de un fármaco."""
        farmacos = self.buscar_por_nombre(nombre)
        if not farmacos:
            print("Fármaco no encontrado")
            return
        
        f = farmacos[0]
        print("\n" + "="*80)
        print(f"💊 {f['nombre_comercial']} ({f['nombre_generico']})")
        print("="*80)
        print(f"Laboratorio: {f['laboratorio']}")
        print(f"Aprobación: {f['fecha_aprobacion']} | {f['pais_aprobacion']}")
        print(f"\n📋 INDICACIONES:")
        print(f"  Principal: {f['indicacion_principal']}")
        print(f"  Secundarias: {f['indicaciones_secundarias']}")
        print(f"\n🔬 FARMACOCINÉTICA:")
        print(f"  {f['farmacocinética']}")
        print(f"\n⚙️ MECANISMO:")
        print(f"  {f['mecanismo_accion']}")
        print(f"\n📊 CLASIFICACIÓN:")
        print(f"  Clase Terapéutica: {f['clase_terapeutica']}")
        print(f"  Código ATC: {f['codigo_atc']}")
        print(f"\n⚠️ SEGURIDAD:")
        print(f"  Efectos Adversos: {f['efectos_adversos']}")
        print(f"  Contraindicaciones: {f['contraindicaciones']}")
        print(f"\n💊 INTERACCIONES:")
        print(f"  {f['interacciones_importantes']}")
        print(f"\n🔄 REPOSICIONAMIENTO:")
        print(f"  {f['potencial_reposicionamiento']}")
        print("="*80 + "\n")


def menu_principal():
    """Menú principal interactivo."""
    gestor = GestorFarmacosAvanzado()
    
    while True:
        print("\n" + "="*60)
        print("🏥 GESTOR AVANZADO DE FÁRMACOS - REPOSICIONAMIENTO")
        print("="*60)
        print("BÚSQUEDA:")
        print("  1. Buscar por nombre")
        print("  2. Buscar por indicación")
        print("  3. Buscar por clase terapéutica")
        print("\nANÁLISIS DE REPOSICIONAMIENTO:")
        print("  4. Ver fármacos con potencial de reposicionamiento")
        print("  5. Analizar mecanismo de acción")
        print("  6. Interacciones metabólicas (CYP450)")
        print("  7. Indicaciones secundarias (uso compasivo)")
        print("\nANÁLISIS CLÍNICO:")
        print("  8. Perfil de seguridad de fármaco")
        print("  9. Fármacos para poblaciones especiales")
        print("  10. Estadísticas completas")
        print("\nREPORTES:")
        print("  11. Generar reporte de reposicionamiento")
        print("  12. Exportar datos (JSON/CSV)")
        print("  13. Ver información detallada de fármaco")
        print("\n  14. Salir")
        print("="*60)
        
        opcion = input("Seleccione opción (1-14): ").strip()
        
        if opcion == '1':
            nombre = input("Nombre del fármaco: ").strip()
            resultados = gestor.buscar_por_nombre(nombre)
            if resultados:
                for f in resultados[:5]:
                    print(f"✓ {f['nombre_comercial']} - {f['indicacion_principal']}")
            else:
                print("No encontrado")
        
        elif opcion == '2':
            indicacion = input("Indicación: ").strip()
            resultados = gestor.buscar_por_indicacion(indicacion)
            print(f"✓ Encontrados {len(resultados)} fármacos")
            for f in resultados[:10]:
                print(f"  • {f['nombre_comercial']}")
        
        elif opcion == '3':
            clase = input("Clase terapéutica: ").strip()
            resultados = gestor.buscar_por_clase_terapeutica(clase)
            print(f"✓ Encontrados {len(resultados)} fármacos de esta clase")
            for f in resultados[:10]:
                print(f"  • {f['nombre_comercial']}")
        
        elif opcion == '4':
            reposicionamiento = gestor.farmacos_con_potencial_reposicionamiento()
            print(f"\n💚 FÁRMACOS CON POTENCIAL DE REPOSICIONAMIENTO ({len(reposicionamiento)}):")
            for f in reposicionamiento:
                print(f"  • {f['nombre_comercial']}: {f['potencial_reposicionamiento']}")
        
        elif opcion == '5':
            mecanismo = input("Mecanismo de acción: ").strip()
            resultados = gestor.analizar_mecanismo_de_accion(mecanismo)
            print(f"✓ {len(resultados)} fármacos con este mecanismo")
            for f in resultados[:10]:
                print(f"  • {f['nombre_comercial']}")
        
        elif opcion == '6':
            metabolicos = gestor.farmacos_por_vias_metabolicas_comunes()
            print("\n🧬 AGRUPACIÓN POR VÍA METABÓLICA (CYP450):")
            for cyp, farmacos in sorted(metabolicos.items()):
                print(f"  {cyp}: {len(farmacos)} fármacos")
                for f in farmacos[:3]:
                    print(f"    - {f['nombre_comercial']}")
        
        elif opcion == '7':
            usos = gestor.indicaciones_no_aprobadas_por_uso_compasivo()
            print("\n🔄 POTENCIAL USO COMPASIVO:")
            for indicacion, farmacos_list in usos.items():
                print(f"  {indicacion.upper()}: {len(farmacos_list)} fármacos")
                for farmaco in farmacos_list[:5]:
                    print(f"    - {farmaco}")
        
        elif opcion == '8':
            nombre = input("Nombre del fármaco: ").strip()
            perfil = gestor.perfil_seguridad(nombre)
            if perfil:
                print(f"\n⚠️ PERFIL DE SEGURIDAD: {perfil['nombre']}")
                print(f"  Riesgo General: {perfil['riesgo_general']}")
                print(f"  Vía Admin: {perfil['via_administracion']}")
                print(f"  Efectos adversos principales: {', '.join(perfil['efectos_adversos_principales'])}")
        
        elif opcion == '9':
            poblacion = input("Población (embarazo/renal/hepatica): ").strip()
            farmacos_seguros = gestor.farmacos_para_poblaciones_especiales(poblacion)
            print(f"✓ {len(farmacos_seguros)} fármacos recomendados para {poblacion}")
        
        elif opcion == '10':
            stats = gestor.estadisticas_completas()
            print(f"\n📊 ESTADÍSTICAS COMPLETAS:")
            for clave, valor in stats.items():
                print(f"  {clave}: {valor}")
        
        elif opcion == '11':
            reporte = gestor.generar_reporte_reposicionamiento()
            print(reporte)
        
        elif opcion == '12':
            formato = input("Formato (json/csv): ").strip()
            gestor.exportar_para_analisis(formato)
        
        elif opcion == '13':
            nombre = input("Nombre del fármaco: ").strip()
            gestor.mostrar_farmaco_detallado(nombre)
        
        elif opcion == '14':
            print("\n¡Hasta luego!")
            break
        
        else:
            print("Opción no válida")


if __name__ == '__main__':
    menu_principal()
