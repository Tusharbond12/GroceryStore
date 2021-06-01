from datetime import datetime
from ecommerce.config.config import ConfigReader
import os

class AppLogger(ConfigReader):
    def __init__(self):
        """
        Description: This method is adding default app logs which is defined in config.ini or
        can be changed from child class by updating self.logPath value
        """

        super(AppLogger, self).__init__()
        self.logPath = self.config['DEFAULT']['LOG_DIR']

    def log(self, log_message: str, log_path: str = ''):
        """
        Description: This method writes application logs
        :param log_message: log message
        :param log_path: path where the log file is present
        :return: Null
        """

        now = datetime.now()
        date = now.date()
        current_time = now.strftime("%H:%M:%S")
        if not log_path:
            log_path = f"{self.logPath}/log_{date}.txt"

        if not os.path.exists(log_path):
            self.create_log_path(log_path)

        file_object = open(log_path, 'a+')
        file_object.write(str(date) + "/" + str(current_time) + "\t\t" + log_message +"\n")

    def create_log_path(self, path):
        path_arr = path.split('/')
        if len(path_arr) > 1:
            init_path = ''
            for dir in path_arr[:-1]:
                init_path += dir+'/'
                if not os.path.exists(init_path):
                    os.mkdir(init_path)