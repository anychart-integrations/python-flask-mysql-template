import MySQLdb
import MySQLdb.cursors
from flask import Flask, render_template, json

app = Flask(__name__)

database = MySQLdb.connect(host = "localhost", 
	user = "anychart_user",
	passwd = "anychart_pass", 
	db = "anychart_db", 
	cursorclass = MySQLdb.cursors.DictCursor)
cursor = database.cursor()

@app.route("/")
def main():
	cursor.execute("SELECT name, value FROM fruits ORDER BY value DESC LIMIT 5")
	data = cursor.fetchall()
	chart = {
		"chart": {
			"type": "pie",
			"title": "Top 5 fruits",
			"data": data,
			"container": "container"
		}
	}
	return render_template("index.html", title = "Anychart Python template", chartData = json.dumps(chart))

if __name__ == "__main__": 
	app.run()