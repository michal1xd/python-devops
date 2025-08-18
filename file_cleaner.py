import time
from pathlib import Path


def cleaner():
    max_age_days = 30 # 30 days
    target_directory = Path('logs')
    age_in_days = max_age_days*24*60*60 
    dry_run = True

    for i in target_directory.iterdir():
        file_mod_time = i.stat().st_mtime
        file_mod_time = time.time() - file_mod_time

        if file_mod_time > age_in_days:
            print(f'{i} is an old file')
            if dry_run:
                print(f'{i} hasnt been removed')
            else:
                print(f'{i} has been removed')
                i.unlink()
        else:
            print(f'{i} is not an old file')



cleaner()