from pathlib import Path
import time
import os

def loggs():
    logs_folder = Path('logs')
    logs_folder.mkdir(exist_ok=True) # creating catalogues
    
    logs_file = logs_folder / 'new_log.txt'
    logs_file_old = logs_folder / 'old_log.log'
    logs_file.touch()   # creating files
    logs_file_old.touch()

    year = time.time() - (60*60*24*60)  # a 60 days

    os.utime(logs_file_old, (year, year)) # changing modification and access time of old logs





loggs()