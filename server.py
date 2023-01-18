# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify
import datetime
import scraper
from flask_cors import CORS, cross_origin
from flask.helpers import send_from_directory



x = datetime.datetime.now()
  
# Initializing flask app
app = Flask(__name__, static_folder = "frontend/build", static_url_path='')
CORS(app)
  

@app.route('/submit-data', methods=['POST'])
@cross_origin()
def inputs():
    data = request.get_json()
    input_data = data.get('input')
    input_string = input_data.replace(" ", "+")
    scrape_result = scraper.scrape_page(input_string)
    return jsonify({'status': 'success', 'input': '1', 'scrape': scrape_result})


@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

# Running app
if __name__ == '__main__':
    app.run(debug=True)