import pymysql

def connect():
    return pymysq.connect(
    host= "localhost", 
    user="root", 
    password="root", 
    db="appdbproj")

def view_speakers_sessions():
    speaker = input("Enter speaker name: ")
    
    print (f"Sessions details for {speaker}")
    print ("------------------------------------------")
    conn = connect()
    cur = conn.cursor()

    query = """
        SELECT DISTINCT speakerName, sessionTitle, roomName
        FROM session
        JOIN room USING (roomID)
        WHERE speakerName LIKE %s
    """

    cur.execute(query, (f"%{speaker}%",))
    rows = cur.fetchall()

    if rows:
        for speakerName, sessionTitle, roomName in rows:
            print(f"Speaker: {speakerName} | Session: {sessionTitle} | Room: {roomName}")
    else:
        print("No speaker was found of that name")

    conn.close()
    
def view_attendees_by_company():
    if (not conn):
        connect();
        
        query = """ SELECT * FROM teacher where experience < %s"""
        
    with conn:
        
       
    
    conn.close()
    
def add_new_attendee():
    if (not conn):
        connect();
        
        query = """ SELECT * FROM teacher where experience < %s"""
        
    with conn:
        
       
    
    conn.close()
    
def add_attendee_connection():
    if (not conn):
        connect();
        
        query = """ SELECT * FROM teacher where experience < %s"""
        
    with conn:
        
       
    
    conn.close()

def view_rooms():
    if (not conn):
        connect();
        
        query = """ SELECT * FROM teacher where experience < %s"""
        
    with conn:
        
       
    
    conn.close()