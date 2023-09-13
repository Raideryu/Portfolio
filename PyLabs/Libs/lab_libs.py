import os
import json
import keyboard as kbd
import random as rnd
import math

class cl_Ex_1:
    
    def i_do_compute_got_lib(self, string : str = "") -> dict:
        key : str = ""
        value : str = ""
        i : int = 0
        while i < len(string):
            buffer : str = ""
            char : chr = string[i]
            
            if char == '-' and string[i+1] == "k":
                j : int = i + 2
                
                while j < len(string):
                    if j != len(string) - 1 and string[j] != "^": buffer += string[j]
                    else:
                        if string[j] != '^': buffer += string[j]
                        key = buffer
                        buffer = ""
                        print(f"\nKey:\t{key}")
                        break
                    j += 1
                    pass
                pass
            elif char == "-" and string[i+1] == "v":
                j : int = i + 2
                
                while j < len(string):
                    if j != len(string) - 1 and string[j] != "^": buffer += string[j]
                    else:
                        if string[j] != '^': buffer += string[j]
                        value = buffer
                        buffer = ""
                        print(f"\nValue:\t{value}")
                        break
                    j += 1
                    pass
                pass
            elif i == len(string) - 1 or (key != "" and value != ""): break
            i += 1
            pass
        return {key : value}
    
    def i_do_get_dict(self) -> dict:
        out_lib : dict = dict()
        
        while True:
            buffer : str = input("\nВведите ключ и значение разделив их \"^\" без пробелов."
                                 + "\nПеред ключем поставтье \"-k\" (англ). А перед значением - \"-v\"\n")
            if buffer == "" or buffer == " ": break
            elif buffer == "q" or buffer == "й": raise SystemExit
            else:
                print(f"\nString:\t{buffer}")
                out_lib.update(self.i_do_compute_got_lib(buffer))
                print(f"\ndict now:\t{out_lib}")
                pass
            pass
        return out_lib
    
    def i_reverse_lookup(self, lib : dict, trgt_value : str) -> list:
        out_lib : list = []
        
        for key, value in lib.items():
            if value == trgt_value: out_lib.append(key)
            pass
        return out_lib
    
    def _main(self) -> None:
        input_lib : dict = self.i_do_get_dict()
        trgt_value : str = input("\nВведите значение по которому будут искаться ключи:\t")
        
        print(f"\nВведенный словарь:\n\"{input_lib}\"\n и значение для поиска:\t\"{trgt_value}\"")
        new_dict : list = self.i_reverse_lookup(input_lib, trgt_value)
        
        print(f"\nСписок ключей со значением равному \"{trgt_value}\":\n{new_dict}")
        pass
    pass

class cl_Ex_2:
    def __init__(self) -> None:
        self.all_stats : dict = dict()
        pass
    
    def i_do_get_2d6(self) -> int: return rnd.randint(1, 6) + rnd.randint(1, 6)
    
    def i_do_form_stat_string(self, pos : int, freq : int, all_freq) -> list:
        freq_i : float = round(freq / all_freq, 3)
        frct = self.i_do_get_forecast(pos)
        return {"pos" : pos, "f" : freq, "fi" : freq_i, "ft" : frct}
    
    def i_do_get_forecast(self, num : int):
        p : float = round(1/6+1/6,3)
        q : float = round(1 - p,3)
        count : float = 0
        
        if num >= 5 and num <= 9: count = round(100*p+p, 3)
        else: count = round(100*p-q, 3)
        
        print(f"\nnum: {num}, count: {count}")
        C = math.factorial(100)/(self._fact(count) * self._fact(100-count))
        
        return round(C * p**count * q**(100-count),3) * 10
    
    def _fact(self, n : float) -> float:
        fact : float = 1
        while n > 1:
            fact *= n
            n -= 1
            pass
        return fact
    
    def _main(self) -> None:
        results : dict() = dict()
        all_freq : int = 1000
        
        i : int = 0
        while i < 1000:
            result : int = self.i_do_get_2d6()
            
            if result not in results.keys(): results[result] = 1
            else: results[result] += 1
            i += 1
            pass
        
        results = dict(sorted(results.items()))
        
        i = 1
        for key in results:
            self.all_stats[i] = self.i_do_form_stat_string(key, results[key], all_freq)
            i += 1
            pass
        
        print("\nЗначение\tЧастота\tОтносительная частота\tПрогноз")
        for key, string in self.all_stats.items():
            for value in string:
                print(f"{string[value]}\t|", end = "\t")
                pass
            print("\n")
            pass
        print("\n")
        #print(math.factorial(1000))
        pass
    pass

