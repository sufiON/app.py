from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def location():
    location_data = request.get_json()
    if not location_data:
        print("No data received")
        return jsonify({"error": "No data received"}), 400

    latitude = location_data.get('latitude')
    longitude = location_data.get('longitude')

    if not latitude or not longitude:
        print("Incomplete data received")
        return jsonify({"error": "Incomplete data received"}), 400

    print(f"Received Location: Latitude {latitude}, Longitude {longitude}")
    return jsonify({"message": "Location data received successfully!"})

@app.after_request
def add_cache_control(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

if __name__ == '__main__':
    app.run(debug=True)
