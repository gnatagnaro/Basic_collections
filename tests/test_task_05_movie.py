import unittest
from unittest.mock import patch

from task_05_movie.main import main


class Test05Movie(unittest.TestCase):
    @patch('task_05_movie.main.print')
    @patch('task_05_movie.main.input')
    def test_main(self, mock_input, mock_print):
        """
        Проверяем обычный кейс. При вводе "5", "3070", "2060", "3090", "3070", "3090"  должны получить "Неподходящие значения: 0 2"
        """
        videocards_count = "3"
        videocards_list = ["Леон", "Безумный Макс", "Мементо"]
        mock_input.side_effect = [videocards_count] + videocards_list
        main()
        print_result = mock_print.call_args_list

        if not print_result:
            self.fail("Вы ничего не выводите")

        self.assertEqual(
            ' '.join([str(j) for j in print_result[0].args]).lstrip(),
            'Ошибка: фильма Безумный Макс у нас нет :(',
        )
        self.assertEqual(
            ' '.join([str(j) for j in print_result[1].args]).lstrip(),
            'Ваш список любимых фильмов: Леон, Мементо'
        )


if __name__ == '__main__':
    unittest.main()