class cl_Ex_3:
    def __init__(self) -> None:
        self.i_key_lib : dict = {
            '1' : ['.', ',', '?', '!', ';'],
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z'],
            '0' : [' '],
        }
        pass
    
    def _main(self) -> None:
        writer : str = ""
        message : str = ""
        
        print("\n\n\tЗадание 3 \t Лаб. Словари\n\n")
        print("\nКлавиши для взаимодействия:\n\'1\'-\'0\' - клавиши выбора символа"
              + "\n\'ctrl\' - добавить текущий символ в строку"
              + "\n\'shift\' - меняет символ на строчный или прописной"
              + "\n\'backspace\' - удаляет текущий символ из строки"
              + "\n\'enter\' - завершить ввод"
              + "\nПамятка по символам:\n"
              + "\'1\':\t. , ? ! ;\n"
              + "\'2\':\ta b c\n"
              + "\'3\':\td e f\n"
              + "\'4\':\tg h i\n"
              + "\'5\':\tj k l\n"
              + "\'6\':\tm n o\n"
              + "\'7\':\tp q r s\n"
              + "\'8\':\tt u v\n"
              + "\'9\':\tw x y z\n"
              + "\'0\':\t\'пробел\'\n")
        
        while True:
            event = kbd.read_event()
            if event.event_type == kbd.KEY_DOWN:
                if event.name == 'enter': break
                
                if event.name == "ctrl": message += message[len(message)-1]
                elif event.name == "shift":
                    if message[len(message)-1].isupper(): char = message[len(message)-1].lower()
                    else: char = message[len(message)-1].upper()
                    
                    message = message[:len(message)-1] + char if len(message) > 1 else char
                    pass
                elif event.name == 'backspace': message = message[:len(message)-1] if len(message) > 1 else ""
                else: 
                    symbs : list = self.i_key_lib[event.name]
                    
                    writer += event.name
                    
                    if len(message) == 0:
                        message += symbs[0]
                        pass
                    
                    if message[len(message)-1].lower() in symbs:
                        char = symbs[symbs.index(message[len(message)-1].lower()) + 1] if symbs.index(message[len(message)-1].lower()) != len(symbs)-1 else symbs[0]
                        message = message[:len(message)-1] + char if len(message) > 1 else char
                        pass
                    elif message[len(message)-1] not in symbs: message += symbs[0]
                    pass
                print(message)
                pass
            pass
        print(f"full message:\t{message}")
        input()
        pass
    pass

class cl_Ex_4:
    def __init__(self) -> None:
        self.i_lib : dict = {
            "a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ".", "f" : "..-.",
            "g" : "--.", "h" : "....", "i" : "..", "j" : ".---", "k" : "-.-", "l" : ".-..",
            "m" : "--", "n" : "-.", "o" : "---", "p" : ".--.", "q" : "--.-", "r" : ".-.",
            "s" : "...", "t" : "-", "u" : "..-", "v" : "...-", "w" : ".--", "x" : "-..-",
            "y" : "-.--", "z" : "--..",
            "0" : "-----", "1" : ".----", "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....",
            "6" : "-....", "7" : "--...", "8" : "---..", "9" : "----.", 
        }
        pass
    
    def i_do_convert_string(self, string : str) -> str:
        output : str = ""
        
        for char in string.lower():
            if char in self.i_lib.keys(): output += self.i_lib[char] + " "
            pass
        return output
    
    def _main(self) -> None:
        print("\n\n\tЗадание 4 \t Лаб. Словари\n\n")
        message : str = input("\nВведите любое сообщение:\t")
        
        print(f"\nВаше введенное сообщение:\t{message}\nВаше шифрованное сообщение:\t{self.i_do_convert_string(message)}")
        pass
    pass

