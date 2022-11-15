#!/usr/bin/env python3
import cgi
from LR15 import *

def id_find(con, req_id):
    curs = con.cursor()
    curs.execute(f'SELECT * FROM {tbl_name}')
    cc = curs.fetchall()
    for d in range(len(cc)):
        if cc[d][0] == req_id:
            return True

    return False


form = cgi.FieldStorage()
if form.getvalue('table_list') is not None:  # запись в файл
    tbl_name = form.getvalue('table_list')
    file = open("cgi-bin/table.txt", "w")
    file.write(form.getvalue('table_list'))
    file.close()
else:
    inp = open("cgi-bin/table.txt", "r")
    tbl_name = inp.read()
    inp.close()


print("Content-type: text/html\n")
print(f"""<!DOCTYPE HTML>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Work with table {tbl_name}</title>
            </head>
            <body>
                <form action="/index.html">
                    <p><input type="submit" value="Return to choice tables"></p>
                </form>
                <form action="/form.py">
                    <h3>What do you want to do with the table {tbl_name}?</h3>
                        <p><select name="act_list">
                        <option></option>
                        <option>Add an entry</option>
                        <option>Update an entry</option>
                        <option>Delete an entry</option>
                        <option>Show all entries</option>
                    </select></p>
                    <p><input type="submit" value="Sent"></p>
                """)

connection = sql_connection()
table_str = '<table><tr>\n'

act = form.getvalue('act_list')
if form.getvalue('act_list') is not None:  # запись в файл
    act = form.getvalue('act_list')
    file = open("option.txt", "w")
    file.write(form.getvalue('act_list'))
    file.close()
else:
    inp = open("option.txt", "r")
    act = inp.readline()
    inp.close()

if act is not None:
    if act == 'Add a entry':
        print("""
                Enter the data of the new entry separated by a space: <input type="text" name="new_tran">
                <p><input type="submit" value="Sent"></p>
                    <style>
                    input[type="text"] 
                    {
                        width: 300px;
                    }
                    </style>
               </form>
        """)

        cursorObj = connection.cursor()
        cursor = connection.cursor()
        row = form.getfirst("new_tran").split()
        cursor.execute(f'SELECT * FROM {tbl_name}')  # имя таблицы можно хранить в файле
        headers = [description[0] for description in cursor.description]

        if len(row) < len(headers) - 1 or len(row) >= len(headers):
            print("""An incorrect number of arguments was entered -> the entry was not added to the table""")
        elif len(row) == len(headers) - 1:

            fields = ""
            for j in range(len(row)):
                fields += '?, '
            fields = fields[:-2]
            cursorObj.execute(f'INSERT INTO {tbl_name} VALUES(null, {fields})', row)
            connection.commit()
            print("""the entry was successfully added to the table""")

        file = open("option.txt", "w")
        file.write('None')
        file.close()

    if act == 'Update an entry':
        print("""
                        Запись обновления: <input type="text" name="update_id"><br /><br />
                        Enter the updated record data separated by a space: <input type="text" name="update_tran">
                        <p><input type="submit" value="Sent"></p>
                            <style>
                            input[name="update_tran"] 
                            {
                                width: 300px;
                            }
                            input[name="update_id"]
                            {
                                width:50px;
                            }
                            </style>
                       </form>
                """)

        cursorObj = connection.cursor()
        update_id = int(form.getfirst("update_id"))
        row = form.getfirst("update_tran").split()
        cursorObj.execute(f'SELECT * FROM {tbl_name}')
        headers = [description[0] for description in cursorObj.description]

        find = id_find(connection, update_id)
        sql_str = 'UPDATE ' + tbl_name + ' SET '

        if len(row) < len(headers) - 1 or len(row) >= len(headers):
            print('An incorrect number of arguments was entered -> the entry was not added to the table')
        elif not find:
            print('there is no record with this id')
        elif len(row) == len(headers) - 1 and find:
            for i in range(len(row)):
                sql_str += headers[i + 1] + ' = "' + row[i] + '", '
            sql_str = sql_str[:-2]
            sql_str += ' where id = ' + str(update_id)
            cursorObj.execute(sql_str)
            connection.commit()
            print("record changed successfully")

        file = open("option.txt", "w")
        file.write('None')
        file.close()

    if act == 'Delete an entry':
        print("""
                        Enter the id of the record you want to delete: <input type="text" name="delete_id">
                        <p><input type="submit" value="Sent"></p>
                            <style>
                            input[name="delete_id"]
                            {
                                width:50px;
                            }
                            </style>
                       </form>
                """)

        cursorObj = connection.cursor()
        delete_id = int(form.getfirst("delete_id"))
        find = id_find(connection, delete_id)
        if find:
            cursorObj.execute(f'DELETE from {tbl_name} where id = {delete_id}')
            connection.commit()
            print("the record was successfully deleted")
        else:
            print('there is no record with this id')

    file = open("option.txt", "w")
    file.write('None')
    file.close()

if act == 'Output all entries':
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {tbl_name}')  # имя таблицы можно хранить в файле
    headers = [description[0] for description in cursor.description]
    for i in range(len(headers)):
        table_str += '<th>' + headers[i] + '</th>'
    table_str += '</tr>\n\n'

    for row in cursor.fetchall():
        table_str += '<tr>\n'
        tmp = list(row)
        for i in range(len(tmp)):
            table_str += '<td>' + str(tmp[i]) + '</td>'
        table_str += '</tr>\n'

    table_str += """<style>table {
           border: 1px solid grey;
           border-collapse: collapse;
            }
           td {
           border: 1px solid grey;
           text-align: center;
            }
            th {
           border: 1px solid grey;
           min-width:160px;
            }
        </table>
        </style>"""
    print(table_str)
    print('</table>')
    file = open("option.txt", "w")
    file.write('None')
    file.close()

print("""</body>
         </html>""")