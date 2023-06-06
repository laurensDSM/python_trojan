import datetime
class Default_module():
    def log(self,id):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print(timestamp)
        log_file = f"logs/{id}/log_{timestamp}.txt"
        with open(log_file, "a") as file:
            file.write(f"Hallo ik ben op {timestamp} besmet\n")