class cl_Ex_5:
    def __init__(self) -> None:
        self.i_f_tier : dict = {
            '0' : "zero", '1' : "one", '2' : "two", '3' : "three", '4' : "four",
            '5' : "five", '6' : "six", '7' : "seven", '8' : "eigth", '9' : "nine",
        }
        self.i_t_tier : dict = {
            '1' : {
                '0' : "ten", '1' : "eleven", '2' : "twelve", '3' : "thirteen", '4' : "fourteen",  '5' : "fifteen",
                '6' : "sixteen",  '7' : "seventeen",  '8' : "eighteen",  '9' : "nineteen",
            },
            '2' : "twenty",  '3' : "thirty",  '4' : "fourty",  '5' : "fifty",
            '6' : "sixty",  '7' : "seventy",  '8' : "eighty",  '9' : "ninety",
        }
        self.i_th_tier : str = "hundred"
        pass
    
    def i_do_convert(self, string : str) -> str:
        output : str = ""
        
        while len(string) != 0:
            
            match len(string):
                case 1:
                    output += self.i_f_tier[string[0]]
                    string = ""
                    break
                case 2:
                    if string[0] == '1':
                        output += self.i_t_tier[string[0]][string[1]]
                        string = ""
                        pass
                    elif string[0] == '0' and string[1] != '0': string = string[1:]
                    elif string[0] == '0' and string[1] == '0': string = ""
                    else:
                        output += self.i_t_tier[string[0]] + " "
                        if string[1] == '0': string = ""
                        else: string = string[1:]
                        pass
                    pass
                case 3:
                    output += self.i_f_tier[string[0]] + " " + self.i_th_tier + " "
                    string = string[1:]
                    pass
                case _:
                    return "\n\t-A wrong value-\n"
                
            pass
        return output
    
    def _main(self) -> None:
        
        print("\n\n\tЗадание 5 \t Лаб. Словари\n\n")
        message : str = input("\nВведите число от 0 до 999: ")
        print(f"\nВаше введенное число: {message}")
        print(f"\nВаше число после конвертации:\t{self.i_do_convert(message)}")
        pass
    pass

class cl_Ex_6:
    def _main(self) -> None:
        
        print("\n\n\tЗадание 4 \t Лаб. Словари\n\n")
        message : str = input("\nВведите любое сообщение: ")
        print(f"\nВаше сообщение:\t{message}")
        print(f"\nКол-во уникальных символов:\t{len(set(message))}")
        pass
    pass

