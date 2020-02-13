from piyush_utils.base_test_case import BaseTestCase
from piyush_utils.basic_funcs import BasicFuncs


class AdventOfCode(object):
    @staticmethod
    def problem_1_2017(inp: str):
        l = len(inp)
        total = 0
        for i in range(l-1):
            if inp[i] == inp[i + 1]:
                total += int(inp[i])
        if inp[-1] == inp[0]:
            total += int(inp[0])
        return total

    @staticmethod
    def problem2(inp: str):
        check_sum = 0
        for line in inp.splitlines():
            array = line.split(' ')
            while '' in array:
                array.remove('')
            num_array = [int(el) for el in array]
            small = min(num_array)
            large = max(num_array)
            check_sum += large - small
        return check_sum


class AdventOfCodeTest(BaseTestCase):
    def test_problem_1_2017(self):
        self.assertEqual(AdventOfCode.problem_1_2017('1122'), 3)
        self.assertEqual(AdventOfCode.problem_1_2017('1111'), 4)
        self.assertEqual(AdventOfCode.problem_1_2017('1234'), 0)
        self.assertEqual(AdventOfCode.problem_1_2017('91212129'), 9)
        problem_input = BasicFuncs.load_file_as_string('problem_1_2017.txt').rstrip()
        print((AdventOfCode.problem_1_2017(problem_input)))

    def test_problem2(self):
        s = '5 1 9 5\n7 5 3\n2 4 6 8'
        self.assertEqual(AdventOfCode.problem2(s), 18)
        problem_input = BasicFuncs.load_file_as_string('problem2.txt')
        print(AdventOfCode.problem2(problem_input))
