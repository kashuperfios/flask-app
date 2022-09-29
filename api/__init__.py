from flask_restful import Api
from applic import flaskAppInstance
from api.Task import Task
from api.TaskById import TaskById
restServer = Api(flaskAppInstance)

restServer.add_resource(Task, "/api/task")
restServer.add_resource(TaskById, "/api/task/id/<string:taskId>")



