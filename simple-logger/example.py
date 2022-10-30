import logger

@logger.LoggerApplication
class Application:
    def __init__(self, *args, logger: logger.Logger): # when we use @logger.LoggerApplication it passes the logger for us :)
        self.logger = logger
        self.args = args

    def print_args(self):
        self.logger.debug("Debugging is enabled!")
        self.logger.info("Printing some args")
        self.logger.info("".join(str(e) + " " for e in self.args))

    def crash(self, code):
        self.logger.warn("About to crash!")
        self.logger.error("Can't handle that!")
        self.logger.critical("Process exited with code " + str(code))

# debug mode is disabled by default so we enable it
logger.set_level(logger.LogLevels.DEBUG)

app = Application(1,2,3)
app.print_args()
app.crash(1024)