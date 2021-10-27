import unittest
from unittest.mock import patch

from task_10_sort.main import main


class Test10Sort(unittest.TestCase):
    @patch('task_10_sort.main.print')
    @patch('task_10_sort.main.input')
    def test_main(self, mock_input, mock_print):
        """
        Проверяем обычный кейс. При вводе "[1, 4, -3, 0, 10]" должны получить "Отсортированный список: [-3, 0, 1, 4, 10]"
        """
        mock_input.return_value = "[1, 4, -3, 0, 10]"
        main()
        print_result = mock_print.call_args_list

        if not print_result:
            self.fail("Вы ничего не выводите")

        self.assertEqual(
            ' '.join([str(j) for j in print_result[0].args]).lstrip(),
            'Отсортированный список: [-3, 0, 1, 4, 10]',
        )


if __name__ == '__main__':
    unittest.main()
