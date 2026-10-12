import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()  #sys.exc_info()

    file_name = "<unknown_file>"
    line_no = "<unknown_line>"

    if exc_tb is not None:
        file_name=exc_tb.tb_frame.f_code.co_filename
        line_no = exc_tb.tb_lineno

    error_message="Error occured python script name[{0}] line number[{1}] error message [{2}]".format(file_name,line_no,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
       super().__init__(error_message) # Pass the string message here
       self.error_message=error_message_detail(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message