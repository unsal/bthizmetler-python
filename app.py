from flask import Flask
from api.projeler_api import ProjelerApi
from flask_cors import CORS

app = Flask(__name__)

# React tarafında Access-Control-Allow-Origin hatasını önlemek için
CORS(app)

# app.config.from_object('config.Config')

@app.route('/')
def root():
    return 'Python Web Server working successfully...'

@app.route('/projeler', methods=['GET'])
def api_projeler():
    api = ProjelerApi()
    return api.message()

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    print("Server started successfully!")






