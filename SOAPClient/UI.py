from flask import Flask, render_template, jsonify, request
import SOAPClient.soapsuds as suds
import SOAPClient.soapzeep as zeep

app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    return render_template('index.html')

@app.route("/getWeatherData", methods=['GET'])
def getWeatherData():

    longitude = request.args.get('longitude', 0)
    latitude = request.args.get('latitude', 1)
    maxt = request.args.get('maxt', 2)
    mint = request.args.get('mint', 3)
    dew = request.args.get('dew', 4)
    winddirection = request.args.get('wdir', 5)

    m1 = False
    m2 = False
    m3 = False
    m4 = False
    if maxt == 'true':
        m1 = True
    if mint == 'true':
        m2 = True
    if dew == 'true':
        m3 = True
    if waveh == 'true':
        m4 = True

    parameters = {'maxt': m1, 'mint': m2, 'dew': m3, 'wdir': m4}

    result = suds.getWeatherData_suds(longitude,latitude,parameters)

    return jsonify(result=result)

if __name__ == "__main__":
    app.run()