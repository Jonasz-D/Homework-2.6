import sqlite3

NUM_OF_QUERRIES = 10

def run_querry(inner_path):
    with open(inner_path, 'r') as f:
        sql = f.read()

    with sqlite3.connect('school.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

if __name__ == '__main__':
    for querry in range(1, NUM_OF_QUERRIES + 1):
        inner_path = f'querries/querry_{querry}.sql'
        msg = f'\nQuerry number: {querry}\n'
        print(msg)
        for el in run_querry(inner_path):
            print(el)