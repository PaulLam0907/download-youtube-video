from proglog import ProgressBarLogger

# https://stackoverflow.com/questions/69423410/moviepy-getting-progress-bar-values
# https://stackoverflow.com/questions/7039114/waiting-animation-in-command-prompt-python


class Logger(ProgressBarLogger):
    """
    Logger class for moviepy
    """
    
    def callback(self, **kwargs):
        """
        This function is called every time when the logger message is updated
        
        :param kwargs: dictionary of {key: value}
        :return:
        """
        # for key, value in kwargs.items():
        #     print(f"Parameter {key} is now {value}", end = "\r")
        pass
    
    def bars_callback(self, bar, attr, value, old_value = None):
        """
        This function is called every time when the logger progress is updated
        
        :param bar:
        :param attr:
        :param value:
        :param old_value:
        :return:
        """
        
        old_percentage = (old_value / self.bars[bar]["total"]) * 100 if old_value else None
        percentage = (value / self.bars[bar]["total"]) * 100
        
        progress_bar = "=" * int(percentage/5)
        # print(f"{bar} {attr} {percentage}")
        
        if old_percentage:
            
            if int(percentage) > int(old_percentage):
                print(f"{bar:<7} : [{progress_bar:<20}] {int(percentage)}% ", end = "\r")
        