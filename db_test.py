from inspect import _void
import sqlite3
from audios.get_songs import read_audio_dir #callback procedure

class DataHandler:
    def get_data() -> list:
        try:
            connection = sqlite3.connect("db/save.sql")
            cursor = connection.cursor()

            cursor.execute(
                "CREATE TABLE song_data(meta str)")

            cursor.execute(
                "INSERT INTO song_data VALUES ('this')")

            connection.commit()

            saved_save = [cursor.execute("SELECT * FROM song_data")]
            for i in saved_save:
                for u in i:
                    to_ret: list = [u, cursor, connection]
                    return to_ret

        except Exception as e:
            print("err: ", e)

    @classmethod
    def reset_data_base(self) -> _void:
        data: list = self.get_data()
        for i in data:
            _info: object = data[0]
            _cursor: object = data[1]
            _connection: object = data[2] # sub by 1 instead of 2 to get db contents
            _info = ["data_one" == _info]
            if type(_info) is list:
                for u in i:
                    for j in _cursor:
                        print(j) # prints data saved within the _cursor object
                        _cursor.execute("DELETE * FROM song_data")
                    _connection.commit()
                    print(u) # printing 'u' here seems kinda... impractical
                    return _info
            print("Failed")
            _cursor.close()
            return

DataHandler.get_data()