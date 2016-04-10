import sqlite3

database = 'books.db'

def setupdb(db=database):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    #create table here
    c.execute('''CREATE TABLE book
(id integer primary key autoincrement, title text, author text, series text, sort_order integer, genre text, isbn text)''')
    conn.close()

def cleardb(db=database):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('''drop table book''')
    conn.commit()
    conn.close()
    setupdb()

def debug(db = database, sortier=""):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    print('_'*80)
    print('|{:^5}|{:^35}|{:^20}|{:^15}|'.format('ID', 'Titel', 'Autor', 'ISBN'))
    c.execute("select * from book {}".format(sortier))
    conn.commit()
    entries = c.fetchall()
    for entry in entries:
        titel = entry[1]
        if len(titel) > 35:
            i = titel.index(' ', 20)
            row1 = titel[:i]
            row2 = titel[i+1:]
            print('|{:^5}|{:^35}|{:^20}|{:^15}|'.format(entry[0], row1, entry[2], entry[-1]))
            while len(row2) > 35:
                i = row2.index(' ', 20)
                row1 = row2[:i]
                row2 = row2[i+1:]
                print('|{:^5}|{:^35}|{:^20}|{:^15}|'.format(' ', row1, '', ''))
            print('|{:^5}|{:^35}|{:^20}|{:^15}|'.format(' ', row2, '', ''))
             

        else:
            print('|{:^5}|{:^35}|{:^20}|{:^15}|'.format(entry[0], entry[1], entry[2], entry[-1]))
    conn.close()
    
def go(db=database):
    conn = sqlite3.connect(db)
    c = conn.cursor()

    #execute, commit, close
    def savebook():
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN-10: ")
        return title, author, isbn

    for i in range(1000):
        title, author, isbn = savebook()
        c.execute("insert into book (title, author, isbn) values (?, ?, ?)", [title, author, isbn])
        conn.commit()

    conn.close()
    
if __name__ == '__main__':
    go()
    
