````markdown
# 💊 Base de Datos de Fármacos Aprobados

Base de datos completa con información sobre fármacos aprobados y un gestor Python para consultarla, buscarla y manipularla.

## 📋 Descripción

Este proyecto contiene:
- **datos_farmacos.csv**: Base de datos con 10 fármacos aprobados
- **gestor_farmacos.py**: Script Python con herramientas para gestionar la BD
- **README.md**: Esta documentación

## 📊 Estructura de la Base de Datos

Cada fármaco en la base de datos contiene la siguiente información:

| Campo | Descripción |
|-------|-------------|
| `id` | Identificador único del fármaco |
| `nombre_comercial` | Nombre comercial del medicamento |
| `nombre_generico` | Nombre genérico/principio activo |
| `laboratorio` | Laboratorio fabricante |
| `fecha_aprobacion` | Fecha de aprobación |
| `indicacion` | Indicación terapéutica principal |
| `presentacion` | Forma de presentación (tableta, cápsula, etc.) |
| `dosis_recomendada` | Dosis recomendada |
| `efectos_adversos` | Efectos secundarios comunes |
| `contraindicaciones` | Situaciones donde NO debe usarse |

## 🔧 Instalación

### Requisitos
- Python 3.7 o superior
- Módulos estándar de Python (csv, json, typing)

### Pasos

1. Clona o descarga el repositorio
2. Verifica que `datos_farmacos.csv` esté en el mismo directorio que `gestor_farmacos.py`

## 📖 Uso

### Ejecutar el script principal

```bash
python gestor_farmacos.py
```

Esto ejecutará demostraciones de todas las funcionalidades.

### Usar como módulo

```python
from gestor_farmacos import GestorFarmacos

# Inicializar el gestor
gestor = GestorFarmacos("datos_farmacos.csv")

# Buscar por nombre
resultados = gestor.buscar_por_nombre("Aspirin")

# Buscar por indicación
resultados = gestor.buscar_por_indicacion("Hipertension")

# Buscar por laboratorio
resultados = gestor.buscar_por_laboratorio("Pfizer")

# Obtener un fármaco por ID
farmaco = gestor.obtener_farmaco_por_id("1")

# Listar todos los fármacos
gestor.listar_todos()

# Exportar a JSON
gestor.exportar_json("farmacos.json")

# Obtener estadísticas
stats = gestor.obtener_estadisticas()
print(f"Total: {stats['total_farmacos']} fármacos")
```

## 💊 Fármacos en la Base de Datos

### 1. **Aspirina**
- **Nombre genérico**: Ácido Acetilsalicílico
- **Laboratorio**: Bayer
- **Indicación**: Analgesia y anticoagulación
- **Dosis**: 100-500mg cada 4-6 horas
- **Contraindicaciones**: Alergia al AAS

### 2. **Ibupirac**
- **Nombre genérico**: Ibuprofeno
- **Laboratorio**: Grupo Farmacéutico
- **Indicación**: Antiinflamatorio y analgésico
- **Dosis**: 200-400mg cada 6-8 horas
- **Contraindicaciones**: Úlcera péptica

### 3. **Amoxicilina**
- **Nombre genérico**: Amoxicilina
- **Laboratorio**: Pfizer
- **Indicación**: Infección bacteriana
- **Dosis**: 500mg-1g cada 8 horas
- **Contraindicaciones**: Reacción alérgica a penicilinas

### 4. **Omeprazol**
- **Nombre genérico**: Omeprazol
- **Laboratorio**: Astra Zeneca
- **Indicación**: Reflujo gastroesofágico
- **Dosis**: 20-40mg diarios
- **Contraindicaciones**: Hipersensibilidad

### 5. **Metformina**
- **Nombre genérico**: Metformina
- **Laboratorio**: Merck
- **Indicación**: Diabetes tipo 2
- **Dosis**: 1500-2000mg diarios
- **Contraindicaciones**: Insuficiencia renal

### 6. **Lisinopril**
- **Nombre genérico**: Lisinopril
- **Laboratorio**: Astra Zeneca
- **Indicación**: Hipertensión arterial
- **Dosis**: 10-40mg diarios
- **Contraindicaciones**: Embarazo

### 7. **Atorvastatina**
- **Nombre genérico**: Atorvastatina
- **Laboratorio**: Pfizer
- **Indicación**: Hipercolesterolemia
- **Dosis**: 10-80mg diarios
- **Contraindicaciones**: Enfermedad hepática activa

