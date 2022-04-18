import sqlite3
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
                    saved = inserted
                    dng = True
        if dng:
             # try generating another
            try:
                sec_gen = random.randrange(num/2, 3000)
                if sec_gen != saved:
                    failed.append(sec_gen)
                    print(sec_gen)
                    return failed
                return
            except:
                connection = sqlite3.connect("saved.sql")
                cursor = connection.cursor()
                cursor.execute(
                    "CREATE TABLE saved (f int)")

                for i in failed:
                    cursor.execute(
                        "INSERT INTO saved(f) VALUES (%d)" % i)

                connection.commit()

                for saved in cursor.execute("SELECT * FROM saved"):
                    print("Generated non-integer number... canceling (saved %s into database)" % saved)

                cursor.close()

        elif input() == "yes" and not dng:
            success = [num]
            print("Thank you for using gen-dot-py")
            return success

gen()
