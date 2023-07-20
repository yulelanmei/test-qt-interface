from flask import Flask, request
import cv2
import base64
import numpy as np
import json

app = Flask(__name__)

INFO = {
    'action' : '',
    'timestamp': '',
}

@app.route('/receive', methods=['POST'])
def receive_data():
    INFO['action'] = request.get_json()['action']
    INFO['timestamp'] = request.get_json()['timestamp']

    image_base64 = request.get_json()['image_data']
    image_data = base64.b64decode(image_base64)
    image_array = cv2.imdecode(np.frombuffer(image_data, dtype=np.uint8), cv2.IMREAD_COLOR)
    
    print('load')

    # 保存图片
    cv2.imwrite(f'./resources/img/{INFO["timestamp"]}.jpg', image_array)

    # 保存json
    json_name = INFO['timestamp'][:10]
    with open(f'./resources/json/{json_name}.json', 'a') as f:
        json.dump(INFO, f, indent=4)
        f.write('\n')

    return 'Received'

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port= 5001)