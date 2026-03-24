# 📚 Proyecto 03: Inventory System (Control de Stock y Eventos)

Este es el tercer reto técnico de la **Fase 1: Arquitectura y Persistencia**. En este proyecto introducimos un concepto avanzado de Clean Architecture: los **Eventos de Dominio**. El objetivo es gestionar un inventario donde el sistema reaccione automáticamente ante situaciones críticas.

## 🎯 Objetivo Técnico

Construir un sistema de inventario capaz de detectar y notificar cambios de estado importantes. Aprenderás a desacoplar la lógica de "modificar stock" de la lógica de "enviar una alerta", permitiendo que el sistema sea extensible sin ensuciar las entidades básicas.

## 📋 Requisitos Funcionales

**1. Catálogo de Productos**

- **Atributos**: Cada producto debe tener un ID único, nombre, SKU (código de referencia), stock actual y un umbral de stock bajo (mínimo deseado).

**2. Lógica de Movimientos (Reglas de Dominio)**

1.  **Entrada/Salida de Stock**: El sistema debe permitir sumar o restar existencias.

2.  **Validación de Existencias**: No se puede retirar más stock del que hay disponible (el stock nunca puede ser negativo).

3.  **Detección de Stock Bajo:** Si tras una operación el stock cae por debajo del "umbral", el sistema debe generar una alerta.

**3. Sistema de Notificaciones (Efectos Secundarios)**

El sistema debe ser capaz de "escuchar" cuando un producto tiene stock bajo y ejecutar una acción (por ahora, un simple print o log profesional que simule un aviso al gerente).

## 🏗️ Estructura del Proyecto

Siguiendo la **Arquitectura Limpia**, el código se organizará en src/:

- **Capa de Dominio (Domain):**
    - **Entidad Producto:** Contiene la lógica para aumentar/disminuir stock y detectar si se ha cruzado el umbral.

    - **Eventos de Dominio:** Definición de la clase StockBajoEvent.

- **Capa de Aplicación (Application):**
    - **Casos de Uso:** RegistrarMovimientoStock, ConsultarProducto.

    - **Manejadores de Eventos (Handlers):** Lógica que decide qué hacer cuando se dispara un evento de stock bajo.

- Capa de Infraestructura (Infrastructure):
    - Repositorio para persistir los productos.

- **Capa de Entrada (Entrypoints):**
    - API con **FastAPI** para realizar las operaciones de almacén.

## 🛠️ Pasos Sugeridos

1.  **Modelar el Evento:** Crea una clase sencilla que represente que "algo ha pasado" (ej: ProductoID, StockActual, Timestamp).

2.  **Lógica en la Entidad:** La entidad Producto debe tener un método que, al restar stock, verifique el umbral y "registre" el evento si es necesario.

3.  **El Bus de Eventos (Básico):** Implementa una forma sencilla de que el Caso de Uso, tras guardar en el repositorio, revise si hay eventos pendientes y los "dispare" a sus manejadores.

4.  **Desacoplamiento:** Asegúrate de que la función que imprime la alerta de "¡Stock Bajo!" esté en un archivo separado de la lógica que resta el número de existencias.

## 🚨 Restricciones Profesionales

- **No Acoplamiento:** La lógica de "restar stock" no debe saber cómo se envía la notificación (ni por email, ni por consola, ni por Telegram). Solo debe emitir el evento.

- **Integridad:** El evento solo debe dispararse si la transacción en la base de datos se completa con éxito.

- **Clean Code:** Las entidades deben ser "ricas", es decir, ellas mismas deben saber si su stock es bajo, no dejar esa lógica desperdigada en los servicios.

**Nota:** _Este patrón de eventos es el que usaremos en el módulo de Habit Intelligence de tu proyecto Senior para detectar patrones de procrastinación en tiempo real._
