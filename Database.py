import pymysql
import datetime
from neo4j import GraphDatabase

# MYSQL CONNECTION

def connect():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        db="appdbproj"
    )


# NEO4J CONNECTION

def connect_neo4j():
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "neo4jneo4j"

    return GraphDatabase.driver(uri, auth=(user, password))


# MYSQL FUNCTIONS

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
            print("*** ERROR *** Invalid Company ID")

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
        INNER JOIN registration r ON a.attendeeID = r.attendeeID
        INNER JOIN session s ON r.sessionID = s.sessionID
        INNER JOIN room ro ON s.roomID = ro.roomID
        WHERE a.attendeeCompanyID = %s
    """

    cur.execute(query, (company_id,))
    rows = cur.fetchall()

    if rows:
        print(f"\n{company_name} Attendees:\n")

        for row in rows:
            attendee_name = row[0]
            attendee_dob = row[1].strftime("%Y-%m-%d")
            session_title = row[2]
            speaker_name = row[3]
            session_date = row[4].strftime("%Y-%m-%d")
            room_name = row[5]

            print(
                f"Attendee: {attendee_name} | DOB: {attendee_dob} | "
                f"Session: {session_title} | Speaker: {speaker_name} | "
                f"Date: {session_date} | Room: {room_name}"
            )

    else:
        print(f"No attendees found for {company_name}")

    conn.close()


def add_new_attendee():
    conn = connect()
    cur = conn.cursor()

    new_user_id = int(input("Insert new user ID: "))
    new_user_name = input("Insert new user Name: ")
    new_user_dob = input("Insert DOB (YYYY-MM-DD): ")
    new_user_gender = input("Insert Gender (Male/Female): ")
    new_user_company = int(input("Insert Company ID: "))

    try:
        datetime.datetime.strptime(new_user_dob, "%Y-%m-%d")
    except ValueError:
        print("Invalid date")
        return

    cur.execute("""
        INSERT INTO attendee 
        (attendeeID, attendeeName, attendeeDOB, attendeeGender, attendeeCompanyID)
        VALUES (%s, %s, %s, %s, %s)
    """, (new_user_id, new_user_name, new_user_dob, new_user_gender, new_user_company))

    conn.commit()
    conn.close()

    print("Attendee added")
    
# NEO4J FUNCTIONS

def view_connected_attendees():

    while True:
        user_input = input("Enter Attendee ID: ")
        try:
            attendee_id = int(user_input)
            break
        except ValueError:
            print("*** ERROR *** Invalid attendee ID")
            return

    # Get name from MYSQL
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT attendeeName FROM attendee WHERE attendeeID = %s",
        (attendee_id,)
    )

    result = cur.fetchone()
    conn.close()

    if not result:
        print("*** ERROR *** Attendee does not exist (MySQL)")
        return

    attendee_name = result[0]

    # NEO4J
    driver = connect_neo4j()

    with driver.session(database="appdbprojNeo4j") as session:

        result = session.run("""
            MATCH (a:Attendee {AttendeeID: $id})
            RETURN a.AttendeeID AS id
        """, id=attendee_id)

        record = result.single()

        if not record:
            print("No connections")
            driver.close()
            return

        print(f"\nAttendee ID: {attendee_id}")
        print(f"Attendee Name: {attendee_name}")
        print("------------------------------")

        query = """
        MATCH (a:Attendee {AttendeeID: $id})-[:CONNECTED_TO]-(b:Attendee)
        RETURN b.AttendeeID AS id
        """

        results = session.run(query, id=attendee_id)

        connections = list(results)

        if not connections:
            print("No connections")
        else:
            for r in connections:
                # también traemos nombres desde MySQL
                conn = connect()
                cur = conn.cursor()
                cur.execute(
                    "SELECT attendeeName FROM attendee WHERE attendeeID = %s",
                    (r["id"],)
                )
                name_result = cur.fetchone()
                conn.close()

                name = name_result[0] if name_result else "Unknown"

                print(f"{r['id']} | {name}")

    driver.close()


# Peding

def add_attendee_connection():
    print("Not implemented yet")


def view_rooms():
    print("Not implemented yet")