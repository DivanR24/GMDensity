from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import map_gen


app = Flask(__name__)

@app.route('/')
def rend_map():
  map_gen.fetch_map()
  return render_template("index.html")



app.run(host='0.0.0.0', port=8080)