from unicodedata import name
import math
import time


class Ex_1:
    name = "Матвей"
    email = "my.email@yandex.ru"
    
    def do_get_info(self, name, email):
        print(f"\nЗадание 1 \t Лаб. Строки\n\n\tМое имя: {name} \tМоя почта: {email}\n")
        pass
    pass

class Ex_2:
    
    def do_get_EnteredName(self):
        print("\nЗадание 2 \t Лаб. Строки\n\n")
        name = input("Please, enter your name: ")
        print(f"\n\tПриветствую, {name}!\n")
        pass
    pass

class Ex_3:
    
    def do_get_RoomSquare():
        print("\nЗадание 3 \t Лаб. Строки\n\n")
        a = input("Введите длину комнаты (со знаком после запятой): ")
        b = input("Введите ширину комнаты (со знаком после запятой): ")
        square = float(a) * float(b)
        print(f"\n\tПлощадь комнаты равна: \t{square} М\n")
        pass
    pass

class Ex_4:
    
    def do_get_LandSquare():
        print("\nЗадание 4 \t Лаб. Строки\n\n")
        a = input("Введите длину поля в метрах: ")
        b = input("Введите ширину поля в метрах: ")
        square = (float(a) * float(b)) / 10000
        print(f"\nПлощадь поля равна \t{square} Га\n")
        pass
    pass
        
class Ex_5:
    
    def do_get_tax():
        print("\nЗадание 5 \t Лаб. Строки\n\n")
        order = input("Введите сумму заказа: ")
        order = float(order)
        tax = order * 0.13
        tips = order * 0.18
        total = float(order + tax + tips)
        print(f"\n\t\tЧек\nСумма заказа:\t{order:.2f}\nНалог:\t\t{tax:.2f}\nЧаевые:\t\t{tips:.2f}\nИтог:\t\t{total:.2f}")
        pass
    pass
        
class Ex_6:
    
    def do_get_sum():
        print("\nЗадание 6 \t Лаб. Строки\n\n")
        num = input("Введите число: ")
        num = int(num)
        sum = (num * (num + 1)) / 2
        print("\nСумма натуральных чисел по формуле:\t", sum)
        pass
    pass

class Ex_7:

    def do_get_sum():
        
        def Total_wt(num):
            
            if num > 1000:
                num = float(num / 1000)
                
                print(f"\nОбщий вес посылки:\t{num} кг\n")
            else:
                print(f"\nОбщий вес посылки:\t{num} грамм\n")
            pass
                
        wt_f = 75
        wt_s = 112
    
        print("\nЗадание 7 \t Лаб. Строки\n\n")
        pack_f = input("Введите кол-во сувениров: ")
        pack_f = int(pack_f)
        
        pack_s = input("Введите кол-во безделушек: ")
        pack_s = int(pack_s)
        
        pack_f *= wt_f
        pack_s *= wt_s
        
        total = pack_f + pack_s
        
        Total_wt(total)
    pass

class Ex_8:
    
    def do_get_sum():
        rate = 0.04
        step = 0
        
        print("\nЗадание 8 \t Лаб. Строки\n\n")
        deposit = float(input("Введите сумму вклада: "))
        
        while step < 3:
            deposit = deposit + (deposit * rate)
            deposit = round(deposit, 2)
            print(f"\nИтог за {step + 1} год:\t{deposit}")
            step += 1
        pass
    pass

class Ex_9:
    
    def Total():
        
        def do_calculate(num_a, num_b, step):
            if step == 0:
                sum_a_b = num_a + num_b
                return sum_a_b
            
            elif step == 1:
                diff = 0
                if num_a >= num_b:
                    diff = num_a - num_b
                else:
                    diff = num_b - num_a
                return diff
            
            elif step == 2:
                multi = num_a * num_b
                return multi
            
            elif step == 3:
                divi = float(num_a / num_b)
                divi = round(divi, 2)
                return divi
            
            elif step == 4:
                divi_re = num_a % num_b
                return divi_re
            
            elif step == 5:
                log_a = float(math.log10(num_a))
                log_a = round(log_a, 2)
                return log_a
            
            elif step == 6:
                degree = num_a ** num_b
                return degree
            
        print("\nЗадание 9 \t Лаб. Строки\n\n")
        
        a = input("\nВведите число а: ")
        b = input("\nВведите число b: ")
        a = int(a)
        b = int(b)
        
        num = 0
        
        while num < 7:
            answer = do_calculate(a, b, num)
            print(f"\nПункт\t{num + 1}\nответ:\t{answer}\n")
            num += 1
        pass
    pass

