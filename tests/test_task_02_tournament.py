import unittest
from unittest.mock import patch

from task_02_tournament.main import main


class Test02Tournament(unittest.TestCase):
    @patch('task_02_tournament.main.print')
    def test_main(self, mock_print):
        """
        Проверяем обычный кейс. Выводим элементы списка только с чётными индексами.
        """
        main()
        print_result = mock_print.call_args_list

        if not print_result:
            self.fail("Вы ничего не выводите")

        self.assertEqual(
            ' '.join([str(j) for j in print_result[-1].args]),
            "Первый день: ['Артемий', 'Влад', 'Дима', 'Женя']",
        )


if __name__ == '__main__':
    unittest.main()
