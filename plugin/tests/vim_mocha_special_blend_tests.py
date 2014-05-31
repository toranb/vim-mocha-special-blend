import unittest
import vim_mocha_special_blend as sut


class VimMochaSpecialBlendTests(unittest.TestCase):

    def test_sub_current_test_with_singleTest_returns_the_proper_string(self):
        current_buffer = self.build_buffer_helper()
        line_num = sut.get_line_num_of_current_test(3, current_buffer)
        returned_string = sut.sub_current_test_with_singleTest(line_num, current_buffer)
        self.assertEqual('it.only("test example 1", function() {\n', returned_string)

    def test_sub_singleTest_with_test_returns_the_proper_string(self):
        current_buffer = self.build_buffer_helper()
        line_num = sut.get_line_num_of_current_test(3, current_buffer)
        current_buffer[line_num] = sut.sub_current_test_with_singleTest(line_num, current_buffer)
        self.assertEqual('it.only("test example 1", function() {\n', current_buffer[line_num])
        returned_string = sut.sub_singleTest_with_test(line_num, current_buffer)
        self.assertEqual('it("test example 1", function() {\n', returned_string)

    def test_sub_current_module_with_singleModule_returns_the_proper_string(self):
        current_buffer = self.build_buffer_helper()
        line_num = sut.get_line_num_of_current_module(7, current_buffer)
        returned_string = sut.sub_current_module_with_singleModule(line_num, current_buffer)
        self.assertEqual('describe.only("first suite of tests", function() {\n', returned_string)

    def test_sub_singleModule_with_module_returns_the_proper_string(self):
        current_buffer = self.build_buffer_helper()
        line_num = sut.get_line_num_of_current_module(7, current_buffer)
        current_buffer[line_num] = sut.sub_current_module_with_singleModule(line_num, current_buffer)
        self.assertEqual('describe.only("first suite of tests", function() {\n', current_buffer[line_num])
        returned_string = sut.sub_singleModule_with_module(line_num, current_buffer)
        self.assertEqual('describe("first suite of tests", function() {\n', returned_string)

    def build_buffer_helper(self):
        with open("dummy_test_file.js", "r") as f:
            current_buffer = []
            for line in f.readlines():
                current_buffer.append(line)
        return current_buffer
