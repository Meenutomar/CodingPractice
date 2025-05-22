def extract_time(datetime_str):
    """
    Extract time part from ISO datetime string (e.g. '2025-05-16T13:45:30')
    Returns time in HH:MM:SS format as string.
    """
    try:
        dt = datetime.fromisoformat(datetime_str)
        return dt.time().strftime("%H:%M:%S")
    except Exception:
        # If input is already time or invalid format, return as is
        return datetime_str

@app.post("/insert-chat-sessions")
def insert_chat_sessions():
    try:
        # Step 1: Load JSON file from public/data/robomh.json
        file_path = os.path.join("public", "data", "robomh.json")
        with open(file_path, "r") as f:
            data = json.load(f)

        mycursor = mydb.cursor()

        # Step 2: Prepare insert query
        sql = """
        INSERT INTO chat_session 
        (Id,created_at, session_id, user_email, conversation, started_at, ended_at)
        VALUES (%s,%s, %s, %s, %s, %s, %s)
        """

        # Step 3: Loop and insert each record with time extraction
        for row in data:
            created_at_time = extract_time(row.get("created_at", "00:00:00"))
            started_at_time = extract_time(row.get("started_at", "00:00:00"))
            ended_at_time = extract_time(row.get("ended_at", "00:00:00"))

            val = (
                created_at_time,
                row.get("session_id", ""),
                row.get("user_email", ""),
                json.dumps(row.get("conversation", {})),  # convert dict to JSON string
                started_at_time,
                ended_at_time
            )
            mycursor.execute(sql, val)

        mydb.commit()
        return {"message": f"{mycursor.rowcount} records inserted successfully"}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
