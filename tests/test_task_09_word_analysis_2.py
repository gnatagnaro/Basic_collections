import unittest
from unittest.mock import patch

from task_09_word_analysis_2.main import main


class Test09WordAnalysis2(unittest.TestCase):
    @patch('task_09_word_analysis_2.main.print')
    @patch('task_09_word_analysis_2.main.input')
    def test_main_madam(self, mock_input, mock_print):
        """
        Проверяем обычный кейс. При вводе "мадам" должны получить "Слово является палиндромом"
        """
        mock_input.return_value = "мадам"
        main()
        print_result = mock_print.call_args_list

        if not print_result:
            self.fail("Вы ничего не выводите")

        self.assertEqual(
            ' '.join([str(j) for j in print_result[0].args]).lstrip(),
            'Слово является палиндромом',
        )

    @patch('task_09_word_analysis_2.main.print')
    @patch('task_09_word_analysis_2.main.input')
    def test_main_abccba(self, mock_input, mock_print):
        """
        Проверяем обычный кейс. При вводе "abccba" должны получить "Слово является палиндромом"
        """
        mock_input.return_value = "abccba"
        main()
        print_result = mock_print.call_args_list

        if not print_result:
            self.fail("Вы ничего не выводите")

        self.assertEqual(
            ' '.join([str(j) for j in print_result[0].args]).lstrip(),
            'Слово является палиндромом',
        )

    @patch('task_09_word_analysis_2.main.print')
    @patch('task_09_word_analysis_2.main.input')
    def test_main_abbd(self, mock_input, mock_print):
        """
        Проверяем обычный кейс. При вводе "abbd" должны получить "Слово является палиндромом"
        """
        mock_input.return_value = "abbd"
        main()
        print_result = mock_print.call_args_list

        if not print_result:
            self.fail("Вы ничего не выводите")

        self.assertEqual(
            ' '.join([str(j) for j in print_result[0].args]).lstrip(),
            'Слово не является палиндромом',
        )


if __name__ == '__main__':
    unittest.main()
