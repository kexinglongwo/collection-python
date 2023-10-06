import sqlite3


class CONLUMN:
    pass


class CURSOR:
    def __init__(self, cursor, table) -> None:
        self.cursor = cursor
        self.table  = table

    def __getitem__(self, __name) -> list:
        self.cursor.execute(f'SELECT "{__name}" FROM {self.table}')
        return [item[0] for item in self.cursor.fetchall() ]

    def __setitem__(self, __name, __value) -> None:
        if type(__value) not in [list, tuple]:
            __value = [__value]
       # print("INSERT INTO {} VALUES({})".format(self.table, ",".join( [ '"{}"'.format(item) for item in __value ])))
        self.cursor.execute(
            f"""INSERT INTO "{self.table}" VALUES({",".join([f'"{item}"' for item in __value])})"""
        )



class SQL:
    def __init__(self, file = ':memory:') -> None:
        self.connect = sqlite3.connect(file)
        self.cursor  = self.connect.cursor()

    def __setitem__(self, __name, __value) -> None:
        #print("table is done")
        if type(__value) not in [list, tuple]:
            __value = [__value]
        try:
            self.cursor.execute(
                'CREATE TABLE "{}"\n({});'.format(
                    __name, ',\n'.join([f'{item} TEXT' for item in __value])
                )
            )
        except sqlite3.OperationalError as e:
            print(e)

    def __getitem__(self, __name) -> CURSOR:
        return CURSOR(self.cursor, __name)
        
    def __del__(self) -> None:
        self.connect.commit()
        self.cursor .close()
        self.connect.close()


