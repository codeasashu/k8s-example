import os, json
from flask import Flask
import redis
from flask import jsonify, request
app = Flask(__name__)

r = redis.Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], db=0)

@app.route('/api')
def hello():
    return 'Welcome to my api!!'

@app.route('/api/add', methods=['POST'])
def addTask():
    content = request.get_json()
    r.rpush('task', content['task'])
    return json.dumps(content)

@app.route('/api/list', methods=['GET'])
def getTask():
    tasks = r.lrange('task', 0, -1)
    taskstr = [task.decode() for task in tasks]
    print("list2", taskstr)
    return json.dumps(taskstr)


if __name__ == '__main__':
    print("Server running at"+ os.environ['HOST'] +":"+ os.environ['PORT'])
    app.run(host=os.environ['BACKEND_HOST'], port=os.environ['BACKEND_PORT'], debug=True)
