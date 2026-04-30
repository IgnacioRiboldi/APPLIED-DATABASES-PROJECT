import pymysql
import datetime
from neo4j import GraphDatabase


# MYSQL CONNECTION

def connect():
    return pymysql.connect(
        host="localhost",
        user="root",
        auth=("neo4j", "neo4j")
    )


# NEO4J CONNECTION

def connect_neo4j():
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "neo4j"

    return GraphDatabase.driver(uri, auth=(user, password))


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
        for row in rows:
            print(row)
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
        INSERT INTO attendee (attendeeID, attendeeName, attendeeDOB, attendeeGender, attendeeCompanyID)
        VALUES (%s, %s, %s, %s, %s)
    """, (new_user_id, new_user_name, new_user_dob, new_user_gender, new_user_company))

    conn.commit()
    conn.close()

    print("Attendee added")

def view_connected_attendees():
    attendee = input("Enter Attendee ID: ")

    try:
        attendee_id = int(attendee)
    except ValueError:
        print("*** ERROR *** Invalid attendee ID")
        return

    driver = connect_neo4j()

    with driver.session(database="appdbprojNeo4j") as session:

        # Get attendee name
        result = session.run(
            "MATCH (a:Attendee {AttendeeID: $id}) RETURN a.AttendeeID AS id",
            id=attendee_id
        )

        record = result.single()

        if not record:
            print("*** ERROR *** Attendee does not exist")
            driver.close()
            return

        # Get name separately
        name_result = session.run(
            "MATCH (a:Attendee {AttendeeID: $id}) RETURN a.AttendeeID AS id",
            id=attendee_id
        )

        print(f'Attendee ID: {attendee_id}')
        print("------------------------------")

        # Get connections
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
                print(f"-> Attendee {r['id']}")

    driver.close()


# PENDING
def add_attendee_connection():
    print("Not implemented yet")


def view_rooms():
    print("Not implemented yet")