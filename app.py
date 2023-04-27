from flask import Flask, request,render_template
import pandas as pd
app = Flask(__name__)
df = pd.read_csv("data/pledges.csv", index_col=0)
df.rename(columns=df.iloc[0]).drop(df.index[0])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/points')
def display_points():
    df.to_html(header="true", table_id="table")
    return render_template('points_page.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        df.at[form_data['Name'], 'Points'] = form_data['Points']
        return render_template('points_page.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)