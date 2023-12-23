"""
На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.

Напишите класс LotteryGame, который будет иметь метод compare_lists, который будет сравнивать числа из вашего билета из
list1 со списком выпавших чисел list2

Если совпадающих чисел нет, то выведите на экран:
Совпадающих чисел нет.
"""

import logging

logging.basicConfig(filename='lottery.log',
                    encoding='utf-8',
                    format='{levelname:<6} - {asctime} - "{funcName}()" - {msg}',
                    style='{',
                    level=logging.INFO
                    )
logger = logging.getLogger(__name__)


class LotteryGame:

    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        result_list = []
        for i in self.list1:
            for j in self.list2:
                if i == j:
                    result_list.append(i)
                    break
        if len(result_list) > 0:
            print(f'Совпадающие числа: {result_list} - Кол-во совпадений: {len(result_list)}')
            logger.info(f'Совпадающие числа: {result_list} - Кол-во совпадений: {len(result_list)}')

        else:
            logger.info(f'Совпадающих чисел нет.')
            print('Совпадающих чисел нет.')


if __name__ == "__main__":
    # users_numbers = [2, 54, 64, 7, 15]
    # draws_numbers = [14, 22, 17, 41, 8, 3, 18]
    users_numbers = [22, 17, 64, 8, 15]
    draws_numbers = [14, 22, 17, 41, 8, 3, 18]
    game = LotteryGame(users_numbers, draws_numbers)
    game.compare_lists()
