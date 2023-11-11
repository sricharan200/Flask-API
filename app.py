from flask import Flask,jsonify
import sqlite3
conn = sqlite3.connect('my_data.db')
c = conn.cursor()
alldata = c.execute('''SELECT * FROM users''').fetchall() 


app = Flask(__name__)
@app.route('/covid/<country>/<dt>')
def home(country,dt):
    enddata = []
    date = dt
    month = date[0:2]
    year = date[2:]
    for data in alldata:
        if data[2]!=None:
            
            if country.lower() == data[3].lower():
                
                yid = data[1].split('/')
                if month == yid[1] and year == yid[2]:
                    temp = {}
                    temp['ObservationDate'] = yid[2]+yid[0]+yid[1]
                    temp['State'] = data[2]
                    temp['Confirmed'] = int(data[-3])
                    temp['Deaths'] = int(data[-2])
                    temp['Recovered'] = int(data[-1])
                    enddata.append(temp)
    return jsonify(enddata)


if __name__ == '__main__':
    app.run()