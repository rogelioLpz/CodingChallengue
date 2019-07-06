from flask import Flask,jsonify,make_response
from puzzle_queens import puzzle_queens
#from models import SolucionReina
from database import init_db, db_session,SolucionReina

app = Flask(__name__)


@app.route('/api/v1/puzzle_queens/<int:n_queens>', methods=['GET'])
def get_solutions(n_queens):
    init_db()
    # Obtener algoritmo para n reinas
    datos= puzzle_queens(n_queens)
    #Eliminar datos previos de BD
    db_session.query(SolucionReina).filter(SolucionReina.NumReinas==n_queens).delete()
    #Insertar datos en la BD
    for r in datos:
        db_session.add(SolucionReina(n_queens,str(r)))  
    #Finalizar operacion en BD
    db_session.commit()
    #Respuesta del servicio 
    return jsonify({'n_solutions':len(datos),'solutions': datos})

#Otras rutas
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Servicio no encontrado'}), 404)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=True)
    print('Servicio iniciado correctamente')
