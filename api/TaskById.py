from flask_restful import Resource  

class TaskById(Resource):

    def get(self, taskId):
        import logging as logger
        logger.debug("Inside get by Id method")
        return {"message":f"This is the get by Id method, TASK_ID={taskId}"}, 200

    def post(self, taskId):
        import logging as logger
        logger.debug("Inside post by Id method")
        return {"message":f"This is the post by Id method, TASK_ID={taskId}"}, 200