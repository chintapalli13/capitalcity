from flask import Flask, request
from flask import render_template
from src.services.capital_city import CountryCapitals as countries

app = Flask(__name__)

@app.route("/", methods =['GET'])
@app.route("/home", methods =['GET'])
def home():
    return render_template('index.html',)


@app.route("/country", methods=['GET' ,"POST"])
def country():
    country_code = request.form['country']
    if country_code:
        cp = countries(country_code).capital_city()
        return render_template('index.html', city = cp)
    else:
        return render_template('index.html', city='', message='Please input country code or name')


if __name__ == "__main__":
   app.run(debug=True)