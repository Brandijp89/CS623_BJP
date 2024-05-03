
import psycopg2

# Connection URL
conn_url = "postgresql://postgres:brandijp89cm@localhost:5432/marketdb"

try:
    # Connect to the database
    conn = psycopg2.connect(conn_url)
    print("Connected to database...")

    # Start transaction
    conn.autocommit = False

    # Your transactional operations here...
    # For example:
    with conn.cursor() as cur:
#        cur.execute("DELETE FROM Product WHERE prod = 'p1'")
#        cur.execute("DELETE FROM Stock WHERE prod = 'p1'")
        
#        cur.execute("DELETE FROM Depot WHERE dep = 'd1'")
#        cur.execute("DELETE FROM Stock WHERE dep = 'd1'")
        
    #    cur.execute("UPDATE Product SET pname = 'pp1' WHERE prod = 'p1'")
    #    cur.execute("UPDATE Stock SET prod = 'pp1' WHERE prod = 'p1'")
 
 #       cur.execute("UPDATE Depot SET addr = 'dd1' WHERE dep = 'd1'")
  #      cur.execute("UPDATE Stock SET dep = 'dd1' WHERE dep = 'd1'")
        
        cur.execute("INSERT INTO Product (prod, pname, price) VALUES ('p100', 'cd', 5)")
        cur.execute("INSERT INTO Stock (prod, dep, quantity) VALUES ('p100', 'd2', 50)")
        
     #   cur.execute("INSERT INTO Depot (dep, addr, volume) VALUES ('d100', 'Chicago', 100)")
      #  cur.execute("INSERT INTO Stock (prod, dep, quantity) VALUES ('p1', 'd100', 100)")
        

    # Commit transaction
    conn.commit()
    print("Transactions committed successfully!")

except psycopg2.Error as e:
    print("Error executing transactions:", e)

finally:
    # Close database connection
    if conn:
        conn.close()
        print("Connection closed.")