class cl_Ex_7:
    def __init__(self) -> None:
        self.__i_card_ref : dict = {
            'B' : [], 'I' : [], 'N' : [], 'G' : [], 'O' : [],
        }
        
        self.__i_symbs : list = ['B', 'I', 'N', 'G', 'O']
        self.__i_card_numbs : list = []
        self.__i_card : dict = self.i_do_form_card()
        pass
    
    def _set_card(self, new_card : dict) -> None: self.__i_card = new_card
    
    def __get_card(self) -> dict: return self.__i_card.copy()
    
    def _get_card_data(self, key : chr = None, pos : int = None):
        card : dict = self.__get_card()
        
        if key == None and pos == None: return card.copy()
        elif key != None and pos == None: return card[key].copy()
        else: return card[key][pos]
            
    def _add_value_to_num_list(self, value, pos : int = None) -> None:
        if pos != None: self.__i_card_numbs[pos].append(value)
        else: self.__i_card_numbs.append(value)
    
    def _get_num_list(self) -> list: return self.__i_card_numbs.copy()
    
    def _show_num_list(self) -> None: print(self.__i_card_numbs.copy())        
    
    def i_do_show_card(self, card : dict) -> None:
        for key in card.keys():
            print(f"| {key} ", end="")
            pass
        print("|")
        i : int = 0
        while i < 5:
            for key in card.keys():
                print(f"| {card[key][i]} ", end="")
                pass
            print("|")
            i += 1
            pass
        pass
    
    def i_do_form_card(self) -> dict:
        new_card : dict = dict()
        
        for key in self.__i_symbs:
            nums : list = []
            i : int = 0
            self._add_value_to_num_list(list())
            while i < 5:
                match key:
                    case 'B':
                        num : int = rnd.randint(1, 15)
                        nums.append(num)
                        new_card[key] = nums
                        self._add_value_to_num_list(num, 0)
                        pass
                    case 'I':
                        num : int = rnd.randint(16, 30)
                        nums.append(num)
                        new_card[key] = nums
                        self._add_value_to_num_list(num, 1)
                        pass
                    case 'N':
                        num : int = rnd.randint(31, 45)
                        nums.append(num)
                        new_card[key] = nums
                        self._add_value_to_num_list(num, 2)
                        pass
                    case 'G':
                        num : int = rnd.randint(46, 60)
                        nums.append(num)
                        new_card[key] = nums
                        self._add_value_to_num_list(num, 3)
                        pass
                    case 'O':
                        num : int = rnd.randint(61, 75)
                        nums.append(num)
                        new_card[key] = nums
                        self._add_value_to_num_list(num, 4)
                        pass
                i += 1
                pass
            
            pass
        return new_card.copy()
    
    def _main(self) -> None:
        my_card : dict = self.i_do_form_card()
        
        print("\n\n\tЗадание 4 \t Лаб. Словари\n\n")
        print("\nВаша бинго карта:\n")
        #print(my_card)
        self.i_do_show_card(my_card)
        pass
    pass

class cl_Ex_8:
    
    def __init__(self) -> None:
        pass
    pass

