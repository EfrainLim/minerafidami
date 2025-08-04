# Configuración de Gunicorn para Minera Fidami
# Puerto: 8005

# Puerto del servidor
bind = "0.0.0.0:8005"

# Número de workers (procesos)
workers = 3

# Timeout
timeout = 30

# Logs
accesslog = "gunicorn_access.log"
errorlog = "gunicorn_error.log"
loglevel = "info"

# Configuración de seguridad
limit_request_line = 4094
limit_request_fields = 100