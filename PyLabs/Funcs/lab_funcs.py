from statistics import *
import random as rnd
import os

class cl_Ex_1:
    
    def do_show_output(self) -> None:
        input_num : list = []
        
        print("\n\n\tЗадание 1 \t Лаб. Функции\n\n")
        
        i : int = 0
        while i < 2:
            input_num.append(int(input(f"\nВведите {i+1} число: ")))
            i += 1
            pass
        print(f"\nВведенные числа:\t{input_num[0]} и {input_num[1]}\tдлина: {len(input_num)}")
        print(f"\nВывод:\t{self.do_compute_arg(input_num[0], input_num[1])}")
        pass
    
    def do_compute_arg(self, i_num : int, j_num : int) -> int:
        if i_num > 0 and j_num > 0: return (i_num + j_num)
        elif i_num < 0 and j_num < 0: return (min(i_num, j_num) - max(i_num, j_num))
        else: return 0
    pass

class cl_Ex_2:
    def do_get_nums(self) -> list:
        output : list = []
        
        print("\n\n\tЗадание 2 \t Лаб. Функции\n\n")
        i : int = 1
        while len(output) != 3:
            output.append(int(input(f"\nВведите {i} число:\t")))
            i += 1
            pass
        
        return output
    
    def do_find_max_nums(self) -> None:
        nums : list = self.do_get_nums()
        max_nums : list = []
        
        print(f"\nВведенные числа:\t{nums}")
        while len(nums) > 1:
            ind : int = nums.index(max(nums))
            max_nums.append(nums.pop(ind))
            pass
        
        print(f"\nДва максимальных числа:\t{max_nums}")
    pass

class cl_Ex_3:
    def __init__(self, use_string : bool = True, keys : list = ['t', 'f']) -> None:
        self.keys : list = keys
        self.use_string : bool = use_string
        pass
    
    def do_compute_nums_list(self) -> None:
        nums : list = []
        output : list = []
        print("\n\n\tЗадание 3 \t Лаб. Функции\n\n")
        if self.use_string: nums = self.do_convert_from_string(input(f"\nВведите числа через пробел:\n"))
        else: nums = self.do_get_nums()
        
        print(f"\nВведенные числа:\t{nums}")
        
        str_key = input(f"\nВведите ключ {self.keys[0]} или {self.keys[1]}:\t")
        key : bool
        
        if str_key == self.keys[0]: key = True
        else: key = False
        
        output = self.do_get_new_list(nums, key)
        
        print(f"\nНовый лист чисел:\t{output}")
        pass
    
    
    def do_get_new_list(self, nums : list, key : bool) -> list:
        output : list = []
        
        for num in nums:
            match key:
                case True:
                    if num % 2 == 0: output.append(num)
                    pass
                case False:
                    if num % 2 != 0: output.append(num)
                    pass
            pass
        return output
    
    def do_convert_from_string(self, string : str) -> list:
        num_list : list = []
        
        buffer : str = ""
        i : int = 0
        while i < len(string):
            char : chr = string[i]
            
            if char != ' ' and char != "\n" and (char != self.keys[0] or char != self.keys[1]): buffer += char
            else:
                num_list.append(int(buffer))
                buffer = ""
                pass
            i += 1
            pass
        return num_list
    
    def do_get_nums(self) -> list:
        num_list : list = []
        
        while True:
            string : str = input(f"\nВведите число или оставте строку пустой, если хотите завершить ввод:\t")
            if string == "" or string == "\n" or string == " ": break
            else:
                num_list.append(int(string))
                pass
            pass
        
        return num_list
    pass

