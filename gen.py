import math
import random

def gen() -> int:
    num = random.randrange(1, 3000)
    dng = False
    print(math.floor(num/2))
    if num:
        if input() == "no":
            failed = [num]
            for inserted in failed:
                if num == inserted:
                    dng = True
        if dng:
             # try generating another
            try:
                sec_gen = random.randrange(num/2, 3000)
                print(sec_gen)
                return failed
            except:
                print("Generated non-integer number... Canceling")

        elif input() == "yes" and not dng:
            success = [num]
            return success

gen()
