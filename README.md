# Base de Datos de Fármacos Aprobados

## 📋 Descripción

Este proyecto contiene una base de datos de fármacos aprobados con información relevante incluyendo:
- Nombres comerciales y genéricos
- Laboratorios fabricantes
- Indicaciones terapéuticas
- Presentaciones y dosis recomendadas
- Efectos adversos y contraindicaciones

## 📁 Estructura del Proyecto

```
├── datos_farmacos.csv       # Base de datos en formato CSV
├── gestor_farmacos.py       # Script Python para gestionar la BD
├── README.md                # Este archivo
└── farmacos.json            # Exportación de la BD en JSON (generado)
```

## 🗄️ Contenido de la Base de Datos

La base de datos incluye los siguientes campos:

| Campo | Descripción |
|-------|-------------|
| id | Identificador único del fármaco |
| nombre_comercial | Nombre con el que se vende el medicamento |
| nombre_generico | Nombre químico/genérico del principio activo |
| laboratorio | Fabricante del fármaco |
| fecha_aprobacion | Fecha de aprobación regulatoria |
| indicacion | Uso terapéutico del medicamento |
| presentacion | Forma farmacéutica y concentración |
| dosis_recomendada | Dosis estándar de administración |
| efectos_adversos | Posibles efectos secundarios |
| contraindicaciones | Situaciones donde NO debe usarse |

## 🐍 Uso del Script Python

### Instalación

No requiere dependencias externas, solo Python 3.6+

```bash
python gestor_farmacos.py
```

### Funcionalidades Principales

#### 1. Buscar por Nombre
```python
from gestor_farmacos import GestorFarmacos

gestor = GestorFarmacos("datos_farmacos.csv")
resultados = gestor.buscar_por_nombre("Aspirina")
```

#### 2. Buscar por Indicación
```python
resultados = gestor.buscar_por_indicacion("Hipertension")
```

#### 3. Buscar por Laboratorio
```python
resultados = gestor.buscar_por_laboratorio("Pfizer")
```

#### 4. Obtener Fármaco por ID
```python
farmaco = gestor.obtener_farmaco_por_id("1")
```

#### 5. Listar Todos los Fármacos
```python
gestor.listar_todos()
```

#### 6. Exportar a JSON
```python
gestor.exportar_json("farmacos.json")
```

#### 7. Obtener Estadísticas
```python
stats = gestor.obtener_estadisticas()
print(stats['total_farmacos'])
```

## 📊 Fármacos Incluidos

La base de datos inicial contiene 10 fármacos aprobados:

1. **Aspirina** - Analgesia y anticoagulación
2. **Ibupirac** - Antiinflamatorio
3. **Amoxicilina** - Antibiótico
4. **Omeprazol** - Reflujo gástrico
5. **Metformina** - Diabetes tipo 2
6. **Lisinopril** - Hipertensión
7. **Atorvastatina** - Hipercolesterolemia
8. **Loratadina** - Alergia
9. **Paracetamol** - Fiebre y dolor
10. **Fluconazol** - Infección fúngica

## 🔧 Cómo Agregar Nuevos Fármacos

### Opción 1: Directamente en el CSV
1. Abre `datos_farmacos.csv`
2. Agrega una nueva fila con los datos del fármaco
3. Guarda el archivo

### Opción 2: Usando el script Python
```python
nuevo_farmaco = {
    'id': '11',
    'nombre_comercial': 'Nombre Comercial',
    'nombre_generico': 'Nombre Genérico',
    'laboratorio': 'Laboratorio',
    'fecha_aprobacion': '2025-01-01',
    'indicacion': 'Indicación',
    'presentacion': 'Presentación',
    'dosis_recomendada': 'Dosis',
    'efectos_adversos': 'Efectos',
    'contraindicaciones': 'Contraindicaciones'
}

gestor.agregar_farmaco(nuevo_farmaco)
```

## 📝 Ejemplo de Uso Completo

```python
from gestor_farmacos import GestorFarmacos

# Inicializar
gestor = GestorFarmacos("datos_farmacos.csv")

# Buscar fármacos para hipertensión
antihipertensivos = gestor.buscar_por_indicacion("Hipertension")
print(f"Encontrados {len(antihipertensivos)} antihipertensivos")

# Obtener estadísticas
stats = gestor.obtener_estadisticas()
print(f"Total: {stats['total_farmacos']} fármacos")
print(f"Laboratorios: {stats['laboratorios']}")

# Exportar a JSON
gestor.exportar_json()
```

## ⚠️ Importante

- Esta base de datos es solo para propósitos educativos y de demostración
- No debe usarse como referencia médica oficial
- Consulta siempre con profesionales de la salud autorizados
- Verifica la información actual en registros farmacéuticos oficiales

## 📄 Licencia

Este proyecto es de acceso público.

## 👤 Autor

Creado por Julianhh89

---

**Última actualización:** Mayo 2026
