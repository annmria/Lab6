import multiprocessing
import concurrent.futures
import numpy as np

keyNumber = np.uint32(150000)

# init global variables for processes
def init_globals(key_not_found):
 global KEY_NOT_FOUND
 KEY_NOT_FOUND = key_not_found
 
 # multiprocess function, notice small v in .value
def crack_something(cpu, cur_key, end_key):
 print('CPU: {cpu} keyspace start at {cur_key} and end at {end_key}')
 
 # share variable between processes, notice large V in .Value
key_not_found = multiprocessing.Value('i', True)
with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count, initializer=init_globals, initargs=(key_not_found,)) as executor:
    for result in executor.map(crack_something, cpus, start_keys, end_keys):
        print(result)

while KEY_NOT_FOUND.value and (cur_key <= end_key):