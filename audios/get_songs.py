import os
class read:
    def read_audio_dir(self) -> str:
        read = os.scandir(self)
        for i in read:
            print(i)
            dir_entry_str: str = str(i)
            for ex in self:
                if dir_entry_str != ex and len(self) < 1:
                    clean: list = dir_entry_str.split("<DirEntry ")
                    for i in clean:
                        sec_clean: list = i.split(">")
                        for u in sec_clean:
                            return u
                else:
                    print("could not find song")