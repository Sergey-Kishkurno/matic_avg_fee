from datetime import datetime
from time import sleep
from setup.setup import TIME_DELTA_DEFAULT


# A decorator for timing in the time series
def timing(func):
    """
    Timing decorator that stamps  the time before and after the measurement.

    If it will be necessary, support for parameters can be added.
    """
    def wrapper(*args, **kwargs):
        # Here we handle timing operations - before calling the function:
        print(f"Current time, when fetching: {datetime.now()}")

        # Calling the function:
        return_value = func(*args, **kwargs)

        # Here there could be some follow-up actions - after calling the function:
        # ...

        return return_value
    return wrapper


# A decorator for timing in the time series
def sleeping(sleeping_timedelta = TIME_DELTA_DEFAULT):
    """
    Timing decorator inserts the delay after function call
    By default the delay is TIME_DELTA_DEFAULT seconds.
    """
    def actual_decorator(func):
        def wrapper(*args, **kwargs):

            # Calling the function:
            return_value = func(*args, **kwargs)

            # Here we're waiting for N seconds - after calling the function:

            sleep(sleeping_timedelta)

            return return_value
        return wrapper
    return actual_decorator

