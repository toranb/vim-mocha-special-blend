import re


def sub_current_test_with_singleTest(module_line_num, current_buffer):
    return re.sub(r"it\(", r"it.only(", current_buffer[module_line_num])


def sub_singleTest_with_test(module_line_num, current_buffer):
    return re.sub(r"it.only\(", r"it(", current_buffer[module_line_num])


def sub_current_module_with_singleModule(module_line_num, current_buffer):
    return re.sub(r"describe\(", r"describe.only(", current_buffer[module_line_num])


def sub_singleModule_with_module(module_line_num, current_buffer):
    return re.sub(r"describe.only\(", r"describe(", current_buffer[module_line_num])


def get_line_num_of_current_module(current_line_index, current_buffer):
    module_regex = re.compile(r"^describe\(")
    for line_num in xrange(current_line_index - 1, -1, -1):
        if module_regex.search(current_buffer[line_num]) is not None:
            return line_num
    return False


def get_line_num_of_current_test(current_line_index, current_buffer):
    test_regex = re.compile(r"^it\(")
    for line_num in xrange(current_line_index - 1, -1, -1):
        if test_regex.search(current_buffer[line_num].lstrip()) is not None:
            return line_num
    return False
