from flask_restful import Resource  


class Task(Resource):

    def get(self):
        import logging as logger
        logger.debug("Inside get method")
        return {"message":"inside get method"}, 200

    def post(self):
        import logging as logger
        logger.debug("Inside post method")
        return {"message":"inside post method"}, 200