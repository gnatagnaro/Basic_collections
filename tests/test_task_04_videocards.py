import unittest
from unittest.mock import patch

from task_04_videocards.main import main


class Test04Videocards(unittest.TestCase):
    @patch('task_04_videocards.main.print')
    @patch('task_04_videocards.main.input')
    def test_main(self, mock_input, mock_print):
        """
        Проверяем обычный кейс. При вводе "5", "3070", "2060", "3090", "3070", "3090"  должны получить "Неподходящие значения: 0 2"
        """
        videocards_count = "5"
        videocards_list = ["3070", "2060", "3090", "3070", "3090"]
        mock_input.side_effect = [videocards_count] + videocards_list
        main()
        print_result = mock_print.call_args_list

        if not print_result:
            self.fail("Вы ничего не выводите")

        for i in range(int(videocards_count)):
            self.assertEqual(' '.join([str(j) for j in print_result[i].args]).lstrip(), f'{i+1} Видеокарта:')

        self.assertEqual(
            ' '.join([str(j) for j in print_result[-2].args]),
            'Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]',
        )
        self.assertEqual(
            ' '.join([str(j) for j in print_result[-1].args]),
            'Новый список видеокарт: [ 3070 2060 3070 ]',
        )


if __name__ == '__main__':
    unittest.main()
