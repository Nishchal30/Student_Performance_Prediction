import sys

class CustomException(Exception):

    def __init__(self, error_msg, error_details):

        self.error_msg = error_msg
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in python script name [{0}] and line no [{1}] error message [{2}]".format(
            self.filename, self.lineno, str(self.error_msg)
        )
