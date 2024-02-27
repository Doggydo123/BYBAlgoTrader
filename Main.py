# run.py
import Webserver.App as server
import AutomatedJobs.Jobs as jobs
import DB.DBAutomation as dbSetup

if __name__ == '__main__':
    dbSetup.setup()
    jobs.start_job_thread()  # Start the automated job using threading
    server.run()