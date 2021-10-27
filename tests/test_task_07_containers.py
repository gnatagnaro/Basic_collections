import unittest
from unittest.mock import patch

from task_07_containers.main import main


class Test07Containers(unittest.TestCase):
    @patch('task_07_containers.main.print')
    @patch('task_07_containers.main.input')
    def test_main(self, mock_input, mock_print):
        """
        Проверяем обычный кейс. При вводе "8", "165", "163", "160", "160", "157", "157", "155", "154", "162"\
        должны получить "Номер, куда встанет новый контейнер: 3"
        """
        containers_cont = "8"
        weights_list = ["165", "163", "160", "160", "157", "157", "155", "154"]
        new_weight = "162"
        mock_input.side_effect = [containers_cont] + weights_list + [new_weight]
        main()
        print_result = mock_print.call_args_list

        if not print_result:
            self.fail("Вы ничего не выводите")

        self.assertEqual(
            ' '.join([str(j) for j in print_result[0].args]).lstrip(),
            'Номер, куда встанет новый контейнер: 3',
        )


if __name__ == '__main__':
    unittest.main()
