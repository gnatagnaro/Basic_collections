import unittest
from unittest.mock import patch

from task_08_running_nums.main import main


class Test08RunningNums(unittest.TestCase):
    @patch('task_08_running_nums.main.print')
    @patch('task_08_running_nums.main.input')
    def test_main_1_step(self, mock_input, mock_print):
        """
        Проверяем обычный кейс. При вводе "1", [1, 2, 3, 4, 5] должны получить  "Сдвинутый список: [5, 1, 2, 3, 4]"
        """
        step = "1"
        list_str = "[1, 2, 3, 4, 5]"
        mock_input.side_effect = [step, list_str]
        main()
        print_result = mock_print.call_args_list

        if not print_result:
            self.fail("Вы ничего не выводите")

        self.assertEqual(
            ' '.join([str(j) for j in print_result[0].args]).lstrip(),
            'Сдвинутый список: [5, 1, 2, 3, 4]',
        )

    @patch('task_08_running_nums.main.print')
    @patch('task_08_running_nums.main.input')
    def test_main_3_step(self, mock_input, mock_print):
        """
        Проверяем обычный кейс. При вводе "3", [1, 4, -3, 0, 10] должны получить "Сдвинутый список: [-3, 0, 10, 1, 4]"
        """
        step = "3"
        list_str = "[1, 4, -3, 0, 10]"
        mock_input.side_effect = [step, list_str]
        main()
        print_result = mock_print.call_args_list

        if not print_result:
            self.fail("Вы ничего не выводите")

        self.assertEqual(
            ' '.join([str(j) for j in print_result[0].args]).lstrip(),
            'Сдвинутый список: [-3, 0, 10, 1, 4]',
        )


if __name__ == '__main__':
    unittest.main()
