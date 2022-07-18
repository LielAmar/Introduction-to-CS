from constants import *
from label import Label


class Timer(Label):
    """
    A Timer object to count-up time
    """

    def __init__(self, root, duration=TIMER_DURATION, prefix="Timer: "):
        if not isinstance(duration, int):
            raise TypeError("${duration} must be an integer")
        if not isinstance(prefix, str):
            raise TypeError("${prefix} must be a string")

        self.__current_time = duration
        self.__start_time = duration
        
        super().__init__(root, prefix)
        super().set_properties({ PROP_TEXT: self.__get_time() })


    def __get_time(self) -> str:
        minutes_raw = self.__current_time // 60
        seconds_raw = self.__current_time % 60

        minutes = str(minutes_raw)
        seconds = str(seconds_raw)

        if minutes_raw < 10:
            minutes = "0" + minutes
        if seconds_raw < 10:
            seconds = "0" + seconds

        return minutes + ":" + seconds
        

    def tick(self):
        """
        Ticks the Timer by one second and updates the tkinter object's text

        Returns true if we've reached 0
        """

        self.__current_time -= 1
        super().set_properties({ PROP_TEXT: self.__get_time() })

        if self.__current_time == 0:
            return True

        return False

    def reset(self):
        """
        Resets the Timer to 0 seconds
        """

        self.__current_time = self.__start_time
        super().set_properties({ PROP_TEXT: self.__get_time() })