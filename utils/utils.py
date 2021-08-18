from datetime import datetime, time
import time


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

        # Here there are some actions - after calling the function:
        # ...

        return return_value
    return wrapper


