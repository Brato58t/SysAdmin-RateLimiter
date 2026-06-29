import time

# Nuestro "HashMap" en memoria
# Estructura: { 'user_ip': {'count': int, 'last_reset': float} }
rate_limiter = {}

def permitir_peticion(user_id):
    current_time = time.time()
    WINDOW_SIZE = 60  # Ventana de 60 segundos
    MAX_REQUESTS = 5  # Límite de peticiones

    # 1. Si el usuario no está, inicializamos su registro (O(1))
    if user_id not in rate_limiter:
        rate_limiter[user_id] = {'count': 1, 'last_reset': current_time}
        return True

    # 2. Obtenemos los datos del usuario (O(1))
    user_data = rate_limiter[user_id]

    # 3. Lógica de validación: ¿Ha pasado la ventana de tiempo?
    if current_time - user_data['last_reset'] > WINDOW_SIZE:
        # Resetear contador para nueva ventana
        user_data['count'] = 1
        user_data['last_reset'] = current_time
        return True
    
    # 4. ¿Estamos dentro del límite permitido?
    if user_data['count'] < MAX_REQUESTS:
        user_data['count'] += 1
        return True
    
    # Denegar petición (Rate Limited)
    return False

# Prueba rápida
ip_cliente = "192.168.1.1"
for i in range(7):
    print(f"Petición {i+1}: {'Aprobada' if permitir_peticion(ip_cliente) else 'Denegada'}")