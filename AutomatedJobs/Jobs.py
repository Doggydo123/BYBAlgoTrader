# jobs/tasks.py
import threading
import time
from Models.Profile import Profile
from Services.ProfileService import insertProfile, getProfileById

def job():
    while True:
        print("Automated Job is running...")
        time.sleep(5)  # Example: sleep for 5 seconds

def testDBJob():
    print("Test Profile insert")
    time.sleep(5)  # Example: sleep for 5 seconds
    profile = Profile(name="John", lastname="Doe", email="john.doe@example.com", username="johndoe", address="123 Main St", accountCreationDate="2022-01-01", accountType="Standard")
    id = insertProfile(profile)
    print("new profile ID",id)
    profile = getProfileById(id)
    print(profile)


def start_job_thread():
    #testDBJob()
    thread = threading.Thread(target=job)
    thread.daemon = True  # Daemonize the thread so it stops with the main process
    thread.start()
