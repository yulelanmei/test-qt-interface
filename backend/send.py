import requests
import cv2
import base64
import json
import time


def send_data(image, dict):
    # 将图片数据编码为 Base64 格式
    _, image_encoded = cv2.imencode('.jpg', image)
    image_base64 = base64.b64encode(image_encoded).decode('utf-8')

    # 构建 JSON 数据
    dict['image_data'] = image_base64
    
    # 发送 POST 请求
    url = 'http://192.168.124.13:5001/receive'  # 替换为 Flask 服务器的 IP 地址和端口号
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(dict), headers=headers, timeout=30)

    # 解析响应
    if response.status_code == 200:
        print('Data sent successfully!')
    else:
        print('Failed to send data.')

def main():
    camera = cv2.VideoCapture(1)

    while True:
        success, frame = camera.read()
        if not success:
            print('read error!')
            break
        
        dict = {'action': 'fall', 'timestamp':time.strftime("%Y-%m-%d_%H_%M_%S", time.gmtime(time.time()+8*60*60))}
        send_data(frame, dict)

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
