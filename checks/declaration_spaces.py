from checks._check import AbstractCheck


class DeclarationSpaces(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "Missing space after keyword"
        self.file_name = file_name
        self.header_lines = header_lines

    def get_check_id(self):
        return "L3"

    def get_check_level(self):
        return 1

    def check_line(self, line, line_number):
        return 'while(' in line or 'for(' in line or 'if(' in line or 'return(' in line or 'switch(' in line

    def check_function_calls(self, func):
        return 0

    def check_function_decl(self, visitor, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_visitor(self, visitor, lines):
        return 0

    def check_inner(self, file_content, file_contentf):
        return 0