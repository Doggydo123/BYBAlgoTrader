# jobs/tasks.py
import threading
import time



def job():
    while True:
        print("Automated Job is running...")
        time.sleep(5)  # Example: sleep for 5 seconds

def start_job_thread():
    #testDBProfileJob()
    #testDBStocksJob()
    #testDBStocksOwnedJob()
    thread = threading.Thread(target=job)
    thread.daemon = True  # Daemonize the thread so it stops with the main process
    thread.start()
