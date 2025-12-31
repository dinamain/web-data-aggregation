import time
from main import main

# Run every 24 hours (in seconds)
INTERVAL = 24 * 60 * 60  
# INTERVAL = 3 * 60
if __name__ == "__main__":
    print("Scheduler started. Running pipeline periodically...")

    while True:
        try:
            print("Running data pipeline...")
            main()
            print("Pipeline run completed.")
        except Exception as e:
            print(f"Pipeline failed: {e}")

        print(f"Sleeping for {INTERVAL} seconds...")
        time.sleep(INTERVAL)
