import os

def read_audio_dir(self) -> str:
    read = os.scandir(self)
    for i in read:
        print(i)
        dir_entry_str: str = str(i)
        return dir_entry_str

read_audio_dir(os.curdir)