class cl_Ex_9:
    def __init__(self) -> None:
        self.__i_card_former = cl_Ex_7()
        self.__i_path : str = "Libs/card_data.json"
        self.__i_cards_list : list = []
        pass
    
    def _get_path(self) -> str: return self.__i_path
    
    def _add_card_to_list(self, card : dict) -> None: self.__i_cards_list.append(card)
    def _get_card_from_list(self, card_num : int) -> dict: return self.__i_cards_list[card_num].copy()
    def _get_list(self) -> list: return self.__i_cards_list.copy()
    
    def __check_file(self, key : str = 'w') -> bool:
        match key:
            case 'w':
                if not os.path.exists(self.__i_path):
                #   Создание файла при его отсутствие
                    with open(self.__i_path, "w") as file:
                        print("\tFile is not exist so it was created\n\tPlease enter data in that file to work code\n")
                        return True
                elif os.stat(self.__i_path).st_size != 0:
                    os.remove(self.__i_path)
                    
                    with open(self.__i_path, "w") as file:
                        print("\tFile was recreate\n")
                        return True
                else: return True
            case 'r':
                if os.stat(self.__i_path).st_size == 0:
                    print("\n\tFile is empty. Please, enter data to work code\n")
                    exit()
                else: return True
        
    def _write_card(self, card : dict) -> None:
        if self.__check_file():
            with open(self.__i_path, 'w') as json_file:
                json.dump(card, json_file)
                pass
    
    def _read_card(self) -> dict:
        if self.__check_file(key = 'r'):
            with open(self.__i_path, 'r') as json_file:
                return dict(json.load(json_file))
    
    def __i_do_check_num(self, card : dict, num : int) -> dict:
        for key in card.keys():
            if num in card[key]:
                i : int = 0
                while i < len(card[key]):
                    #print(card[key][i])
                    if num == card[key][i]:
                        card[key][i] = 0
                        break
                    i += 1
                    pass
                pass
            pass
        return card
    
    def __i_do_check_card_lines(self, card : dict) -> bool:
        for key in card.keys():
            if len(set(card[key])) == 1: return True
            pass
        
        i : int = 0
        while i < len(card['B']):
            if len(set([card['B'][i], card['I'][i], card['N'][i], card['G'][i], card['O'][i]])) == 1: return True
            i += 1
            pass
        
        if len(set([card['B'][0], card['I'][1], card['N'][2], card['G'][3], card['O'][4]])) == 1 or len(set([card['B'][4], card['I'][3], card['N'][2], card['G'][1], card['O'][0]])) == 1: return True
        
        return False
    
    def i_do_sim_bingo(self) -> list:
        card : dict = self.__i_card_former.i_do_form_card()
        self._write_card(card)
        print("\nВаш билет:\n")
        self.__i_card_former.i_do_show_card(card)
        
        card_num : int = 1
        tries : int = 1
        tries_list : list = []
        
        print("\n\tForming nums list\n")
        nums : list = list(range(1,76))
        print("\nNums list is formed\n")
        
        i : int = 0
        while i < 1000:
            rnd.shuffle(nums)
            if len(nums) < 1: nums = list(range(1,76))
            print('.', end=' ')
                
            card = self.__i_do_check_num(card, nums.pop(0))
                
            if self.__i_do_check_card_lines(card):
                self._add_card_to_list([card_num, tries, card])
                tries_list.append(tries)
                    
                print(f"\nБилет под номером {card_num} выиграл с {tries} попытки! Победный билет:\n")
                self.__i_card_former.i_do_show_card(card)
                #print(tries_list)
                    
                tries = 1
                card_num += 1
                    
                card = self._read_card()
                pass
            else: tries += 1
            i += 1
            pass
        print("\n")
        #print(tries_list)
        return tries_list
    
    def i_do_compute_stats(self, stats : list) -> None:
        print(f"\nМинимальное кол-во попыткок:\t{min(stats)}"
              + f"\nМаксимальное кол-во попыток:\t{max(stats)}"
              + f"\nСреднее кол-во попыток:\t{round(sum(stats)/len(stats), 2)}"
              + f"\nВсего попыток:\t{sum(stats)}"  
        )
        pass
    
    def __reset(self) -> None:
        self.__i_cards_list.clear()
        if os.path.exists(self.__i_path) and os.stat(self.__i_path).st_size != 0: os.remove(self.__i_path)
        pass
    
    def _main(self) -> None:
        stat : list = self.i_do_sim_bingo()
        self.i_do_compute_stats(stat)
        self.__reset()
        pass
        
    pass

ex1 = cl_Ex_1()
ex2 = cl_Ex_2()
ex3 = cl_Ex_3()
ex4 = cl_Ex_4()
ex5 = cl_Ex_5()
ex6 = cl_Ex_6()
ex7 = cl_Ex_7()
ex8 = cl_Ex_8()
ex9 = cl_Ex_9()


exs : list = [ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9]
count : int = 1

while True:
    print("\n\tЛабораторная работа по словарям\nПаршаков М.В.\tИПО-21\n")
    print("\nСписок выполненных заданий:\n")
    
    while count <= len(exs):
        print(f"\tЗадание:\t{count}\n")
        count += 1
    count = 1
    
    answer = input("Введите номер задание или Q чтобы выйти: ")
    
    if answer == "q" or answer == "й": raise SystemExit
    
    match answer:
        case "1":
            ex1._main()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "2":
            ex2._main()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "3":
            ex3._main()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "4":
            ex4._main()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "5":
            ex5._main()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "6":
            ex6._main()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "7":
            ex7._main()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "8":
            pass
        case "9":
            ex9._main()
            input("\tНажмите Enter, чтобы продолжить")
            pass
    pass