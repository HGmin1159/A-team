import sqlite3
import pandas as pd

pathfrom = "experiment/2015_축제_위경도 추가_수정.csv"
pathto = "experiment/2015_festival.db"

df = pd.read_csv(pathfrom, encoding="utf-8")

conn = sqlite3.connect(pathto)

def create_festival():
    df.to_sql("festival", conn)

def create_restaurants():
    c = conn.cursor()
    c.execute('''CREATE TABLE "restaurants" (
        "address_name" TEXT,
            "category_group_code" TEXT,
            "category_group_name" TEXT,
            "category_name" TEXT,
            "distance" INTEGER,
            "id" INTEGER,
            "phone" TEXT,
            "place_name" TEXT,
            "place_url" TEXT,
            "road_address_name" TEXT,
            "x" TEXT,
            "y" TEXT,
            "festival_index" INTEGER,
            FOREIGN KEY("festival_index") REFERENCES festival("index")
    );''')
    conn.commit()