import unittest
from unittest.mock import patch

from task_06_word_analysis.main import main


class Test06WordAnalysis(unittest.TestCase):
    @patch('task_06_word_analysis.main.print')
    @patch('task_06_word_analysis.main.input')
    def test_main_privet(self, mock_input, mock_print):
        """
        Проверяем обычный кейс. При вводе "привет"  должны получить "Кол-во уникальных букв: 6"
        """
        mock_input.return_value = "привет"
        main()
        print_result = mock_print.call_args_list

        if not print_result:
            self.fail("Вы ничего не выводите")

        self.assertEqual(
            ' '.join([str(j) for j in print_result[0].args]).lstrip(),
            'Кол-во уникальных букв: 6',
        )

    @patch('task_06_word_analysis.main.print')
    @patch('task_06_word_analysis.main.input')
    def test_main_lava(self, mock_input, mock_print):
        """
        Проверяем обычный кейс. При вводе "лава"  должны получить "Кол-во уникальных букв: 2"
        """
        mock_input.return_value = "лава"
        main()
        print_result = mock_print.call_args_list

        if not print_result:
            self.fail("Вы ничего не выводите")

        self.assertEqual(
            ' '.join([str(j) for j in print_result[0].args]).lstrip(),
            'Кол-во уникальных букв: 2',
        )


if __name__ == '__main__':
    unittest.main()
