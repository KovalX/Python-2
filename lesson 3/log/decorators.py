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



