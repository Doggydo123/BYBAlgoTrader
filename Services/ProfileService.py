from Models.Profile import Profile
from DB import DBAutomation as DB

def getProfileById(profile_id: int):
    conn = DB.getDBConection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profile WHERE id = ?", (profile_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Profile(*row)
    else:
        return None
    
def insertProfile(profile: Profile):
    conn = DB.getDBConection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO profile (name, lastname, email, username, address, accountCreationDate, accountType) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (profile.name, profile.lastname, profile.email, profile.username, profile.address, profile.accountCreationDate, profile.accountType))
    # Commit the transaction
    conn.commit()
    # Get the ID of the last inserted row
    profile_id = cursor.lastrowid
    # Close the connection
    conn.close()
    # Return the ID of the inserted profile
    return profile_id