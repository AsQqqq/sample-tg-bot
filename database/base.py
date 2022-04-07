import sqlite3 as sq
import sqlite3

base = sq.connect('database.db')
cur = base.cursor()

def all_user():
    base.execute('\
    CREATE TABLE IF NOT EXISTS user(\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        user_id VARCHAR (255) NOT NULL,\
        status BBOLEAN NOT NULL DEFAULT (TRUE), \
        ban BBOLEAN NOT NULL DEFAULT (FALSE), \
        warning TEXT DEFAULT (0))')

class all_user_class:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
    
    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `user` WHERE `user_id` = ?', (user_id,)).fetchmany(1)
            return bool(len(result))
    
    async def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute('INSERT INTO `user` (user_id) VALUES (?)', (user_id,))

    async def edit_status(self, status, user_id):
        with self.connection:
            return self.cursor.execute('UPDATE `user` SET `status` = ? WHERE `user_id` = ?', (status, user_id,))


    def total_status(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `user` WHERE `user_id` = ? AND `status` = False',
                                     (user_id,)).fetchmany(2)
            return bool(len(result))

    def total_ban(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `user` WHERE `user_id` = ? AND `ban` = False',
                                     (user_id,)).fetchmany(3)
            return bool(len(result))

    async def number_plus_warning(self, user_id):
        with self.connection:
            self.cursor.execute('UPDATE `user` SET `warning`=warning+1 WHERE `user_id` = ?',
                                (user_id,))

    async def edit_warning(self, warning, user_id):
        with self.connection:
            self.cursor.execute('UPDATE `user` SET `warning` = ? WHERE `user_id` = ?',
                                (warning, user_id,))

    async def edit_ban(self, ban, user_id):
        with self.connection:
            self.cursor.execute('UPDATE `user` SET `ban` = ? WHERE `user_id` = ?',
                                (ban, user_id,))

    def exists_number_warning(self, warning, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `user` WHERE `warning` = ? AND `user_id` = ?',
                                (warning, user_id,))
            return result