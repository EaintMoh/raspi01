from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/post', methods=['POST', 'GET'])
def post_handler():
    print("data",request.data.decode('utf-8')) # should display 'bar'
    a = request.data.decode('utf-8')
    return render_template('aaa.html', aaa=a)  # response to your request.

# @app.route('/')
# def index():
#     aaa = post_handler()
#     print("aaa",aaa)
#     return render_template('aaa.html', aaa=aaa) 
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)