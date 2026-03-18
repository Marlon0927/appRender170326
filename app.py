from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Lista para almacenar las tareas en memoria
tasks = []
task_id_counter = 1

# ==================== GET ====================
@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    """Obtiene todas las tareas"""
    return jsonify({
        'success': True,
        'data': tasks,
        'total': len(tasks)
    }), 200


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Obtiene una tarea específica por ID"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if task is None:
        return jsonify({
            'success': False,
            'message': f'Tarea con ID {task_id} no encontrada'
        }), 404
    
    return jsonify({
        'success': True,
        'data': task
    }), 200


# ==================== POST ====================
@app.route('/tasks', methods=['POST'])
def create_task():
    """Crea una nueva tarea"""
    global task_id_counter
    
    data = request.get_json()
    
    # Validación de datos
    if not data or 'title' not in data:
        return jsonify({
            'success': False,
            'message': 'El campo "title" es requerido'
        }), 400
    
    # Crear la nueva tarea
    new_task = {
        'id': task_id_counter,
        'title': data['title'],
        'description': data.get('description', ''),
        'completed': data.get('completed', False),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    
    tasks.append(new_task)
    task_id_counter += 1
    
    return jsonify({
        'success': True,
        'message': 'Tarea creada exitosamente',
        'data': new_task
    }), 201


# ==================== PUT ====================
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Actualiza una tarea existente"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if task is None:
        return jsonify({
            'success': False,
            'message': f'Tarea con ID {task_id} no encontrada'
        }), 404
    
    data = request.get_json()
    
    # Actualizar solo los campos proporcionados
    if 'title' in data:
        task['title'] = data['title']
    if 'description' in data:
        task['description'] = data['description']
    if 'completed' in data:
        task['completed'] = data['completed']
    
    task['updated_at'] = datetime.now().isoformat()
    
    return jsonify({
        'success': True,
        'message': 'Tarea actualizada exitosamente',
        'data': task
    }), 200


# ==================== DELETE ====================
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Elimina una tarea"""
    global tasks
    
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if task is None:
        return jsonify({
            'success': False,
            'message': f'Tarea con ID {task_id} no encontrada'
        }), 404
    
    tasks = [t for t in tasks if t['id'] != task_id]
    
    return jsonify({
        'success': True,
        'message': 'Tarea eliminada exitosamente',
        'data': task
    }), 200


# ==================== RUTAS ADICIONALES ====================
@app.route('/', methods=['GET'])
def home():
    """Ruta de bienvenida"""
    return jsonify({
        'message': 'Bienvenido a la API de Gestión de Tareas',
        'endpoints': {
            'GET /tasks': 'Obtiene todas las tareas',
            'GET /tasks/<id>': 'Obtiene una tarea específica',
            'POST /tasks': 'Crea una nueva tarea',
            'PUT /tasks/<id>': 'Actualiza una tarea',
            'DELETE /tasks/<id>': 'Elimina una tarea'
        }
    }), 200


# ==================== MANEJO DE ERRORES ====================
@app.errorhandler(404)
def not_found(error):
    """Manejador para rutas no encontradas"""
    return jsonify({
        'success': False,
        'message': 'Ruta no encontrada'
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Manejador para métodos no permitidos"""
    return jsonify({
        'success': False,
        'message': 'Método no permitido'
    }), 405


@app.errorhandler(500)
def internal_error(error):
    """Manejador para errores internos"""
    return jsonify({
        'success': False,
        'message': 'Error interno del servidor'
    }), 500


if __name__ == '__main__':
    # Ejecutar la aplicación en modo desarrollo
    app.run(debug=True, host='0.0.0.0', port=5000)
