import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="elzero",
    user="postgres",
    password="12345"
)

print("Connected Successfully")

cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS users(
        id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        name VARCHAR(20) UNIQUE,
        BirthOfDate Date UNIQUE,
        email VARCHAR(100)
    )
    """)

conn.commit()
#===========================================================

#
# cur.execute("""
# INSERT INTO users(name, birthofdate, email)
# VALUES
# ('Ahmed', '1980-10-20', 'a@elzero.org'),
# ('Sayed', '1990-10-20', 's@elzero.org'),
# ('Gamal', '1991-10-20', 'g@elzero.org'),
# ('Mahmoud', '1987-10-20', 'm@elzero.org'),
# ('Sameh', '2000-10-20', 'sameh@elzero.org');
# """)
conn.commit()
cur.execute('SELECT * FROM users')
# print(cur.fetchall())
#===========================================================

index = int(input("Enter user ID"))

var = cur.fetchall()
found = False

print("Show Other Data:")

for i in var:
    if i[0] == index:
        cur.execute("DELETE FROM users WHERE id = %s", (i[0],))
        print("User Deleted.")
        found = True
    else:
        print(
            f"ID => {i[0]}, "
            f"Name => {i[1]}, "
            f"Date Of Birth => {i[2].strftime('%d/%m/%Y')}, "
            f"Email => {i[3]}"
        )

if not found:
    print("User Not Found.")
else:
    conn.commit()


cur.close()
conn.close()
print("PostgreSQL database and users table are ready!")







