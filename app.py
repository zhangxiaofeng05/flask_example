from flask import Flask,request
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

# 配置 ProxyFix
# x_for=1 表示信任来自第一层代理（通常是你的 CDN）的 X-Forwarded-For 头信息
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)

@app.route('/')
def index():
    return "Hello, World!"

@app.route("/get",methods=["GET"])
def get():
    name = request.args.get("name")
    app.logger.info(name)
    return f"hello, {name}"

@app.route("/post",methods=["POST"])
def post():
    name = request.form.get("name")
    app.logger.info(name)
    return f"hello, {name}"

# 获取请求 ip
@app.route("/ip",methods=["GET"])
def get_ip():
    visitor_ip = request.remote_addr
    app.logger.info(visitor_ip)
    return f"{visitor_ip}"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=20135)
