# Ejemplos de uso con cURL

## Iniciar el servidor
```
python app.py
```

---

## 1. GET - Obtener todas las tareas
```bash
curl -X GET http://localhost:5000/tasks
```

---

## 2. GET - Obtener una tarea específica por ID
```bash
curl -X GET http://localhost:5000/tasks/1
```

---

## 3. POST - Crear una nueva tarea (completa)
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d "{
    \"title\": \"Comprar leche\",
    \"description\": \"Ir al supermercado\",
    \"completed\": false
  }"
```

---

## 4. POST - Crear una nueva tarea (mínima)
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"Mi tarea\"}"
```

---

## 5. PUT - Actualizar una tarea completa
```bash
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d "{
    \"title\": \"Comprar leche y pan\",
    \"description\": \"Ir al supermercado por la tarde\",
    \"completed\": true
  }"
```

---

## 6. PUT - Actualizar solo el título
```bash
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"Nuevo título\"}"
```

---

## 7. PUT - Marcar tarea como completada
```bash
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d "{\"completed\": true}"
```

---

## 8. DELETE - Eliminar una tarea
```bash
curl -X DELETE http://localhost:5000/tasks/1
```

---

## 9. Secuencia completa de ejemplo

```bash
# 1. Crear tarea 1
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"Tarea 1\", \"description\": \"Primera tarea\"}"

# 2. Crear tarea 2
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"Tarea 2\", \"description\": \"Segunda tarea\"}"

# 3. Obtener todas las tareas
curl -X GET http://localhost:5000/tasks

# 4. Obtener tarea con ID 1
curl -X GET http://localhost:5000/tasks/1

# 5. Actualizar tarea con ID 1
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"Tarea 1 actualizada\", \"completed\": true}"

# 6. Eliminar tarea con ID 2
curl -X DELETE http://localhost:5000/tasks/2

# 7. Verificar tareas finales
curl -X GET http://localhost:5000/tasks
```

---

## Usando PowerShell (Windows)

Si estás en Windows y prefieres PowerShell:

```powershell
# GET - Obtener todas las tareas
Invoke-RestMethod -Uri "http://localhost:5000/tasks" -Method Get

# POST - Crear una tarea
$body = @{
    title = "Mi tarea"
    description = "Descripción"
    completed = $false
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/tasks" `
  -Method Post `
  -Body $body `
  -ContentType "application/json"

# PUT - Actualizar una tarea
$body = @{
    title = "Tarea actualizada"
    completed = $true
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/tasks/1" `
  -Method Put `
  -Body $body `
  -ContentType "application/json"

# DELETE - Eliminar una tarea
Invoke-RestMethod -Uri "http://localhost:5000/tasks/1" -Method Delete
```

---

## Códigos de respuesta esperados

| Método | Ruta | Código | Descripción |
|--------|------|--------|-------------|
| GET | `/tasks` | 200 | Obtiene todas las tareas |
| GET | `/tasks/1` | 200 | Tarea encontrada |
| GET | `/tasks/999` | 404 | Tarea no encontrada |
| POST | `/tasks` | 201 | Tarea creada |
| POST | `/tasks` (sin title) | 400 | Datos inválidos |
| PUT | `/tasks/1` | 200 | Tarea actualizada |
| PUT | `/tasks/999` | 404 | Tarea no encontrada |
| DELETE | `/tasks/1` | 200 | Tarea eliminada |
| DELETE | `/tasks/999` | 404 | Tarea no encontrada |
