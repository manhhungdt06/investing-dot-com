import os
from random import randrange
from pathlib import Path
import shutil


def check_exists(dirpath: Path = Path('DummyFolder')) -> bool:
    '''
    # dirpath = Path('dataset3') / 'dataset' # an example
    if dirpath.exists() and dirpath.is_dir():
        # shutil.rmtree(dirpath)    # if needed
        return True
    else:
        return False
    # '''
    
    # shorten version
    return (dirpath.exists() and dirpath.is_dir())


folder_name = "PythonPrograms"
current_folder = Path(__file__).parent.resolve()

FOLDER_NUMS = 2
RANGES = 10
for i in range(FOLDER_NUMS):
    number = int(randrange(0, RANGES))
    if check_exists(Path(f"{current_folder}/{folder_name}_{number}")):
        print(f"Folder {number} is already exist!")
    else:
        print(f"Creating folder {number}!")
        os.mkdir(f"{current_folder}/{folder_name}_{number}")
'''
Problem:
- FileExistsError: [Errno 17] File exists -> OKE
'''
