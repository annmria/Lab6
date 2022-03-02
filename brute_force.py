import multiprocessing
import time
import concurrent.futures
import numpy as np
from psutil import cpu_count
# import factorize_numbers
# import threading
# import psutil
import datetime

UI32 = np.iinfo(np.uint32)
secret_key = np.uint32(150000)
cpu_count = 4

cpus = []
cpu = []
start_keys = []
end_keys = []
cpu_key_space = np.uint32(UI32.max / cpu_count)
cur_key = []
end_key = []

# share variable between processes, notice large V in .Value
key_not_found = multiprocessing.Value('i', True)

# init global variables for processes
def init_globals(key_not_found):
    global KEY_NOT_FOUND
    KEY_NOT_FOUND = key_not_found
 
 # multiprocess function, notice small v in .value
def crack_something(cpu, cur_key, end_key):
    print(f'CPU: {cpu} keyspace start at {cur_key} and end at {end_key}')
    
    while KEY_NOT_FOUND.value and (cur_key <= end_key):
        if(cur_key == secret_key):
            KEY_NOT_FOUND.value = False
            print (f'\nCPU: {cpu} found secret key: {cur_key}')
        else:
            cur_key = cur_key + 1
        
        if(cur_key % 1_000_000 == 0):
            print(f'\nCPU {cpu} is at key: {cur_key}')
            
# när rätt nyckel hittats, visas "None" för att resterande cores inte längre räknar

        
def main():
    """ setup and receive result """
    for i in range(0, cpu_count):
        cpus.append(i)
        start_keys.append(i * cpu_key_space)
        end_keys.append((i+1) * cpu_key_space)
    
    # set last key coorect
    end_keys[-1] = np.uint32(UI32.max)
    
    print(f'Start keyspace offsets: {start_keys}')
    print(f'End keyspace offsets: {end_keys}')
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count, initializer=init_globals, initargs=(key_not_found,)) as executor:
        for result in executor.map(crack_something, cpus, start_keys, end_keys):
            print(result)
    
if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'\nFinished in {round(finish-start, 2)} seconds')
    keys_sec = int(secret_key / round(finish-start, 2) * cpu_count)
    print(f'\nAround {keys_sec} keys per second was tested')
    TOTAL_TIME = str(datetime.timedelta(seconds=int(np.uint32(UI32.max)/keys_sec)))