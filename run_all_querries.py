import sqlite3

NUM_OF_QUERIES = 10

def run_querry(inner_path):
    with open(inner_path, 'r') as f:
        sql = f.read()

    with sqlite3.connect('school.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

if __name__ == '__main__':
    for query in range(1, NUM_OF_QUERIES + 1):
        inner_path = f'queries/query_{query}.sql'
        msg = f'\nQuery number: {query}\n'
        print(msg)
        for el in run_querry(inner_path):
            print(el)