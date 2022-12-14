
from flask import Flask
import logging as logger

# logger.basicConfig(level="DEBUG")

logger.basicConfig(filename="logFile.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

flaskAppInstance =  Flask(__name__)

@flaskAppInstance.route("/")
def hello():
    flaskAppInstance.logger.info("Helloooo")
    return "Hello!!"

@flaskAppInstance.route("/get")
def get():
    from api.Task import Task
    t = Task()
    return t.get()

@flaskAppInstance.route("/post")
def post():
    from api.Task import Task
    t = Task()
    return t.post()

if __name__ == '__main__':
    logger.debug("Starting the app")
    
    flaskAppInstance.run(host="0.0.0.0", port=5005, use_reloader=True)