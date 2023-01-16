# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify
import datetime
  
x = datetime.datetime.now()
  
# Initializing flask app
app = Flask(__name__)
  
  

@app.route('/submit-data', methods=['POST'])
def inputs():
    data = request.get_json()
    input_data = data.get('input')
    return (jsonify({'status': 'success', 'input':input_data}))
    


# Route for seeing a data
@app.route('/data')
def get_time():
  
    # Returning an api for showing in  reactjs
    return {
        'Name':"geek", 
        "Age":"24",
        "Date":x, 
        "programming":"python"
        }
  
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)