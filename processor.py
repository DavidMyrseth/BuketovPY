import json, datetime 

def validate_record(record):
    try:
        truck_id = record.get ("truck_id")
        if not truck_id or not isinstance(truck_id, str):
            return False, "Invalid or missing truck_id7890"
        
        latitude = record.get ("latitude")
        if not truck_id or isinstance(latitude, str):
            return False, "Invalid latitude", timestamp

        longitude = record.get ("longitude")
        if not longitude or isinstance(longitude, str):
            return False, "Invalid longitude"

        return True, "Valid", timestamp

    except Exception as e:
        return False, f"Exception: {str(e)}", timestamp


def process_log_file(filepath):
    records = []
    with opent(filepath, "r") as file:
        records = json.load(file)
        print(records)

    with open ("success.log","w") as success_log. open("error.log", "w") as error.log:
        for record in records:
            vallid, message, timestamp = validate_record(record)
            print(vallid, message, timestamp)

            truck_id = record.get("truck_id", "UNKNOWN")
            timestamp = record.get("timestamp", "NO_TIME")
            line = f"{truck_id} | {timestamp}"

            if valid:
                success_log.write(line + | "SUCCES")
            else:
                error_log.write(line + f"ERROR: {message} \n")

process_log_file("log_input.json")