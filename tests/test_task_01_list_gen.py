import unittest
from unittest.mock import patch

from task_01_list_gen.main import main


class Test01ListGen(unittest.TestCase):
    @patch('task_01_list_gen.main.print')
    @patch('task_01_list_gen.main.input')
    def test_boundary_conditions(self, mock_input, mock_print):
        """
        Проверяем граничные условия. При вводе 1 должна получиться последовательность [1]
        """
        mock_input.return_value = "1"
        main()
        print_result = mock_print.call_args_list

        if not print_result:
            self.fail("Вы ничего не выводите")

        self.assertEqual(
            ' '.join([str(j) for j in print_result[0].args]),
            'Список из нечётных чисел от 1 до N: [1]',
        )

    @patch('task_01_list_gen.main.print')
    @patch('task_01_list_gen.main.input')
    def test_main(self, mock_input, mock_print):
        """
        Проверяем обычный кейс. При вводе 14 должна получиться последовательность [1, 3, 5, 7, 9, 11, 13]
        """
        mock_input.return_value = "14"
        main()
        print_result = mock_print.call_args_list

        if not print_result:
            self.fail("Вы ничего не выводите")

        self.assertEqual(
            ' '.join([str(j) for j in print_result[0].args]),
            'Список из нечётных чисел от 1 до N: [1, 3, 5, 7, 9, 11, 13]',
        )


if __name__ == '__main__':
    unittest.main()
