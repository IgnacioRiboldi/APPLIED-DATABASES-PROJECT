import pymysql
import main
import datetime

def connect():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        db="appdbproj"
    )

def view_speakers_sessions():
    speaker = input("Enter speaker name: ")

    print(f"\nSessions details for {speaker}")
    print("------------------------------------------")

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

    conn = connect()
    cur = conn.cursor()

    while True:
        user_input = input("Enter Company ID: ")
        try:
            company_id = int(user_input)
            if company_id > 0:
                break
        except ValueError:
            pass

    cur.execute(
        "SELECT companyName FROM company WHERE companyID = %s",
        (company_id,)
    )
    company = cur.fetchone()

    if not company:
        print(f"Company with ID {company_id} doesn't exist")
        conn.close()
        return

    company_name = company[0]

    query = """
        SELECT DISTINCT 
            a.attendeeName, 
            a.attendeeDOB, 
            s.sessionTitle, 
            s.speakerName, 
            s.sessionDate, 
            ro.roomName
        FROM attendee a
        INNER JOIN registration r 
            ON a.attendeeID = r.attendeeID
        INNER JOIN session s 
            ON r.sessionID = s.sessionID
        INNER JOIN room ro 
            ON s.roomID = ro.roomID
        WHERE a.attendeeCompanyID = %s
    """

    cur.execute(query, (company_id,))
    rows = cur.fetchall()

    if rows:
        print(f"\n{company_name} Attendees:\n")
        for attendeeName, attendeeDOB, sessionTitle, speakerName, sessionDate, roomName in rows:
            print(f"Attendee: {attendeeName} | DOB: {attendeeDOB} | Session: {sessionTitle} | Speaker: {speakerName} | Date: {sessionDate} | Room: {roomName}")
    else:
        print(f"No attendees found for {company_name}")

    conn.close()

from datetime import datetime

def add_new_attendee():
    conn = connect()
    cur = conn.cursor()

    # Inputs
    new_user_id_input = input("Insert new user ID: ")
    new_user_name = input("Insert new user Name: ")
    new_user_dob = input("Insert new user DOB (YYYY-MM-DD): ")
    new_user_gender = input("Insert new user Gender (Male/Female): ")
    new_user_company_input = input("Insert new user Company: ")

    # Validations
    try:
        new_user_id = int(new_user_id_input)
    except ValueError:
        print(f'*** ERROR *** (1366, "Incorrect integer value: \'{new_user_id_input}\' at row 1")')
        conn.close()
        return

    try:
        new_user_company = int(new_user_company_input)
    except ValueError:
        print(f'*** ERROR *** (1366, "Incorrect integer value: \'{new_user_company_input}\' at row 1")')
        conn.close()
        return

    # DOB validation
    try:
        datetime.strptime(new_user_dob, "%Y-%m-%d")
    except ValueError:
        print(f'*** ERROR *** (1292, "Incorrect date value: \'{new_user_dob}\' at row 1")')
        conn.close()
        return

    # Gender validation
    new_user_gender = new_user_gender.strip().capitalize()
    if new_user_gender not in ["Male", "Female"]:
        print("*** ERROR *** Gender must be Male/Female")
        conn.close()
        return

    # Company exists
    cur.execute("SELECT * FROM company WHERE companyID = %s", (new_user_company,))
    if not cur.fetchone():
        print(f"*** ERROR *** Company ID: {new_user_company} does not exist")
        conn.close()
        return

    # Attendee already exists
    cur.execute("SELECT * FROM attendee WHERE attendeeID = %s", (new_user_id,))
    if cur.fetchone():
        print(f"*** ERROR *** Attendee ID: {new_user_id} already exists")
        conn.close()
        return

    # Add
    cur.execute("""
        INSERT INTO attendee (attendeeID, attendeeName, attendeeDOB, attendeeGender, attendeeCompanyID)
        VALUES (%s, %s, %s, %s, %s)
    """, (new_user_id, new_user_name, new_user_dob, new_user_gender, new_user_company))
    
    conn.commit()
    conn.close()

    print("Attendee successfully added")
    return
    
    
def add_attendee_connection():
    print("Not implemented yet")


def view_rooms():
    print("Not implemented yet")