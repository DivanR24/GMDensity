from flask import Flask
from flask import render_template
import map_gen


app = Flask(__name__)

@app.route('/')
def rend_map():
  map_gen.fetch_map()
  return render_template("index.html")



app.run(host='0.0.0.0', port=8080)


#note: this is planned to be implemented in the future for real-time updates via a flask web app, or we may use django if it will serve better.