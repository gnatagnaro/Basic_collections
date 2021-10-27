import unittest
from unittest.mock import patch

from task_03_cells.main import main


class Test03Cells(unittest.TestCase):
    @patch('task_03_cells.main.print')
    @patch('task_03_cells.main.input')
    def test_main(self, mock_input, mock_print):
        """
        Проверяем обычный кейс. При вводе 5, 3, 0, 6, 2, 10  должны получить "Неподходящие значения: 0 2"
        """
        cells_num = 5
        effic_list = [3, 0, 6, 2, 10]
        mock_input.side_effect = [cells_num] + effic_list
        main()
        print_result = mock_print.call_args_list

        if not print_result:
            self.fail("Вы ничего не выводите")

        for i in range(cells_num):
            self.assertEqual(' '.join([str(j) for j in print_result[i].args]), f'Эффективность {str(i + 1)} клетки:')

        self.assertEqual(' '.join([str(j) for j in print_result[-1].args]), 'Неподходящие значения: 0 2')


if __name__ == '__main__':
    unittest.main()
