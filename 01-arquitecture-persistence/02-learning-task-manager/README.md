# 📚 Proyecto 03: Universal Task Manager (Persistencia Flexible)

Este es el tercer reto técnico de la Fase 1: Arquitectura y Persistencia. En este proyecto, el foco principal es el Principio de Inversión de Dependencias (DIP) y el dominio del Patrón Repositorio para soportar múltiples fuentes de datos.

## 🎯 Objetivo Técnico

Construir una API de gestión de tareas que sea agnóstica al motor de almacenamiento. Debes ser capaz de intercambiar el backend de persistencia (Memoria, Archivo JSON o Base de Datos SQL) sin que la lógica de negocio ni los controladores de FastAPI sufran ninguna modificación.

## 📋 Requisitos Funcionales

**1. Gestión de Tareas (CRUD)**

- **Atributos:** Cada tarea debe tener un ID único, título, descripción, fecha de creación y estado (Pendiente o Completada).

**2. Lógica de Negocio (Reglas de Dominio)**

El sistema debe validar lo siguiente antes de procesar las acciones:

1.  **Límite de Carga:** Un usuario no puede tener más de **10 tareas en estado Pendiente** simultáneamente (evitar el burnout).

2.  **Unicidad de Título:** No se pueden crear dos tareas con el mismo título exacto para evitar duplicidades accidentales.

**3. Persistencia Intercambiable**

El sistema debe funcionar correctamente utilizando cualquiera de estos tres "adaptadores":

- **InMemoryRepository:** Los datos se pierden al reiniciar el servidor (ideal para tests rápidos).

- **JsonFileRepository:** Los datos se guardan en un archivo tasks.json.

- **SQLAlchemyRepository:** Los datos se guardan en una base de datos PostgreSQL.

## 🏗️ Estructura del Proyecto

Siguiendo **la Arquitectura Limpia**, el código se organizará en src/:

- **Capa de Dominio (Domain):**
    - Entidad Tarea.

    - **Contrato del Repositorio:** Una clase abstracta (o Protocol en Python) que defina qué métodos deben tener los repositorios (ej: add, get_all, update).

- **Capa de Aplicación (Application):**
    - **Casos de Uso:** CrearTarea, CompletarTarea, ListarTareas.

    - Esta capa solo "conoce" la interfaz abstracta del repositorio, no las implementaciones reales.

- **Capa de Infraestructura (Infrastructure):**
    - Las tres implementaciones concretas del repositorio (Memory, JSON, SQL).

- **Capa de Entrada (Entrypoints):**
    - Endpoints de FastAPI. Aquí se realizará la "Inyección de Dependencia" para decidir qué repositorio usar.

## 🛠️ Pasos Sugeridos

1.  **Definir el Contrato:** Antes de programar cómo guardar los datos, define la interfaz TaskRepository en el dominio.

2.  **Implementación Incremental:**
    - Empieza por el repositorio en memoria.

    - Luego crea el de JSON (usando la librería json de Python).

    - Finalmente, implementa SQLAlchemy.

3.  **Inyección de Dependencias:** Configura tu aplicación para que el repositorio se pase como argumento a los Casos de Uso.

4.  **Validación:** Prueba que al cambiar de repositorio en el punto de entrada, la API sigue respondiendo exactamente igual.

## 🚨 Restricciones Profesionales

- **Prohibido el acoplamiento:** Los Casos de Uso no pueden importar SQLAlchemy ni la librería json. Solo deben interactuar con la abstracción del dominio.

- **Manejo de Excepciones:** Si el archivo JSON no existe o la DB está caída, la infraestructura debe capturar el error y lanzar una excepción que la aplicación entienda.

- **Clean Code:** Aplica el principio de Responsabilidad Única. El código encargado de escribir en el disco no debe estar mezclado con la lógica de "Límite de Carga".

**Nota:** Dominar la persistencia flexible es fundamental para el ML Service de tu proyecto Senior, donde cambiaremos frecuentemente entre datos de entrenamiento (archivos) y datos de producción (DB).
