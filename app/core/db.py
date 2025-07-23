import sqlite3
import logging

def create_DB():
    logger = logging.getLogger(__name__)
    
    logger.info("Start creating a DB")
    
    connection = sqlite3.connect('app/data/db/test_bibizianka.db')
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    logger.info("Create connection with bd, and create cursor")
    
    try:
        
        # Create a Users table
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        score INTEGER DEFAULT 0
                    )
                    ''')
        logger.info("Create a Users table")
        
        # Create a Tasks table
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        userid INTEGER NOT NULL,
                        score INTEGER NOT NULL,
                        name TEXT NOT NULL,
                        description TEXT,
                        is_done BOOLEAN DEFAULT FALSE,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
                    )
                    ''')
        logger.info("Create a Tasks table")
        
        # Create a Market table
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Market (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        userid INTEGER NOT NULL,
                        price INTEGER NOT NULL,
                        product_name TEXT NOT NULL,
                        is_buy BOOLEAN DEFAULT FALSE,
                        FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
                    )
                    ''')
        logger.info("Create a Market table")
        
        connection.commit()
        logger.info("BD was created")
    except sqlite3.Error as error:
        logger.error(f"Error at create BD: {error}")
    
    finally:
        connection.close()