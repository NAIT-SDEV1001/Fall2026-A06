class Clock:
    pass

    def __init__(self, digital: bool) -> None:
        self.digital = digital

    def __str__(self) -> str:
        return f"{"Digital" if self.digital else "Analog"}"
    
    def make_noise(self) -> None:
        if self.digital:
            print("Beep beep beep!")
        else:
            print("Bong bong bong!")

class AlarmClock(Clock):
    def __init__(self, digital: bool, twenty_four_hour: bool) -> None:
        super().__init__(digital)
        self.twenty_four_hour = twenty_four_hour

    def make_noise(self):
        super().make_noise()
        print("WAKE UP!")


class StopWatch(Clock):
    def start(self):
        self.started = True
        print("Started!")

    def stop(self):
        self.started = False
        print("Stopped!") 


all_clocks = []

digital_clock = Clock(True)
analog_clock = Clock(False)
alarm_clock_twenty_four_hour = AlarmClock(digital=False, twenty_four_hour=True)
stop_watch = StopWatch(True)

stop_watch.start()
stop_watch.stop()

all_clocks.append(digital_clock)
all_clocks.append(analog_clock)
all_clocks.append(alarm_clock_twenty_four_hour)
all_clocks.append(stop_watch)

for clock in all_clocks:
    print(clock)
    clock.make_noise()

    if isinstance(clock, StopWatch):
        clock.start()
