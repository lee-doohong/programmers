from functools import wraps
import time

def check_time(func) :
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        
        result = func(*args, **kwargs)

        end = time.time()

        print(f"[{func.__name__}] 소요 시간 : {end - start : .2f}초")
        return result
    return wrapper

@check_time
def process_data_1():
    time.sleep(1)

@check_time
def process_data_2():
    time.sleep(2)

print(process_data_1.__name__)
process_data_2()    