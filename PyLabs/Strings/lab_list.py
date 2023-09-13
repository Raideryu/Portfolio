from statistics import *
import random as rnd

class cl_Ex_18:
    def __init__(self, exit_key : str, to_int : bool):
        self.in_exit_key = exit_key
        self.in_to_int = to_int
        pass
    
    def do_get_n_show_list(self) -> None:
        output : list = []
        
        print("\n\n\tЗадание 18 \t Лаб. Списки\n\n")
        while True:
            value : str = input("\nВведите целое число (если хотите завершить ввод -> введите 0): ")
            
            if value != self.in_exit_key and int(value):
                if self.in_to_int: output.append(int(value))
                else: output.append(value)
                pass
            else: break
            pass
        
        output.sort()
        print(f"\nВведенные значения:\n{output}")
        pass
    pass

class cl_Ex_19:
    def __init__(self, exit_key : str, to_int : bool):
        self.in_exit_key = exit_key
        self.in_to_int = to_int
        pass
    
    def do_get_n_show_list(self) -> None:
        output : list = []
        
        print("\n\n\tЗадание 19 \t Лаб. Списки\n\n")
        while True:
            value : str = input("\nВведите целое число (если хотите завершить ввод -> введите 0): ")
            
            if value != self.in_exit_key and int(value):
                if self.in_to_int: output.append(int(value))
                else: output.append(value)
                pass
            else: break
            pass
        
        output.sort(reverse = True)
        print(f"\nВведенные значения:\n{output}")
        pass
    pass

class cl_Ex_20:
    def __init__(self, exit_key : str = "", replay : bool = False):
        self.in_exit_key = exit_key
        self.in_replay = replay
        pass
    
    def do_get_words(self) -> None:
        output : list = []
        
        print("\n\n\tЗадание 20 \t Лаб. Списки\n\n")
        while True:
            value : str = input("\nВведите слово\n(нажмите enter без ввода слов, если хотите завершить ввод):\n")
            print(f"\n\tTaked word: {value}")
            if value != self.in_exit_key:
                print(f"\nExit key: {self.in_exit_key}")
                if not self.in_replay:
                    print(f"\nReplay mod: {self.in_replay}")
                    if (value not in output) or len(output) == 0: output.append(value)
                    pass
                else: output.append(value)
                pass
            else: break
            
            pass
        
        print(f"\nВведенные слова:\t{output}")
        pass
    pass

class cl_Ex_21:
    def do_get_nums():
        buffer : list = []
        output : list = []
        
        print("\n\n\tЗадание 21 \t Лаб. Списки\n\n")
        while True:
            value : str = input("\nВведите целое число\n(нажмите enter при пустой строке, чтобы закончить ввод):\n")
            
            if value != "": buffer.append(int(value))
            else: break
            pass     
        
        
        minus : list = []
        zeros : list = []
        pluses : list = []
        for num in buffer:
            if num < 0: minus.append(num)
            elif num == 0: zeros.append(num)
            elif num > 0: pluses.append(num)
            pass
        
        output.extend(minus), output.extend(zeros), output.extend(pluses)
        minus.clear(), zeros.clear(), pluses.clear(), buffer.clear()
        
        print(f"\nВведенные значения:\t{output}")
        pass
    pass

class cl_Ex_22:
    def do_show_mid():
        print("\n\n\tЗадание 22 \t Лаб. Списки\n\n")
        buffer : list = []
        
        mid_num : int = 0
        before_mid : list = []
        mid_nums : list = []
        after_mid : list = []
        
        while True:
            value : str = input("\nДля прекращения ввода оставьте строку пустой и нажмите enter\nВведите число: ")
            
            if value != "": buffer.append(int(value))
            else: break
            pass
        
        mid_num = int(mean(buffer))
        for num in buffer:
            if num < mid_num: before_mid.append(num)
            elif num == mid_num: mid_nums.append(num)
            else: after_mid.append(num)
            pass
        
        print(f"\nСреднее число ряда чисел:\t{mid_num}")
        
        if len(mid_nums) != 0: print(f"\nЧисла равные среднему значению:\t{mid_nums}")
        else: print(f"\nЧисла равные среднему значению:\tотсутствуют")
        if len(before_mid) != 0: print(f"\nЧисла ниже среднего значения:\t{before_mid}")
        else: print(f"\nЧисла ниже среднего значения:\tотсутствуют")
        if len(after_mid) != 0: print(f"\nЧисла выше среднего значения:\t{after_mid}")
        else: print(f"\nЧисла выше среднего значения:\tотсутствуют")
        pass
    pass

