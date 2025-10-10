from flask import Flask, request, jsonify
from flask_cors import CORS  # 解决前端跨域问题（不同端口访问需要）

# 1. 初始化Flask应用
app = Flask(__name__)
# 2. 允许跨域（因为前端在浏览器打开是“file://”协议，后端在“http://localhost:5000”，需要允许跨域）
CORS(app)

# 3. 定义阶乘计算函数
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 4. 创建API接口：前端会POST请求这个地址
@app.route('/calculate-factorial', methods=['POST'])
def factorial_api():
    # 5. 接收前端传的JSON数据
    data = request.get_json()
    # 6. 提取前端传的数字
    number = data.get('number', 0)  # 没传数字的话默认算0的阶乘

    # 7. 计算阶乘
    factorial_result = calculate_factorial(number)

    # 8. 把结果包装成JSON返回给前端
    return jsonify({
        'status': 'success',
        'number': number,
        'factorial': factorial_result
    })

# 9. 启动后端服务（默认端口5000）
if __name__ == '__main__':
    app.run(debug=True)  # debug=True表示改代码后自动重启，方便测试