### 8. **Loratadina**
- **Nombre genérico**: Loratadina
- **Laboratorio**: Schering
- **Indicación**: Alergia
- **Dosis**: 10mg diarios
- **Contraindicaciones**: Hipersensibilidad

### 9. **Paracetamol**
- **Nombre genérico**: Acetaminofén
- **Laboratorio**: GSK
- **Indicación**: Fiebre y dolor
- **Dosis**: 500-1000mg cada 6 horas
- **Contraindicaciones**: Hipersensibilidad

### 10. **Fluconazol**
- **Nombre genérico**: Fluconazol
- **Laboratorio**: Pfizer
- **Indicación**: Infección fúngica
- **Dosis**: 150mg dosis única
- **Contraindicaciones**: Hipersensibilidad

## 🔍 Métodos Disponibles

### `GestorFarmacos` - Clase principal

#### `__init__(archivo_csv="datos_farmacos.csv")`
Inicializa el gestor y carga los datos del archivo CSV.

#### `cargar_datos()`
Carga los datos del archivo CSV.

#### `buscar_por_nombre(nombre: str) -> List[Dict]`
Busca fármacos por nombre comercial o genérico.

#### `buscar_por_indicacion(indicacion: str) -> List[Dict]`
Busca fármacos por indicación terapéutica.

#### `buscar_por_laboratorio(laboratorio: str) -> List[Dict]`
Busca fármacos por laboratorio fabricante.

#### `obtener_farmaco_por_id(farmaco_id: str) -> Dict`
Obtiene un fármaco específico por su ID.

#### `listar_todos() -> None`
Imprime todos los fármacos en la base de datos.

#### `exportar_json(archivo_salida: str = "farmacos.json") -> None`
Exporta la base de datos a formato JSON.

#### `agregar_farmaco(datos_farmaco: Dict) -> None`
Agrega un nuevo fármaco a la base de datos.

#### `obtener_estadisticas() -> Dict`
Obtiene estadísticas sobre la base de datos.

## 📝 Agregar Nuevos Fármacos

Para agregar un nuevo fármaco a la base de datos, agrega una nueva fila al archivo `datos_farmacos.csv` con la siguiente estructura:

```csv
11,Nombre Comercial,Nombre Genérico,Laboratorio,YYYY-MM-DD,Indicación,Presentación,Dosis,Efectos Adversos,Contraindicaciones
```

O mediante código Python:

```python
nuevo_farmaco = {
    'id': '11',
    'nombre_comercial': 'Nombre Comercial',
    'nombre_generico': 'Nombre Genérico',
    'laboratorio': 'Laboratorio',
    'fecha_aprobacion': '2023-01-01',
    'indicacion': 'Indicación',
    'presentacion': 'Presentación',
    'dosis_recomendada': 'Dosis',
    'efectos_adversos': 'Efectos',
    'contraindicaciones': 'Contraindicaciones'
}

gestor.agregar_farmaco(nuevo_farmaco)
```

## 📊 Estadísticas

Ejecuta el siguiente código para obtener estadísticas de la base de datos:

```python
stats = gestor.obtener_estadisticas()
print(f"Total de fármacos: {stats['total_farmacos']}")
print(f"Laboratorios únicos: {stats['laboratorios_unicos']}")
print(f"Indicaciones únicas: {stats['indicaciones_unicas']}")
print(f"Laboratorios: {stats['laboratorios']}")
print(f"Indicaciones: {stats['indicaciones']}")
```

## 📤 Exportación

### A JSON

```python
gestor.exportar_json("farmacos.json")
```

Esto crea un archivo `farmacos.json` con todos los datos en formato JSON.

## ⚠️ Advertencias Importantes

- Esta base de datos es solo con fines educativos/demostrativos
- Consulta siempre con profesionales médicos antes de usar cualquier medicamento
- La información debe ser verificada con fuentes oficiales
- No se responsabiliza por mal uso de la información

## 📄 Licencia

Este proyecto es de código abierto y se proporciona tal cual es.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el repositorio
2. Crea una rama con tus cambios
3. Haz un Pull Request

## 👨‍💻 Autor

Proyecto creado como demostración de gestión de bases de datos en Python.

---

**Última actualización**: 2026-05-26
````
