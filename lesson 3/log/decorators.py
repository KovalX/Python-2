def log(logger):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                err = "There was an exception in {}".format(func.__name__)
                logger.exception(err)
                raise
        return wrapper
    return decorator



























#from functools import wraps


#class Log:

    #def __init__(self, logger):
        #self.logger = logger

    #@staticmethod
    #def _create_message(result=None, *args, **kwargs):

        #message = ""
        #if args:
            #message += 'args: {}'.format(args)
        #if kwargs:
            #message += 'kwargs: {}'.format(kwargs)
        #if result:
            #message += '= {}'.format(result)
        #return message

    #def __call__(self, func):

        #@wraps(func)
        #def decorated(*args, **kwargs):
            #result = func(*args, **kwargs)
            #message = Log._create_message(result, *args, **kwargs)
            #self.logger.info('{} - {} - {}'.format(message, func.__name__, func.__module__))
            #return result

        #return decorated

