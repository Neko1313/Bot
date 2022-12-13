import sqlite3

class Database:
    def __init__(self,db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor  = self.connection.cursor()
    
    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `us` WHERE `user_id`= ?", (user_id,)).fetchall()
            return bool(len(result))
    
    def add_user(self,user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `us` (`user_id`) VALUES (?)",(user_id,))

    def count_FIO(self,user_id):
        with self.connection:
            fio = self.cursor.execute("SELECT `FIO` FROM `us` WHERE `user_id` = ?",(user_id,)).fetchone()[0]
            return fio
        
    def count_tele(self,user_id):
        with self.connection:
            tele = self.cursor.execute("SELECT `tele` FROM `us` WHERE `user_id` = ?",(user_id,)).fetchone()[0]
            return tele
    
    def plus_ans(self,user_id, answer):
        with self.connection:
            ans = self.cursor.execute("SELECT `answers` FROM `us` WHERE `user_id` = ?",(user_id,)).fetchone()[0]
            ans = str(ans)
            ans += answer
            self.cursor.execute("UPDATE `us` SET `answers` = ? WHERE `user_id`= ?",(ans,user_id,))
            self.connection.commit()
    
    def update_tele(self, user_id, phono):
        with self.connection:
            telephon = self.cursor.execute("SELECT `tele` FROM `us` WHERE `user_id` = ?",(user_id,)).fetchone()[0]
            telephon = phono
            self.cursor.execute("UPDATE `us` SET `tele` = ? WHERE `user_id`= ?",(telephon,user_id,))
            self.connection.commit()

    def update_fio(self, user_id, fio):
        with self.connection:
            fio_on = self.cursor.execute("SELECT `FIO` FROM `us` WHERE `user_id` = ?",(user_id,)).fetchone()[0]
            fio_on = fio
            self.cursor.execute("UPDATE `us` SET `FIO` = ? WHERE `user_id`= ?",(fio_on,user_id,))
            self.connection.commit()
    
    def update_specialization(self, user_id, sp):
        with self.connection:
            specialization = self.cursor.execute("SELECT `specialization` FROM `us` WHERE `user_id` = ?",(user_id,)).fetchone()[0]
            specialization = sp
            self.cursor.execute("UPDATE `us` SET `specialization` = ? WHERE `user_id`= ?",(specialization,user_id,))
            self.connection.commit()
    
    def count_answers(self,user_id):
        with self.connection:
            answers = self.cursor.execute("SELECT `answers` FROM `us` WHERE `user_id` = ?",(user_id,)).fetchone()[0]
            return answers
        
    def count_specialization(self,user_id):
        with self.connection:
            specialization = self.cursor.execute("SELECT `specialization` FROM `us` WHERE `user_id` = ?",(user_id,)).fetchone()[0]
            return specialization