class cl_Ex_4:
    def __init__(self) -> None:
        self.i_file_data : str = ""
        pass
    
    def i_do_find_min_max(self, *nums) -> list:
        output : list = []
        
        output.append(min(*nums))
        output.append(max(*nums))
        return output
    
    def i_compute_nums(self) -> None:
        self._check_file()
        nums : list = self.i_do_get_nums()
        min_max : list = []
        
        print(f"\nВведенные данные:\n{nums}")
        min_max = self.i_do_find_min_max(*nums)
        
        print(f"\nМинимальное и макссимальное число из введенных данных:\t{min_max}")
        pass
    
    def i_do_get_nums(self) -> list:
        output : list = []
        
        if self.i_file_data == "": exit()
        print("\n\n\tЗадание 4 \t Лаб. Функции\n\n")
        
        buffer : str = ""
        for char in self.i_file_data:
            if char != " ": buffer += char
            else:
                output.append(int(buffer))
                buffer = ""
                pass
            
            if self.i_file_data.index(char) == len(self.i_file_data) - 1:
                output.append(int(buffer))
                buffer = ""
                pass 
            pass
        output.append(int(buffer))
        buffer = ""
        
        return output
    
    def _check_file(self) -> None:
        if not os.path.exists("Funcs/input_ex4.txt"):
        #   Создание файла при его отсутствие
            with open("Funcs/input_ex4.txt", "w") as file:
                print("\tFile is not exist so it was created\n\tPlease enter data in that file to work code\n")
                exit()

        #   Проверка на наличие данных в файле
        if os.stat("Funcs/input_ex4.txt").st_size == 0:
            print("\n\tFile is empty. Please, enter data to work code\n")
            exit()

        #   Открытие файла с данными как read_file
        with open("Funcs/input_ex4.txt", "r") as read_file:
            #   Передача строк из файла в заранее созданный лист
            self.i_file_data = read_file.read()
            pass
        pass   
    pass

class cl_Ex_5:
    
    def i_do_get_value(self) -> list:
        output : list = []
        
        print("\n\n\tЗадание 5 \t Лаб. Функции\n\n")
        
        output.append(input("\nВведите строку:\t"))
        output.append(int(input("\nВведите ключ (1 - если вверхний регистр или 0 - если нижний):\t")))
        return output
    
    def i_do_compute_string(self) -> None:
        value : list = self.i_do_get_value()
        new_str : str = ""
        
        new_str = self.i_do_change_string(value[0], value[1])
        
        print(f"\nВаша новая строка:\n{new_str}")
        pass
    
    def i_do_change_string(self, string : str, case : bool = True) -> str:
        if case: return string.upper()
        else: return string.lower()
    pass

class cl_Ex_6:
    def __init__(self) -> None:
        self.i_connector : str = ":"
        pass
    
    def i_do_get_strings(self) -> list:
        output : list = []
        
        print("\n\n\tЗадание 6 \t Лаб. Функции\n\n")
        while True:
            in_str : str = input("\nВведите строку или оставтье ввод пустым, либо введите \"-\" и соеденительный символ:\t")
            
            if in_str == "" or in_str == " ": break
            elif in_str[0] == "-": self.i_connector = in_str[1:len(in_str)]
            else: output.append(in_str)
            pass
        
        
        return output
    
    def i_do_connect_strings(self, *strings, glue : str = ":") -> str:
        output : str = ""
        
        print(*strings)
        for string in strings:
            if len(string) > 3:
                if len(output) == 0: output += string
                else: output += glue + string
                pass
            pass
        return output
    
    def i_do_compute_strings(self) -> None:
        all_strings : list = self.i_do_get_strings()
        new_str : list = ""
        
        print(f"\nВведенные строки:\t{all_strings}")
        
        new_str = self.i_do_connect_strings(*all_strings, glue = self.i_connector)
        
        print(f"\nНовая строка:\n{new_str}")
        pass
    pass

ex1 = cl_Ex_1()
ex2 = cl_Ex_2()
ex3 = cl_Ex_3(use_string=True)
ex4 = cl_Ex_4()
ex5 = cl_Ex_5()
ex6 = cl_Ex_6()

exs : list = [ex1, ex2, ex3, ex4, ex5, ex6]
lng : int = len(exs)
i : int = 0
while True:
    print("\n\tЛабораторная работа по Функциям\nПаршаков М.В.\tИПО-21\n")
    print("\nСписок выполненных заданий:\n")
    
    while i < lng:
        print(f"Задание:\t{i+1}\n")
        i += 1
    i = 0
    
    answer = input("Введите номер задание или Q чтобы выйти: ")
    
    if answer == "q" or answer == "й":
        raise SystemExit
    
    match answer:
        case "1":
            ex1.do_show_output()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "2":
            ex2.do_find_max_nums()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "3":
            ex3.do_compute_nums_list()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "4":
            ex4.i_compute_nums()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "5":
            ex5.i_do_compute_string()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "6":
            ex6.i_do_compute_strings()
            input("\tНажмите Enter, чтобы продолжить")
            pass
    pass