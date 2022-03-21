from distutils.log import debug
from flask import Flask, jsonify, request
from yolo_detection_images import detectObject

app = Flask(__name__)

@app.route('/')
def hello():
    return {'msg' : 'Hello World!!'}

@app.route('/detect')
def detect():
    img = request.args['image']
    print(img)
    img_path = 'YOLO-v3-Object-Detection-master/images/' + img
    print(img_path)
    results = detectObject(img_path)
    return jsonify(results)

#run app api
app.run(debug=True)