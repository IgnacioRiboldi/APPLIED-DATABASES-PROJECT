import pymysql

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



def add_new_attendee():
    print("Not implemented yet")


def add_attendee_connection():
    print("Not implemented yet")


def view_rooms():
    print("Not implemented yet")