import csv
import os
import psycopg2
from psycopg2.extras import RealDictCursor


def write_chat_to_csv(file_path, message):
    header = ["chat_id", "first_name", "last_name", "trello_username"]
    row = {
        "chat_id": message.chat.id,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "trello_username": message.text
    }

    with open(file_path, "a", newline="\n", encoding='utf8') as f:
        csv_writer = csv.DictWriter(f, header)
        if os.path.getsize(file_path) == 0:
            csv_writer.writeheader()
        print(row)
        csv_writer.writerow(row)
    print("Chat add successfully.")


def write_databse_trello( fullname ,chat_id , phone):
    connection = psycopg2.connect(
        dbname='trello',
        user='postgres',
        password='12345',
        host='localhost',
        port=5432
    )
    cur = connection.cursor(cursor_factory=RealDictCursor)
    sql = "insert into registration(full_name , chatid ,phone) values (%s, %s, %s)"
    cur.execute(sql, (fullname ,chat_id ,phone))
    connection.commit()


def check_chat_id_from_csv(file_path, chat_id):
    with open(file_path, encoding="utf-8") as f:
        csv_reader = csv.DictReader(f)
        return chat_id in [int(row.get("chat_id")) for row in csv_reader]


def get_trello_username_by_chat_id(file_path, chat_id):
    with open(file_path, encoding="utf-8") as f:
        csv_reader = csv.DictReader(f)
        users = [
            row.get("trello_username")
            for row in csv_reader
            if int(row.get("chat_id")) == chat_id
        ]
        return users[0] if users else None


def get_member_tasks_message(card_data, member_id):
    msg = ""
    for data in card_data:
        if member_id in data.get("idMembers"):
            msg += f"{data.get('idShort')} - <a href=\"{data.get('url')}\">{data.get('name')}</a>\n"

    return msg