# 📚 Enunciado: The Decoupled Library (Gestión de Préstamos)

Este es tu primer proyecto de aprendizaje de la Fase 1. El objetivo principal no es solo que el código "funcione", sino que la lógica de negocio esté totalmente aislada de la tecnología externa (bases de datos y frameworks web).

## 🎯 Objetivo Técnico

Construir una API de gestión de biblioteca utilizando **Clean Architecture**. Debes demostrar que puedes cambiar el mecanismo de persistencia (de una lista en memoria a una base de datos real) sin modificar las reglas de préstamo.

## 📋 Requisitos Funcionales

#### 1. Gestión de Libros

- Cada libro debe tener un identificador único (ISBN), un título, un autor y la cantidad de ejemplares disponibles en stock.

- Debe permitir el registro de nuevos ejemplares.

#### 2. Gestión de Socios

- Cada socio se identifica por un ID único, nombre y correo electrónico.

#### 3. Lógica de Préstamos (Reglas de Negocio)

Esta es la parte más importante del proyecto. Debes implementar un servicio que valide lo siguiente antes de confirmar un préstamo:

- **Regla de Stock:** No se puede prestar un libro si no quedan unidades disponibles en el inventario.

- **Regla de Límite:** Un socio no puede tener más de 3 libros prestados al mismo tiempo. Si ya tiene 3, el sistema debe rechazar la operación.

#### 4. Devoluciones

- Al devolver un libro, el stock debe aumentar y el préstamo debe marcarse como finalizado.

## 🏗️ Estructura del Proyecto

Debes organizar tu código en las siguientes capas, siguiendo la "Regla de la Dependencia":

1.  **Capa de Dominio (Domain):**
    - Contiene las **Entidades** (clases puras de Python como Libro y Socio).

    - No debe importar nada de FastAPI, SQLAlchemy o cualquier otra librería externa.

2.  **Capa de Aplicación (Application):**
    - Contiene los **Casos de Uso** (ej: la lógica de RealizarPrestamo).

    - Aquí es donde se verifican las reglas de negocio mencionadas arriba.

3.  **Capa de Infraestructura (Infrastructure):**
    - Aquí implementarás el **Repositorio**. Inicialmente, crea uno que guarde los datos en una lista de Python (en memoria).

    - Más adelante, aquí es donde configurarás SQLAlchemy para conectar con PostgreSQL.

4.  **Capa de Entrada (Entrypoints):**
    - Configuración de FastAPI y las rutas (endpoints) para interactuar con el sistema.

## 🛠️ Pasos Sugeridos

1.  Define tus entidades en la capa de dominio usando clases de datos.

2.  Escribe la lógica del caso de uso de préstamo, definiendo cómo recibirá la información de los libros y socios.

3.  Crea una interfaz (o contrato) para el repositorio de datos.

4.  Implementa la API con FastAPI para exponer estas funcionalidades.

## 🚨 Restricciones

- **Prohibido** usar lógica de base de datos dentro de las rutas de FastAPI.

- **Prohibido** que la capa de dominio importe librerías de infraestructura.

- **Utiliza Type Hinting** en todos los parámetros y retornos de funciones para asegurar la claridad del código.