class Ex_10:
    
    def do_get_coordinates():
        point_1 = []
        point_2 = []
        
        i = 0
        j = 0
        
        print("\nЗадание 10 \t Лаб. Строки\n\n")
        
        while i < 2:
            while j < 2:
                if j == 0:
                   taken = input(f"Введите широту {i + 1}-й точки: ")
                elif j == 1:
                   taken = input(f"Введите долготу {i + 1}-й точки: ")
                
                taken = float(taken)
                
                if i == 0:
                    point_1.append(taken)
                elif i == 1:
                    point_2.append(taken)
                
                j += 1
            
            j = 0
            i += 1
        i = 0
        j = 0
        
        print("\nПервая точка")
        for item in point_1:
            print(f"\n\t{item}")
        
        print("\nВторая точка")
        for item in point_2:
            print(f"\n\t{item}")

        while i < 2:
            point_1[i] = math.radians(point_1[i])
            point_2[i] = math.radians(point_2[i])
            i += 1
        i = 0
        
        distance = 6471.01 * math.acos(math.sin(point_1[0]) * math.sin(point_2[0]) + math.cos(point_1[0]) * math.cos(point_2[0]) * math.cos(point_1[1] - point_2[1]))
        distance = round(distance, 3)
        print(f"\nДистанция от первой точки до второй:\t{distance}\n")
        pass
    pass

class Ex_11:
    
    def do_calculate():
        print("\nЗадание 11 \t Лаб. Строки\n\n")
        
        r = float(input("\nВведите радиус:\t"))
        square = float(r * (math.pi ** 2))
        volume = (4/3) * (math.pi * (r ** 3))
        ball_square = 4 * math.pi * (r ** 2)
        
        print(f"Площадь круга:\t%.2f" % square, "\nОбъем шара:\t%.2f" % volume, "\nПлошадь шаровой поверхности:\t%.2f" % ball_square, "\n")
        pass
    
    pass 

class Ex_12:
    water_C = 4.186
    mass = 0.00
    mass_for_cup = 0.00
    t_0 = 0.00
    cost = 0.00
    
    def do_calculate_temp():
        lever = 1
        
        print("\nЗадание 12 \t Лаб. Строки\n\n")
        
        Ex_12.mass = float(input("\nВведите объем нагреваеммой воды: "))
        
        while lever == 1:
            Ex_12.mass_for_cup = float(input("\nВведите объем воды для чашки (не больше 500 мл. Записать в мл (целым числом)): "))
            
            if Ex_12.mass_for_cup < 0 or Ex_12.mass_for_cup > 500.00:
                print("\nНеверное значение. Повторите еще раз.\n")
                pass
            else:
                break
        
        Ex_12.t_0 = float(input("\nВведите изначальную температуру воды: "))
        water_t = float(input("\nВведите требуемую температуру воды: "))
        
        del_t = water_t - Ex_12.t_0
        
        water_q = Ex_12.mass * Ex_12.water_C * del_t
        cup_q = Ex_12.mass_for_cup * Ex_12.water_C * del_t
        
        electric_cup = cup_q / float(3600000)
        electric_water = water_q / float(3600000)
        
        el_cost_cup = 1.3 * electric_cup
        el_cost_water = 1.3 * electric_water
        
        print("\nТребуемая энергия для изменения температуры воды:\t%.2f" % water_q, "\nЗатраты в киловаты час: %.2f" % electric_water, "\tСтоимость: %.2f\n" % el_cost_water)
        print("\nТребуемая энергия для нагрева воды в чашке:\t%.2f" % cup_q, "\nЗатраты в киловаты час: %.2f" % electric_cup, "\tСтоимость: %.2f\n" % el_cost_cup)
        
        pass
    pass

