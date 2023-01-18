# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify
import datetime
import scraper

x = datetime.datetime.now()
  
# Initializing flask app
app = Flask(__name__)
  
  

@app.route('/submit-data', methods=['POST'])
def inputs():
    data = request.get_json()
    input_data = data.get('input')
    input_string = input_data.replace(" ", "+")
    scrape_result = scraper.scrape_page(input_string)
    return jsonify({'status': 'success', 'input': '1', 'scrape': scrape_result})
    

# Running app
if __name__ == '__main__':
    app.run(debug=True)