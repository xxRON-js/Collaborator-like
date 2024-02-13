from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Collaborator Server is running!"

@app.route('/notify', methods=['POST'])
def notify():
    data = request.get_data(as_text=True)
    print(f"Received notification: {data}")
    return "Notification received!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
