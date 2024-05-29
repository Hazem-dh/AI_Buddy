from flask import Flask, request, jsonify

app = Flask(__name__)



@app.get('/api/data')
def get_data():
    data = {
        'message': 'Mock data',
        'status': 'success'
    }
    return jsonify(data)

@app.post('/api/echo')
def echo():
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