class cl_Ex_23:
    def __init__(self, max_tickets : int = 10, ticket_len : int = 6, rand_step : int = 2, tickets_sort : bool = False,
                 nums_sort : bool = True, true_rand : bool = True, display_all_tickets : bool = False) -> None:
        self.max_tickets = max_tickets
        self.ticket_len = ticket_len
        self.rand_step = rand_step
        self.tickets_sort = tickets_sort
        self.nums_sort = nums_sort
        self.true_rand = true_rand
        self.display_tickets = display_all_tickets
        self.all_nums : list = []
        self.tickets : list = []
        self.win_ticket : list = []
        self.try_count : int = 0
        self.win_taked : bool = False
        pass
    
    def do_generate_tickets(self):
        print("\n\n\tЗадание 23 \t Лаб. Списки\n\n")
        while len(self.all_nums) <= self.max_tickets * self.ticket_len:
            num : int = rnd.randrange(1, 49, self.rand_step)
            self.all_nums.append(num)
            pass
        i : int = 0
        while i < self.max_tickets:
            ticket : list = []
            while len(ticket) < self.ticket_len:
                num : int = rnd.choice(self.all_nums)
                if num not in ticket or len(ticket) == 0: ticket.append(num)
                pass
            #print(f"\nБилет: {ticket}\tпод номером: #{i+1}")
            if self.nums_sort: ticket.sort()
            self.tickets.append(ticket)
            i += 1
            pass
        i = 0
        
        if self.tickets_sort: self.tickets.sort()
        
        if self.true_rand:
            while len(self.win_ticket) < self.ticket_len:
                num : int = rnd.choice(self.all_nums)
                if num not in self.win_ticket or len(self.win_ticket) == 0: self.win_ticket.append(num)
                pass
            self.win_ticket.sort()
            pass
        else:
            self.win_ticket.extend(self.tickets[rnd.randint(0, self.max_tickets)])
            pass
        #print(f"\nwin ticket:\t{win_ticket}")
        #print(f"\nВсе билеты:\n{self.tickets}")
        
        winner : list = []
        winner_pos : int = 0
        
        for ticket in self.tickets:
            scorer : int = 0
            for num in ticket:
                if num in self.win_ticket: scorer += 1
                pass
            
            if scorer == self.ticket_len:
                winner.extend(ticket)
                winner_pos = i+1
                break
            i += 1
            pass
        i = 0
        
        if self.display_tickets:
            print("\nСписок всех билетов:\n")
            while i < len(self.tickets):
                print(f"#{i+1}\t{self.tickets[i]}")
                i += 1
                pass
            pass
        
        print(f"Выиграшный билет:\t{self.win_ticket}\nПобедил билет:\t{winner}\tпод номером #{winner_pos}\n")
        if len(winner) != 0: self.win_taked = True
        #print(f"\n\twin taked\t{self.win_taked}")
        self.do_clear()
        pass
    
    def do_clear(self) -> None:
        self.tickets.clear()
        self.win_ticket.clear()
        self.all_nums.clear()
        self.try_count += 1
        pass
    
    def _reset(self) -> None:
        self.win_taked = False
        self.try_count = 0
        pass
    pass

