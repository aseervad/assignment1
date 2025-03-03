from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the IELTS Speaking Test Platform!"})

@app.route('/info')
def info():
    return jsonify({
        "platform_name": "IELTS Speaking Test Platform",
        "version": "1.0",
        "developer_contact": "support@example.com"
    })

if __name__ == "__main__":
    app.run(debug=True)