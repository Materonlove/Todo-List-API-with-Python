from flask import Flask, jsonify, request 
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/todos', methods=['GET'])
def todo_get(): 
    json_text = jsonify(todos)
    return json_text

    

    some_data = { "name": "Bobby", "lastname": "Rixer" }

@app.route('/blahblah', methods=['GET'])
def blahblah():


    # puedes convertir esa variable en un string json así
    json_text = jsonify(todos)

    # y luego puedes retornarla (return) en el response body así:
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)


    todos.append(request_body)
    json_text = jsonify(todos)
    
    return json_text


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    position = int(position)
    if position >= len(todos):
        return jsonify({"message":"indice invalido"})
    if position < 0:
        return jsonify({"message":"indice invalido"})
    if len(todos)==0:
        return jsonify({"message":"indice invalido"})


    todos.pop(position)

    json_text = jsonify(todos)
    return json_text 








# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)