# 📚 Proyecto 01: The Decoupled Library

Este proyecto es el punto de partida de la Fase 1. Aquí implementaremos el núcleo de un sistema de gestión bibliotecaria aplicando **Arquitectura Limpia**. La prioridad es el desacoplamiento: la lógica de negocio debe ser agnóstica a la base de datos y al framework web.

## 🎯 Objetivos de Aprendizaje

- Aplicar la **Regla de la Dependencia.**

- Definir **Entidades de Dominio** puras (sin dependencias externas).

- Orquestar la lógica mediante **Casos de Uso.**

- Implementar el **Patrón Repositorio** (In-Memory y SQL).

## 📋 Enunciado y Reglas de Negocio

El sistema debe gestionar el préstamo de libros a socios cumpliendo estrictamente con las siguientes validaciones antes de confirmar cualquier operación:

1.  **Validación de Inventario:** No se puede realizar un préstamo si el libro tiene stock = 0.

2.  **Límite de Préstamos:** Un socio tiene un límite máximo de 3 libros activos. Si intenta pedir un cuarto, el sistema debe denegar la operación con un mensaje de error de negocio.

3.  **Ciclo de Devolución:** Al devolver un libro, el stock debe incrementarse automáticamente y el préstamo debe quedar cerrado.

## 🏗️ Requerimientos Técnicos

#### Estructura de Capas (src/)

- domain/: Clases Libro, Socio y Prestamo (Python puro, sin librerías).

- application/: Lógica de los casos de uso (ej. RealizarPrestamoService).

- infrastructure/: Adaptadores de persistencia (SQLAlchemy y Repositorio en memoria).

- entrypoints/: Rutas de FastAPI.

#### Estándares de Calidad

- **Type Hinting:** Obligatorio en todos los parámetros y retornos.

- **Clean Code:** Nombres descriptivos y funciones de responsabilidad única.

- **Excepciones:** Manejo de errores de dominio personalizados (ej: StockInsuficienteError).

## 🚀 Guía de Ejecución

1.  **Diseño de Dominio:** Crear entidades en src/domain/.

2.  **Casos de Uso:** Implementar la lógica en src/application/.

3.  **Persistencia:** Crear el repositorio en memoria en src/infrastructure/.

4.  **API:** Exponer los endpoints en src/entrypoints/.

**Estado:** 🏗️ En fase de diseño de dominio.
