import requests, time

def DataBase_API(mode, target, var, text = 'DataBase'):

    app = requests.get(f'http://free-online-db-maker.herokuapp.com/api?{target}%&%{mode}%&%{var}%&%{text}')
    
    time.sleep(0.3)
    
    app = requests.get(f'http://free-online-db-maker.herokuapp.com/api')

    if 'Error You Can Not' in app.text:

        print ('\033[91m Error You Can Not Save Password, Email, Link, Number, Payment Card Number In Thi\'s DB')
        exit()
        # return 'Error You Can Not Save Password, Email, Link, Number, Payment Card Number In Thi\'s DB'

    # print (f'http://free-online-db-maker.herokuapp.com/api?{target}%&%{mode}%&%{var}%&%{text}')

    cat = len(list(str(app.text)))
    
    if cat == 20:

        return "Error db.907"

    return app.text

# def DataBase_API3(mode, target, var, text = ''):

#     app = requests.get(f'http://free-online-db-maker.herokuapp.com/api?{target}%&%{mode}%&%{var}%&%{text}')
    
#     time.sleep(0.3)
    
#     app = requests.get(f'http://free-online-db-maker.herokuapp.com/api?{target}%&%{mode}%&%{var}%&%{text}')


#     return app.text


db = ''

class Database():


    def __init__(self, uid):

        global db

        db = uid

    def delete(self, var):

        global db

        return DataBase_API ('delete', db, var)

    def read(self, var):

        global db

        return DataBase_API ('read', db, var)

    # def delete(self, var):

    #     global db

    #     return DataBase_API3 ('delete', db, var)

    def write(self, var, text):

        global db

        return DataBase_API ('write', db, var, text)

# print(DataBase_API('write', 'kWsgz5n4-NiBJpYlAAAB', 'Hello', 'My_Data'))

# db_ = DataBase('bA3R6ECCCiGG_UA8AAAB')

# db_.write('Data', 'My_Data')

# print(db_.delete('hi'))

# print (db_.read('Data'))
