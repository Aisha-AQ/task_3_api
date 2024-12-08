from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Render!"

@app.route('/deblur', methods=['POST'])
def deblur():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    # Save and process the image here (dummy response for now)
    return jsonify({"message": "Image processed!"}), 200

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
