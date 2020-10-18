from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import stringbuilder

# Flask App
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello():
    weather_string = stringbuilder.getRandomWeatherString()
    return render_template('frontpage.html', weather_string=weather_string)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))