class Ex_13:
    
    def do_convert_interval():
        interval = []
        i = 0
        value = 0
        
        print("\nЗадание 13 \t Лаб. Строки\n\n")
        
        while i < 4:
            print("\nCcounter: ", i)
            if i == 0:
                value = int(input("\nВведите кол-во пройденных дней\n"))
                interval.append(value)
                pass
            elif i == 1:
                value = int(input("\nВведите кол-во пройденных часов\n"))
                interval.append(value)
                pass
            elif i == 2:
                value = int(input("\nВведите кол-во пройденных минут\n"))
                interval.append(value)
                pass
            elif i == 3:
                value = int(input("\nВведите кол-во пройденных секунд\n"))
                interval.append(value)
                pass
            i += 1
        
        total_sec = (interval[0] * 24 * 60 * 60) + (interval[1] * 60 * 60) + (interval[2] * 60) + interval[3]
        
        print(f"\nВы ввели:\nДней: {interval[0]}\tЧасов: {interval[1]}\tМинут: {interval[2]}\tСекунд: {interval[3]}\n")
        print("\nИтоговый промежуток в секундах: ", total_sec)    
        pass
    pass

class Ex_14:
    
    def do_convert_interval():
        interval = []
        i = 0
        value = 0
        print("\nЗадание 14 \t Лаб. Строки\n\n")
        time = int(input("\nВведите временой промежуток в секундах: "))

        if len(interval) == 0:
            if time/(24 * 60 * 60) > 1:
                value = int(time/(24 * 60 * 60))
                interval.append(value)
                time -= value - 24 * 60 * 60
                pass
            else:
                interval.append(0)
                pass
            pass
            
        if len(interval) == 1:
            if time/(60 * 60) > 1:
                if time/(60 * 60) < 10:
                    value = int(time/(60 * 60))
                    interval.append("{0:02}".format((value)))
                    pass
                else:
                    value = int(time/(60 * 60))
                    interval.append((value))
                    pass
                print("\nDD: ", value)
                time -= value * 60 * 60
                pass
            else:
                interval.append("{0:02}".format((0)))
                pass
            pass
        
        if len(interval) == 2:
            if time/60 > 1:
                if time/ 60 < 10:
                    value = int(time/60)
                    interval.append("{0:02}".format((value)))
                    pass
                else:
                    value = int(time/60)
                    interval.append((value))
                    pass
                time -= value * 60
                pass
            else:
                interval.append("{0:02}".format((0)))
                pass
            pass
        
        if len(interval) == 3:
            if time > 1:
                if time < 10:
                    value = int(time)
                    interval.append("{0:02}".format((value)))
                    pass
                else:
                    value = int(time)
                    interval.append((value))
                    pass
                time -= value
                pass
            else:
                interval.append("{0:02}".format((0)))
                pass
            pass
        
        print(f"промежуток:\n{interval}\tD:HH:MM:SS\n")
        
        pass
    pass

class Ex_15:
    def __init__(self, times : time):
        self.time = times.asctime()
        pass
    
    def do_show_time(self) -> None:
        print("\nЗадание 15 \t Лаб. Строки\n\n")
        self.time = time.asctime()
        print(f"\nTime:\t{self.time}")
        pass
    pass

class Ex_16:
    def __init__(self):        
        self.output : int = 0
        pass
    
    def do_show_answer(self) -> None:
        print("\nЗадание 16 \t Лаб. Строки\n\n")
        in_num : str = input("Введите любое 4-х значное число: ")
        
        for char in in_num:
            self.output += int(char)
            pass
        
        print(f"\nСумма цифр в числе:\t{self.output}")
        pass
    pass

