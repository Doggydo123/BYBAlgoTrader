# run.py
import Webserver.App as server
import AutomatedJobs.Jobs as jobs

if __name__ == '__main__':
    jobs.start_job_thread()  # Start the automated job using threading
    server.run()