from flask import Flask, jsonify

app = Flask(__name__)

movies = ['homem-aranha', 'madagascar', 'harry-potter']

@app.route('/movies')
def get_movies():
    return jsonify(movies)

if __name__ == "__main__":

    PORT = 3000
    HOST = '0.0.0.0'
    print("Starting server...")

    app.run(host=HOST, port=PORT)