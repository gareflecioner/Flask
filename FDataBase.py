import math
import os.path
import sqlite3
import time
from flask import Flask, render_template, request, redirect, url_for, flash, g
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

class FDataBase:
    def __int__(self,db):
        self.__db=db
        self.__cur=db.cursor()
    def getMenu(self):
        sql="""SELECT * FROM mainmenu"""
        try:
            self.__cur.execute(sql)
            res=self.__cur.fetchall()
            if res: return res
        except:
            print("Error")
            return[]

    def addPost(self,name,email,text):
        try:
            tm=math.floor(time.time())
            self.__cur.execute("INSERT INTO feedd (name,email,text,tm) VALUES(?,?,?,?)" ,(name,email,text,tm,))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления статьи", str(e))
            return False
        return True


    def addUser(self,name,email,hpsw):
        try:
            self.__cur.execute(f"SELECT COUNT() as `count` FROM register WHERE email LIKE '{email}'")
            res=self.__cur.fetchone()
            if res['count']>0:
                print("Такой email уже существует")
                return False

            tm=math.floor(time.time())
            self.__cur.execute("INSERT INTO register (name,email,hpsw,tm) VALUES(?,?,?,?)",(name,email,hpsw,tm,))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка при добавлении пользователя в бд",str(e))
            return False
        return True