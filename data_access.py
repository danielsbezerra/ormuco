#!/usr/bin/env python

from flask import Flask, escape, flash
import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except:
        flash('Failed to create database connection')
    return None


def select_all_preferences(conn):
    """
    Query all rows in the preferences table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    #import ipdb; ipdb.set_trace() # the same as breakpoint()
    cur.execute("SELECT * FROM preferences")
    return cur.fetchall()
    


def insert_preference(conn, preference):
    """
    Create a new preference into the preferences table
    :param conn:
    :param preference:
    """
    sql = ''' INSERT INTO preferences(name,favorite_color,pet)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    #import ipdb; ipdb.set_trace() # the same as breakpoint()
    cur.execute(sql, preference)
    conn.execute("COMMIT")