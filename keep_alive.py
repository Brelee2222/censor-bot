import random
from flask import Flask, render_template
from threading import Thread

app = Flask('')

@app.route('/')
def index():
    return render_template("html.html")
def run():
  app.run(host="0.0.0.0", port=8580)

    
def keep_alive():
    server = Thread(target=run)
    server.start()

    

