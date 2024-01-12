from flask import Flask, render_template, Response
import random
import time

app = Flask(__name__)

def get_wind_speed():
    # Simulate wind speed data (replace with your actual data retrieval logic)
    return [round(random.uniform(1.0, 10.0), 2) for _ in range(6)]

def generate_wind_speed():
    while True:
        time.sleep(1)  # Update every 1 second
        wind_speeds = get_wind_speed()
        yield f"data: {';'.join(map(str, wind_speeds))}\n\n"

@app.route('/')
def index():
    return render_template('index_sse.html')

@app.route('/stream')
def stream():
    return Response(generate_wind_speed(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
