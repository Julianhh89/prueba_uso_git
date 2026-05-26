# 💊 Base de Datos de Fármacos Aprobados

Este proyecto contiene una base de datos completa de fármacos aprobados con un gestor interactivo para consultar, buscar y administrar medicamentos.

## 📋 Estructura del Proyecto

```
├── datos_farmacos.csv        # Base de datos de fármacos
├── gestor_farmacos.py        # Script de gestión
└── README.md                 # Documentación
```

## 📊 Base de Datos

La base de datos incluye los siguientes campos:

| Campo | Descripción |
|-------|-------------|
| **id** | Identificador único del fármaco |
| **nombre_comercial** | Nombre bajo el cual se comercializa |
| **nombre_generico** | Principio activo del medicamento |
| **laboratorio** | Fabricante del fármaco |
| **fecha_aprobacion** | Fecha de aprobación regulatoria |
| **indicacion** | Uso terapéutico principal |
| **presentacion** | Forma farmacéutica y dosis |
| **dosis_recomendada** | Dosis y pauta de administración |
| **efectos_adversos** | Posibles reacciones adversas |
| **contraindicaciones** | Casos en los que NO debe usarse |

## 🔍 Fármacos Incluidos

1. **Aspirina** - Ácido Acetilsalicílico (Bayer)
   - Indicación: Analgesia y anticoagulación
   - Dosis: 100-500mg cada 4-6 horas

2. **Ibupirac** - Ibuprofeno (Grupo Farmacéutico)
   - Indicación: Antiinflamatorio y analgésico
   - Dosis: 200-400mg cada 6-8 horas

3. **Amoxicilina** - Amoxicilina (Pfizer)
   - Indicación: Infección bacteriana
   - Dosis: 500mg-1g cada 8 horas

4. **Omeprazol** - Omeprazol (Astra Zeneca)
   - Indicación: Reflujo gastroesofágico
   - Dosis: 20-40mg diarios

5. **Metformina** - Metformina (Merck)
   - Indicación: Diabetes tipo 2
   - Dosis: 1500-2000mg diarios

6. **Lisinopril** - Lisinopril (Astra Zeneca)
   - Indicación: Hipertensión arterial
   - Dosis: 10-40mg diarios

7. **Atorvastatina** - Atorvastatina (Pfizer)
   - Indicación: Hipercolesterolemia
   - Dosis: 10-80mg diarios

8. **Loratadina** - Loratadina (Schering)
   - Indicación: Alergia
   - Dosis: 10mg diarios

9. **Paracetamol** - Acetaminofén (GSK)
   - Indicación: Fiebre y dolor
   - Dosis: 500-1000mg cada 6 horas

10. **Fluconazol** - Fluconazol (Pfizer)
    - Indicación: Infección fúngica
    - Dosis: 150mg dosis única

## 🚀 Cómo Usar

### Instalación

```bash
# No requiere dependencias externas, solo Python 3.x
python --version  # Verificar Python 3.x
```

### Ejecutar el Gestor

```bash
python gestor_farmacos.py
```

### Ejemplos de Uso

#### 1. Buscar un fármaco por nombre
```
Opción: 1
Ingrese el nombre: Aspirina
```

#### 2. Buscar por indicación terapéutica
```
Opción: 2
Ingrese la indicación: Hipertensión
```

#### 3. Buscar por laboratorio
```
Opción: 3
Ingrese el laboratorio: Pfizer
```

#### 4. Ver todos los fármacos
```
Opción: 4
```

#### 5. Ver estadísticas
```
Opción: 5
```

#### 6. Exportar a JSON
```
Opción: 6
# Genera: farmacos.json
```

#### 7. Agregar un nuevo fármaco
```
Opción: 7
Nombre comercial: [ingrese nombre]
Nombre genérico: [ingrese principio activo]
...
```

## 💻 Uso Programático

```python
from gestor_farmacos import GestorFarmacos

# Crear instancia del gestor
gestor = GestorFarmacos('datos_farmacos.csv')

# Buscar un fármaco
resultados = gestor.buscar_por_nombre('Aspirina')
for farmaco in resultados:
    print(farmaco['nombre_comercial'])

# Buscar por indicación
antibioticos = gestor.buscar_por_indicacion('Infección')

# Buscar por laboratorio
farmacos_pfizer = gestor.buscar_por_laboratorio('Pfizer')

# Obtener por ID
farmaco = gestor.obtener_por_id('1')

# Obtener todos
todos = gestor.listar_todos()

# Exportar a JSON
gestor.exportar_a_json()

# Ver estadísticas
stats = gestor.estadisticas()
print(f"Total de fármacos: {stats['total_farmacos']}")

# Agregar nuevo fármaco
nuevo = {
    'nombre_comercial': 'Nuevo Fármaco',
    'nombre_generico': 'Principio Activo',
    'laboratorio': 'Lab X',
    'indicacion': 'Tratamiento Y',
    'presentacion': 'Tableta 100mg',
    'dosis_recomendada': '100mg diarios',
    'efectos_adversos': 'Leve molestia',
    'contraindicaciones': 'Embarazo'
}
gestor.agregar_farmaco(nuevo)
```

## 📝 Funcionalidades Principales

- ✅ Búsqueda por nombre comercial o genérico
- ✅ Búsqueda por indicación terapéutica
- ✅ Búsqueda por laboratorio fabricante
- ✅ Listado completo de fármacos
- ✅ Estadísticas de la base de datos
- ✅ Exportación a formato JSON
- ✅ Agregar nuevos fármacos
- ✅ Persistencia de datos en CSV
- ✅ Interfaz interactiva de menú
- ✅ Uso programático desde otros scripts

## 🛠️ Requisitos

- Python 3.6+
- Sistema operativo: Windows, macOS, Linux
- Librerías estándar (csv, json, datetime)

## 📄 Licencia

Este proyecto es de código abierto y puede ser utilizado libremente.

## 👨‍💻 Autor

Creado por: Julianhh89

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el repositorio
2. Crea una rama con tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

---

**Última actualización:** 2026-05-26
