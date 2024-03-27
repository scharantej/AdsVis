### main.py


from flask import Flask, render_template, request, redirect, url_for, flash
import csv

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        campaign_name = request.form['campaign_name']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        budget = request.form['budget']

        with open('campaigns.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([campaign_name, start_date, end_date, budget])

        flash('Campaign details submitted successfully!')
        return redirect(url_for('index'))

@app.route('/results')
def results():
    with open('campaigns.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        campaigns = [row for row in csvreader]

    return render_template('results.html', campaigns=campaigns)

@app.route('/download')
def download():
    with open('campaigns.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        campaigns = [row for row in csvreader]

    with open('campaigns.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Campaign Name', 'Start Date', 'End Date', 'Budget'])
        for campaign in campaigns:
            csvwriter.writerow(campaign)

    return redirect(url_for('results'))

if __name__ == '__main__':
    app.run(debug=True)
