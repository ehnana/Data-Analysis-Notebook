import sqlite3

# Connect to Database customer.db (does not already exist)

conn = sqlite3.connect('customer.db')

# ------------------ Create a Database Table -----------------

# Create a cursor
c = conn.cursor()

# Create a Table
c.execute('''CREATE TABLE customers1 (
            first_name text,
            last_name text,
            email text)''')

# Data types: NULL INTEGER REAL TEXT BLOB

# Commit our command
conn.commit()


# ------------------ INSERT ONE RECORD IN A TABLE ---------

c.execute('''INSERT INTO customers1 VALUES('Emna', 'HNANA', 'emna@gmail.com')
            ''')
print(" Command executed successfully ")

conn.commit()

# Close our connection
conn.close()