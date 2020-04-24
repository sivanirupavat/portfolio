from flask import Flask, render_template,request, jsonify,send_from_directory

app = Flask(__name__)


@app.route("/")
def parent():
  return render_template("home.html")



if __name__=='__main__':
  app.run(debug=True)  