class cl_Ex_24:
    def __init__(self, single_string : bool = True, cut_char : chr = ' ', fix_size : bool = True) -> None:
        self.sngl_str = single_string
        self.cut_char = cut_char
        self.fix_size = fix_size
        self.words : list = []
        pass
    
    def _pig_language(self) -> None:
        output : str = ""
        
        print("\n\n\tЗадание 24 \t Лаб. Списки\n\n")
        self.words = self.do_get_strings()
        print(self.words)
        
        for word in self.words:
            output += self.do_convert_word(word) + " "
            pass
        
        print(f"\nВаши слова на свинячем языке:\t{output}")
        pass
    
    def do_convert_word(self, word : str) -> str:
        output : str = ""
        Buffer : str = ""
        
        char_list : list = ['a', 'e', 'o', 'i', 'u']
        
        if self.fix_size: word = word.lower()
        
        i : int = 0
        while i < len(word):
            char = word[i]
            
            if char in char_list and i == 0:
                word += "way"
                return word
            
            if char not in char_list:
                Buffer += char
                pass
            elif char in char_list and i != 0:
                Buffer += "ay"
                break
            
            if char not in char_list and i == len(word) - 1:
                Buffer += "ay"
                break
            
            i += 1
            pass
        
        while i < len(word):
            output += word[i]
            i += 1
            pass
        output += Buffer
        return output
    
    def do_get_strings(self) -> list:
        strings : str = input(f"\nВведите слова разделенные \"{self.cut_char}\":\t")
        words : list = []
        
        print(f"\nВведенные слова:\t{strings}")
        
        buffer : str = ""
        i : int = 0
        print(f"\nlen:\t{len(strings)}")
        while i < len(strings):
            #print(f"i:\t{i}")
            char = strings[i]
            #print(f"\nChar:\t{char}")
            if char != "" and char != self.cut_char: buffer += char
            elif  char == "\n" or char == self.cut_char:
                words.append(buffer)
                buffer = ""
                pass
            if i == len(strings) - 1:
                words.append(buffer)
                buffer = ""
                pass
            i += 1
            pass
        return words
    
    def _reset(self) -> None:
        self.words.clear()
        pass
    pass

