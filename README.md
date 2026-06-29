# SysAdmin-RateLimiter
# Misión 1: Sistema de Rate Limiting (Escudo Perimetral)

## Descripción del Proyecto
Implementación de un sistema de limitación de tasa (Rate Limiter) diseñado para proteger la infraestructura contra ataques de fuerza bruta o saturación de peticiones (DDoS de bajo nivel).

## Decisión de Arquitectura
Para garantizar un rendimiento óptimo bajo alta carga, se ha seleccionado una estructura de datos tipo **HashMap** (diccionario). 
- **Complejidad:** O(1) en tiempo de acceso.
- **Ventaja:** Minimiza la latencia de respuesta, crucial para sistemas de red en tiempo real.
- **Desacoplamiento:** La lógica de validación está separada de la capa de almacenamiento, permitiendo una migración futura a bases de datos en memoria (Redis/Memcached) sin modificar la lógica central.

## Funcionalidad
El script valida peticiones basándose en:
1. Identificador único (IP o User ID).
2. Ventana de tiempo (Time-window).
3. Conteo de peticiones permitidas por ventana.

## Cómo ejecutar
1. Asegúrate de tener Python instalado.
2. Ejecuta: `python rate_limiter.py`

---
*Desarrollado para el Laboratorio de Arquitectura de Sistemas de Brato58t.*