class Ex_17:
    def do_show_range():
        input_nums : list = []
        buffer : int = 0
        output : list = []
        
        print("\n\tЗадание 17 \t Лаб. Строки\n\n")
        print("\nВведите 3 целых числа:")
        
        i : int = 0
        while i < 3:
            input_num = int(input("\nВведите целое число: "))
            input_nums.append(input_num)
            i += 1
            pass
        i = 0
        
        print(f"\nВведенные числа:\t{input_nums}")
        
        output.append(min(input_nums))
        output.append(max(input_nums))
        
        print(output)
        
        while i < 3:
            
            if input_nums[i] != output[0] and input_nums[i] != output[1]:
                output.insert(1, input_nums[i])
                break
            i += 1
            pass
        
        print(f"\nРезультат сортировки:\t{output}")
        pass
    pass
n = 0

ex1 = Ex_1
ex2 = Ex_2
ex3 = Ex_3
ex4 = Ex_4
ex5 = Ex_5
ex6 = Ex_6
ex7 = Ex_7
ex8 = Ex_8
ex9 = Ex_9
ex10 = Ex_10
ex11 = Ex_11
ex12 = Ex_12
ex13 = Ex_13
ex14 = Ex_14
ex15 = Ex_15(time)
ex16 = Ex_16()
ex17 = Ex_17

exs = [ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex10, ex11, ex12, ex13, ex14, ex15, ex16, ex17]
lng = len(exs)
count = 1

while n < 6:
    print("\n\tЛабораторная работа по строкам\nПаршаков М.В.\tИПО-21\n")
    print("\nСписок выполненных заданий:\n")
    
    while count <= lng:
        print(f"Задание:\t{count}\n")
        count += 1
    count = 1
    
    answer = input("Введите номер задание или Q чтобы выйти: ")
    
    if answer == "q" or answer == "й":
        raise SystemExit
        pass
    
    elif answer == "1":
        ex1.do_get_info(ex1, ex1.name, ex1.email)
        input("\tНажмите Enter, чтобы продолжить")
        pass
    
    elif answer == "2":
        ex2.do_get_EnteredName(ex2)
        input("\tНажмите Enter, чтобы продолжить")
        pass
    
    elif answer == "3":
        ex3.do_get_RoomSquare()
        input("\tНажмите Enter, чтобы продолжить")
        pass
    
    elif answer == "4":
        ex4.do_get_LandSquare()
        input("\tНажмите Enter, чтобы продолжить")
        pass
    
    elif answer == "5":
        ex5.do_get_tax()
        input("\tНажмите Enter, чтобы продолжить")
        pass
        
    elif answer == "6":
        ex6.do_get_sum()
        input("\tНажмите Enter, чтобы продолжить")
        pass
        
    elif answer == "7":
        ex7.do_get_sum()
        input("\tНажмите Enter, чтобы продолжить")
        pass
        
    elif answer == "8":
        ex8.do_get_sum()
        input("\tНажмите Enter, чтобы продолжить")
        pass
        
    elif answer == "9":
        ex9.Total()
        input("\tНажмите Enter, чтобы продолжить")
        pass
    
    elif answer == "10":
        ex10.do_get_coordinates()
        input("\tНажмите Enter, чтобы продолжить")
        pass
    
    elif answer == "11":
        ex11.do_calculate()
        input("\tНажмите Enter, чтобы продолжить")
        pass
    
    elif answer == "12":
        ex12.do_calculate_temp()
        input("\tНажмите Enter, чтобы продолжить")
        pass
    
    elif answer == "13":
        ex13.do_convert_interval()
        input("\tНажмите Enter, чтобы продолжить")
        pass
    elif answer == "14":
        ex14.do_convert_interval()
        input("\tНажмите Enter, чтобы продолжить")
        pass
    
    elif answer == "15":
        ex15.do_show_time()
        input("\tНажмите Enter, чтобы продолжить")
        pass
    
    elif answer == "16":
        ex16.do_show_answer()
        input("\tНажмите Enter, чтобы продолжить")
        pass
    
    elif answer == "17":
        ex17.do_show_range()
        input("\tНажмите Enter, чтобы продолжить")
        pass
    pass
        
    
    
    n += 1