class cl_Ex_25:
    def __init__(self, single_string : bool = True, cut_char : chr = ' ', fix_size : bool = True, use_key : bool = False, key_char : list = ['1', '2']) -> None:
        self.sngl_str = single_string
        self.cut_char = cut_char
        self.fix_size = fix_size
        self.use_key = use_key
        self.key_char = key_char
        
        self.output : str = ""
        self.symbs : list = []
        self.char_list : list = ['a', 'e', 'o', 'i', 'u']
            
        i : int = 33
        while i < 152:
            if i == 65: i = 91
            elif i == 97: i = 123
                
            self.symbs.append(i)
                
            i += 1
            pass
        pass
    
    def do_compute_words(self):
        output : str = ""
        string : list = self.do_form_words_list(self.get_words())
        print(f"\nВведенные слова:\t{string}")
        
        for word in string:
            buffer : str = ""
            sec_buffer : str = ""
            upper_char : bool = False

            i : int = 0
            while i < len(word):
                char = word[i]
                
                if char not in self.symbs:
                    if char.lower() in self.char_list and i == 0:
                        if ord(word[len(word)-1]) in self.symbs:
                            buffer = word[:len(word)-1] + "way" + word[len(word)-1]
                            output += buffer + " "
                            break
                        else:
                            buffer = word + "way"
                            output += buffer + " "
                            break
                    elif char.lower() not in self.char_list and i == 0:
                        if ord(char) >= 65 and ord(char) <= 90:
                            upper_char = True
                            buffer += char.lower()
                            pass
                        else: buffer += char
                        pass
                    
                    if char.lower() not in self.char_list and ord(char) not in self.symbs and i != 0: buffer += char
                    elif char.lower() in self.char_list and i != 0:
                        buffer += "ay"
                        
                        j : int = i
                        while j < len(word):
                            if ord(word[j]) not in self.symbs: sec_buffer += word[j]
                            elif ord(word[j]) in self.symbs and j == len(word)-1:
                                sec_buffer += buffer + word[j]
                                break
                            
                            if j != len(word)-1 and ord(word[j]) in self.symbs and ord(word[j+1]) not in self.symbs:
                                sec_buffer += buffer + word[j]
                                buffer = ""
                                pass
                            
                            if j == len(word)-1 and ord(word[j]) not in self.symbs and buffer != "":
                                sec_buffer += buffer
                                break
                            j += 1
                            pass
                        break
                    
                    if i == len(word) - 1 and buffer != "":
                        buffer += "ay"
                        if ord(char) not in self.symbs and char in buffer: sec_buffer += buffer
                        elif ord(char) in self.symbs: sec_buffer += buffer + char 
                    pass
            
                i += 1
                pass
            
            if upper_char:
                sec_buffer = sec_buffer.capitalize()
                pass
            
            if sec_buffer != "": output += sec_buffer + " "
            pass
        
        return output
    
    def _show_output(self) -> None:
        print("\n\n\tЗадание 25 \t Лаб. Списки\n\n")
        
        self.output = self.do_compute_words()
        
        print(f"\nПолученный результат:\t{self.output}")
        self.output = ""
        pass
    
    def do_form_words_list(self, string : str) -> list:
        output : list = []
        
        buffer : str = ""
        i : int = 0
        while i < len(string):
            char = string[i]
            if char != self.cut_char: buffer += char
            elif char == self.cut_char:
                output.append(buffer)
                buffer = ""
                pass
            
            if i == len(string) - 1:
                output.append(buffer)
                buffer = ""
                pass
            i += 1
            pass
        return output
    
    def get_words(self) -> str: return input(f"\nВведите предложение или слова по отдельности:\n") if not self.use_key else input(f"\nВ начале строки, перед введенными данными, введите {self.key_char[0]},"
        f" если будет введено предложение, или {self.key_char[1]}, если будет введены отдельные слова.\nВвод:\t")
    pass

ex18 = cl_Ex_18("0", True)
ex19 = cl_Ex_19("0", True)
ex20 = cl_Ex_20("", False)
ex21 = cl_Ex_21
ex22 = cl_Ex_22
ex23 = cl_Ex_23(tickets_sort=True, max_tickets=1000, true_rand=True)
ex24 = cl_Ex_24(single_string=True, cut_char=' ')
ex25 = cl_Ex_25(fix_size=False, use_key=False)

exs : list = [ex18, ex19, ex20, ex21, ex22, ex23, ex24, ex25]
lng : int = len(exs)
count : int = 18
while True:
    print("\n\tЛабораторная работа по строкам\nПаршаков М.В.\tИПО-21\n")
    print("\nСписок выполненных заданий:\n")
    
    while count <= lng+17:
        print(f"\tЗадание:\t{count}\n")
        count += 1
    count = 18
    
    answer = input("Введите номер задание или Q чтобы выйти: ")
    
    if answer == "q" or answer == "й": raise SystemExit
    
    match answer:
        case "18":
            ex18.do_get_n_show_list()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "19":
            ex19.do_get_n_show_list()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "20":
            ex20.do_get_words()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "21":
            ex21.do_get_nums()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "22":
            ex22.do_show_mid()
            input("\tНажмите Enter, чтобы продолжить")
            pass
        case "23":
            while not ex23.win_taked:
                ex23.win_taked: ex23.do_generate_tickets()
                pass
            print(f"\n\n\tПотраченно попыток\t{ex23.try_count+1}")
            input("\tНажмите Enter, чтобы продолжить")
            ex23._reset()
            pass
        case "24":
            ex24._pig_language()
            input("\tНажмите Enter, чтобы продолжить")
            ex24._reset()
            pass
        case "25":
            ex25._show_output()
            input("\tНажмите Enter, чтобы продолжить")
            pass
    pass