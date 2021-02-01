from math import sqrt
from math import log
import math
from tkinter import *

# populyatsionnaya ekologiya

print("Добро пожаловать в командное окно PoStNiche v 1.0.0. \nPopulation Statistics and Niche Modeling Package")
print("Для ознакомления с основными функциями библиотеки введите - info()")

Info=str('Любые функции надо вводить со скобками, например samplesize(), А сейчас введите info() обязательно со скобками. info()')

F_criteria = {1 : 161.4, 2 : 19.0, 3 : 9.28, 4 : 6.39, 5 : 5.05, 6 : 4.28,
                    7 : 3.79, 8 : 3.44, 9 : 3.18, 10 : 2.97, 11 : 2.82,
                    12 : 2.69, 13 : 2.58, 14 : 2.48, 15 : 2.40, 16 : 2.33,
                    17 : 2.27, 18 : 2.22, 19 : 2.17, 20 : 2.12, 21 : 2.08,
                    22 : 2.05, 23 : 2.01, 24 : 1.98, 25 : 1.96, 26 : 1.93,
                    27 : 1.90, 28 : 1.88, 29 : 1.86, 30 : 1.84, 31 : 1.82,
                    32 : 1.80, 33 : 1.79, 34 : 1.77, 35 : 1.76, 36 : 1.74,
                    37 : 1.73, 38 : 1.72, 39 : 1.70, 40 : 1.69, 45 : 1.64,
                    50 : 1.60, 55 : 1.56, 60 : 1.53, 65 : 1.51, 70 : 1.49,
                    75 : 1.47, 80 : 1.45, 90 : 1.42, 100 : 1.39}

delta_coef=[0.0025, 0.0067, 0.0180, 0.0474, 0.1192, 0.2689, 0.5, 0.7311, 0.8808, 0.8808, 0.9820]
omega_coef=[0.0099, 0.0266, 0.0707, 0.1807, 0.4200, 0.7864, 1.0, 0.7864, 0.4200, 0.1807, 0.0707]

def info(): #!!!!!!!!!!!!!!!!!!!!!
    print("Добро пожаловать в информационный отдел пакета PoStNiche v 1.0.0.")
    print("В версии 1.0.0 доступны следующие функции:")
    print("\n1. samplesize(), 2. samplesize_list(), 3. projectionsize(),")
    print("4. avstat(), 5. odumindex(), 6. shannonindex(), 7. simpsonindex()")
    print("8. ginisimpsonindex(), 9. inversesimpsonindex(), 10. sorensonindex()")
    print("11. onto.delta(), 12. onto.omega(), 13. onto.deltaomega(), 14. onto.deltaomega_class()")
    print("15. onto.deltaomegas() 16. onto.deltaomegas_class(), 17. onto.deltaomegas_list()")
    print("18. onto.ontoperiodindices(), 19. onto.deltaomega_list(), 20. onto.ontoperiodindices_list()")
    print("21. onto.zhukovindices(), 22. onto.zhukovindices_list(), 23. onto.ontodistances_list()")
    print("24. onto.ontodistances(), 25. onto.populationspeed(), 26. onto.effectivedensity()")
    print("27. morpho.metric(), 28. morpho.dynamic()")
    print("\n29.niche.importdata(), 30.niche._import.matrix()")
    print("31. niche.matrixwork(), 32. niche.matrixedit()")
    print("33. niche.binary(), 34. niche.binary_model()")
    print("\n35. niche.breadth.levin(), 36.niche.breadth.levin_list()")
    print("37. niche.breadth.shannonwiener(), 38. niche.breadth.shannonwiener_list()")
    print("39. niche.breadth.smith(), 40. niche.breadth.smith_list()")
    print("\n41. niche.overlap.mcarthurlevin(), 42. niche.overlap.mcarthurlevin_list()")
    print("43. niche.overlap.pianka(), 44. niche.overlap.pianka_list()")
    print("45. niche.overlap.percentage(), 46. niche.overlap.percentage_list()")
    print("47. niche.overlap.morisita(), 48. niche.overlap.morisita_list()")
    print("49. niche.overlap.morisita_simple(), 50. niche.overlap.morisita_simple_list()")
    print("51. niche.overlap.horn(), 52. niche.overlap.horn_list()")
    print("53. niche.overlap.hurlbert(), 54. niche.overlap.hurlbert_list()")
    print("55. niche.overlap.schoener(), 56. niche.overlap.schoener_list()")
    print("57. niche.overlap.warren(), 58. niche.overlap.warren_list()")
    print("\n59. niche.cooccurrence.cscore(), 60. niche.cooccurrence.cscore_binary()")
    print("\n\n Фукнции для обучения:")
    print("\n61. study(), 62. study2(), 63. study3(), 64. study4()")
    print("\nДля начала обучения введите (!обязательно со скобками!): \nstudy()")
    
    return


def samplesize (b=0, t=1.96, e=5): 
    if b==0:
        b=int(input("Введите общее число организмов:_"))
    else:
        b==b
    a = []  
    for i in range(b):  
        new_element = float(input("Введите морфологические данные и нажмите Enter:_"))  
        a.append(new_element)
    sigma=sqrt(sum((i-(sum(a)/len(a)))**2 for i in a)/(len(a)-1))
    Variation=sigma/(sum(a)/len(a))*100
    sample= (t**2 * Variation**2)/e**2
    print("\nНеобходимый объем выборки равен:")
    print("\n", sample)
    return

def samplesize_list(list1, t=1.96, e=5):
    sigma=sqrt(sum((i-(sum(list1)/len(list1)))**2 for i in list1)/(len(list1)-1))
    Variation=sigma/(sum(list1)/len(list1))*100
    sample= (t**2 * Variation**2)/e**2
    print("\nНеобходимый объем выборки равен:")
    print("\n", sample)
    return

info_samplesize=("info_samplesize()")
def info_samplesize():
    print("\n----------------------------")
    print("samplesize(b, t=1.96, e=5)")
    print("----------------------------")
    print("\nгде b = количество организмов")
    print("t = коэффициент Стьюдента, который по умолчанию равен 1.96 (что соответсвует 95% доверитольности)")
    print("e = допустимая погрешность, по умолчанию 5% (при 95% доверительности)")
    print("\n\nДанная функция подсчитывает количество необходимого объема выборки для статистического анализа. \n\nsamplesize(*введите количество изученных организмов*), нажмите Enter. \n\nПосле этого вам предложат ввести численные показатели изучаемых морфологических признаков. Введите их по одному и нажимайте Enter. \nЕсли число не целое, дробную часть отделять точкой (например 4.2 или 5.3).")
    return

def projectionsize(a=0):
    if a==0:
        print("Используя сеточку Раменского подсчитайте проективное покрытие: одно окошечко сеточки Раменского = 10%")
        a=int(input("Введите значение проективного покрытия в процентах%"))
        if a<1:
            print("Шкала Браун-Бланке: rr=крайне редко с небольшим покрытием; \nШкала Друде: Un=в единственном экземпляре")
        elif a==1:
            print("Шкала Браун-Бланке: r=редко с небольшим покрытием; \nШкала Друде: Sol=единично")
        elif 1<a<5 or a==5:
            print("Шкала Браун-Бланке: 1=часто с небольшим покрытием или редко, но с большим покрытием,\nШкала Друде: Sp=редко")
        elif 5<a<25 or a==25:
            print("Шкала Браун-Бланке: 2=многочисленно, но покрытие меньше 1/20 поверхности; \nШкала Друде: Cop=довольно обильно")
        elif 25<a<50 or a==50:
            print("Шкала Браун-Бланке: 3=покрывает от 1/2 до 1/4 поверхности; \nШкала Друде: Cop2=обильно")
        elif 50<a<75 or a==75:
            print("Шкала Браун-Бланке: 4=покрывает от 3/4 до 1/2 поверхности; \nШкала Друде: Cop3=очень обильно")
        else:
            print("Шкала Браун-Бланке: 4=покрывает более 1/2 поверхности; \nШкала Друде: Soc=растения смыкаются надземными частями")
    else:
        if a<1:
            print("Шкала Браун-Бланке: rr=крайне редко с небольшим покрытием; \nШкала Друде: Un=в единственном экземпляре")
        elif a==1:
            print("Шкала Браун-Бланке: r=редко с небольшим покрытием; \nШкала Друде: Sol=единично")
        elif 1<a<5 or a==5:
            print("Шкала Браун-Бланке: 1=часто с небольшим покрытием или редко, но с большим покрытием,\nШкала Друде: Sp=редко")
        elif 5<a<25 or a==25:
            print("Шкала Браун-Бланке: 2=многочисленно, но покрытие меньше 1/20 поверхности; \nШкала Друде: Cop=довольно обильно")
        elif 25<a<50 or a==50:
            print("Шкала Браун-Бланке: 3=покрывает от 1/2 до 1/4 поверхности; \nШкала Друде: Cop2=обильно")
        elif 50<a<75 or a==75:
            print("Шкала Браун-Бланке: 4=покрывает от 3/4 до 1/2 поверхности; \nШкала Друде: Cop3=очень обильно")
        else:
            print("Шкала Браун-Бланке: 4=покрывает более 1/2 поверхности; \nШкала Друде: Soc=растения смыкаются надземными частями")
    return


def info_projectionsize():
    print("\n----------------------------")
    print("projectionsize(a)")
    print("----------------------------")
    print("\nгде a = значение проективного покрытия по Раневскому")
    print("\nДанная функция оценивает проеткивное покрытие популяции по шкале Браун-Бланке и шкале Друде. Для этого вам надо ввести процент проективного покрытия, который можно узнать при помощи сеточки Раневского")
    return


def avstat(b=0):
    if b==0:
        b=int(input("Введите общее число организмов:_"))
    else:
        b==b
    a = []  
    for i in range(b):  
        new_element = float(input("Введите данные и нажмите Enter:_"))
        a.append(new_element)
    srznach=sum(a)/len(a)
    sigma=sqrt(sum((i-(sum(a)/len(a)))**2 for i in a)/(len(a)-1))
    print("\nСреднее значение и его стандартное отклонение равно:\n", srznach, '±', sigma)
    return


def info_avstat():
    print("\n----------------------------")
    print("avstat(b)")
    print("----------------------------")
    print("\nгде b = общее количество организмов")
    print("\nДанная функция оценивает среднее арифметическое значение показателя и его стандартное отклонение. Эти показатели необходимы при составлении таблиц по статистике популяций. Внутри скобок указать общее количество изучаемых организмов")
    print("\n\nНазвание функции от англ. average - средний") 
    return


def odumindex (b=0):
    if b==0:
        b=int(input("Введите количество пробных площадок:_"))
    else:
        b==b
    a = []  
    for i in range(b):  
        new_element = int(input("Введите количество особей на пробной площадке и нажмите Enter:_"))  
        a.append(new_element)
    sigma=sum((i-(sum(a)/len(a)))**2 for i in a)/(len(a)-1)
    Odumindex=(sigma)/(sum(a)/len(a))
    print("Индекс Одума:")
    print(Odumindex, "\n")
    if Odumindex<1:
        ball=("равномерно")
        print("особи в популяции распределены: ", ball)
    elif Odumindex==1:
        ball=("случайным образом")
        print("особи в популяции распределены: ", ball)
    else:
        ball=("контагиозно")
        print("особи в популяции распределены: ", ball)
    if (sigma**2)>(sum(a)/len(a)):
        df=b-1
        dff=F_criteria[df]
        if dff<Odumindex:
            print("оценка типа распределения особей", ball, "распределения, статистически достоверна на уровне 95%")
        else:
            print("оценка типа распределения особей", ball, "распределения, статистически НЕ достоверна на уровне 95%")
    else:
        OdumTransverse=(sum(a)/len(a))/(sigma**2)
        df=b-1
        dff=F_criteria[df]
        if dff<OdumTransverse:
            print("оценка типа распределения особей", ball, "распределения, статистически достоверна на уровне 95%")
        else:
            print("оценка типа распределения особей", ball, "распределения, статистически НЕ достоверна на уровне 95%")
    return

def info_odumindex(): 
    print("\n----------------------------")
    print("odumindex(b)")
    print("----------------------------")
    print("\nгде b = общее количество пробных площадок")
    print("\nДанная функция оценивает характер распределения особей в популяции и дает оценку достоверности результата.")
    print("\nВ популяции укладываются несколько случайных пробных площадок, на которых учитывается число организмов изучаемого вида.")
    print("\nКоличество площадок вписывается вместо аргумента функции (b), далее в появившихся строках поочередно вводится число организмов на каждой площадке")
    return

shanonindex=("shannonindex()")
def shannonindex(b=0):
    if b==0:
        b=int(input("Введите количество видов в пробной площадке:_"))
    else:
        b==b
    a = []  
    for i in range(b):  
        new_element = int(input("Введите количество особей отдельного вида в пробной площадке и нажмите Enter:_"))  
        a.append(new_element)
    p = []
    for i in a:
        p1=i/sum(a)
        if p1!=0:
            p.append(p1)
        else:
            p1==p1
    Shannon= - sum((i*log(i)) for i in p)
    print("\nИндекс Шэннона: \n", Shannon)
    return

def info_shannonindex(): 
    print("\n----------------------------")
    print("shannonindex(b)")
    print("----------------------------")
    print("\nгде b = общее количество видов в изучаемом сообществе")
    print("\nДанная функция оценивает биоразнообразие изучаемого сообщества.")
    print("\nВ сообществе укладываются несколько случайных пробных площадок, на которых учитывается число организмов каждого вида.")
    print("\nОбщее количество видов вписывается вместо аргумента функции (b), далее в появившихся строках поочередно вводится число организмов каждого вида подсчитанных в сообществе")
    return

def simpsonindex(b=0):
    if b==0:
        b=int(input("Введите количество видов в пробной площадке:_"))
    else:
        b==b
    a = []  
    for i in range(b):  
        new_element = int(input("Введите количество особей отдельного вида в пробной площадке и нажмите Enter:_"))  
        a.append(new_element)
    p = []
    for i in a:
        p1=i/sum(a)
        p.append(p1)
    Simpson_dominance = sum(i**2 for i in p)
    print("Индекс Симпсона: \n", Simpson_dominance)
    return

def info_simpsonindex(): 
    print("\n----------------------------")
    print("simpsonindex(b)")
    print("----------------------------")
    print("\nгде b = общее количество видов в изучаемом сообществе")
    print("\nДанная функция оценивает биоразнообразие изучаемого сообщества.")
    print("\nВ сообществе укладываются несколько случайных пробных площадок, на которых учитывается число организмов каждого вида.")
    print("\nОбщее количество видов вписывается вместо аргумента функции (b), далее в появившихся строках поочередно вводится число организмов каждого вида подсчитанных в сообществе")
    return

def ginisimpsonindex(b=0):
    if b==0:
        b=int(input("Введите количество видов в пробной площадке:_"))
    else:
        b==b
    a = []  
    for i in range(b):  
        new_element = int(input("Введите количество особей отдельного вида в пробной площадке и нажмите Enter:_"))  
        a.append(new_element)
    p = []
    for i in a:
        p1=i/sum(a)
        p.append(p1)
    Gini_Simpson = 1 - sum(i**2 for i in p)
    print("Индекс Джини-Симпсона: \n", Gini_Simpson)
    return

def info_ginisimpsonindex(): 
    print("\n----------------------------")
    print("ginisimpsonindex(b)")
    print("----------------------------")
    print("\nгде b = общее количество видов в изучаемом сообществе")
    print("\nДанная функция оценивает биоразнообразие изучаемого сообщества.")
    print("\nВ сообществе укладываются несколько случайных пробных площадок, на которых учитывается число организмов каждого вида.")
    print("\nОбщее количество видов вписывается вместо аргумента функции (b), далее в появившихся строках поочередно вводится число организмов каждого вида подсчитанных в сообществе")
    return

inverssimpsonindex=("invers'E'simpsonindex(); там есть буква Е: inversesimpsonindex()")
def inversesimpsonindex(b=0):
    if b==0:
        b=int(input("Введите количество видов в пробной площадке:_"))
    else:
        b==b
    a = []  
    for i in range(b):  
        new_element = int(input("Введите количество особей отдельного вида в пробной площадке и нажмите Enter:_"))  
        a.append(new_element)
    p = []
    for i in a:
        p1=i/sum(a)
        p.append(p1)
    InverseSimpson=1/(sum(i**2 for i in p))
    print("Обратный индекс Симпсона: \n", InverseSimpson)
    return

def info_inversesimpsonindex(): 
    print("\n----------------------------")
    print("inversesimpsonindex(b)")
    print("----------------------------")
    print("\nгде b = общее количество видов в изучаемом сообществе")
    print("\nДанная функция оценивает биоразнообразие изучаемого сообщества.")
    print("\nВ сообществе укладываются несколько случайных пробных площадок, на которых учитывается число организмов каждого вида.")
    print("\nОбщее количество видов вписывается вместо аргумента функции (b), далее в появившихся строках поочередно вводится число организмов каждого вида подсчитанных в сообществе")
    return

def sorensonindex(a=0, b=0, c=0):
    if a==0 or b==0 or c==0:
        a=int(input("Введите количество видов в первом сообществе:_"))
        b=int(input("Введите количество видов во втором сообществе:_"))
        c=int(input("Введите количество видов общих для обоих сообществ:_"))
    else:
        a=a
        b=b
        c=c
    Sorenson_coefficient=(2*c)/(a+b)
    print("Коэффициент Соренсона для обоих сообществ равен: \n", Sorenson_coefficient)
    return

def info_sorensonindex(): 
    print("\n----------------------------")
    print("sorensonindex(a, b, c)")
    print("----------------------------")
    print("\nгде a = общее количество видов в изучаемом сообществе A")
    print("где b = общее количество видов в изучаемом сообществе B")
    print("где c = количество видов одинаковых для сообществ А и В")
    print("\nДанная функция оценивает схожесть двух изучаемых сообществ.")
    print("\nВ сообществах укладываются несколько случайных пробных площадок, на которых учитывается число организмов каждого вида.")
    print("\nОбщее количество видов сообщества А вписывается вместо показателя 'а' функции, общее число видов сообщества В вписывается вместо показателя 'b' функции")
    print("А количество видов одинаковых для обоих сообществ вводится вместо показателя 'c' функции")
    return

class onto():

    def delta(b=0):
        if b==0:
            b=int(input("Введите общее количество особей в ценопопуляции:_"))
        else:
            b==b
        ontolog=[]
        print("Поочередно введите количества организмов каждого онтогенетического состояния")
        print("Если данное онтогенетическое состояние не выявлено поставьте 0 и нажмите Enter")
        se=int(input("Семя (se):_"))
        ontolog.append(se)
        pl=int(input("Проросток (pl):_"))
        ontolog.append(pl)
        j=int(input("Ювенильное (j):_"))
        ontolog.append(j)
        im=int(input("Имматурное (im):_"))
        ontolog.append(im)
        v=int(input("Виргинильное (v):_"))
        ontolog.append(v)
        g1=int(input("Молодое генеративное (g1):_"))
        ontolog.append(g1)
        g2=int(input("Средне-возрастное генеративное (g2):_"))
        ontolog.append(g2)
        g3=int(input("Старое генеративное (g3):_"))
        ontolog.append(g3)
        ss=int(input("Субченильное (ss):_"))
        ontolog.append(ss)
        s=int(input("Сенильное (s):_"))
        ontolog.append(s)
        sc=int(input("Отмирающее (sc):_"))
        ontolog.append(sc)
        root=Tk()
        root.title("PoStNiche graphic")
        canvas=Canvas(root,width=260, height=240)
        canvas.pack()
        canvas.create_rectangle(0,0,270,250, fill='#fff')  
        Se=200-((se/sum(ontolog))*200)+10
        Pl=200-((pl/sum(ontolog))*200)+10
        J=200-((j/sum(ontolog))*200)+10
        Im=200-((im/sum(ontolog))*200)+10
        V=200-((v/sum(ontolog))*200)+10
        G1=200-((g1/sum(ontolog))*200)+10
        G2=200-((g2/sum(ontolog))*200)+10
        G3=200-((g3/sum(ontolog))*200)+10
        SS=200-((ss/sum(ontolog))*200)+10
        S=200-((s/sum(ontolog))*200)+10
        Sc=200-((sc/sum(ontolog))*200)+10
        canvas.create_rectangle(20,10,240,210)
        canvas.create_rectangle(25,Se,35,210, fill='black')
        canvas.create_rectangle(45,Pl,55,210, fill='black')
        canvas.create_rectangle(65,J,75,210, fill='black')
        canvas.create_rectangle(85,Im,95,210, fill='black')
        canvas.create_rectangle(105,V,115,210, fill='black')
        canvas.create_rectangle(125,G1,135,210, fill='black')
        canvas.create_rectangle(145,G2,155,210, fill='black')
        canvas.create_rectangle(165,G3,175,210, fill='black')
        canvas.create_rectangle(185,SS,195,210, fill='black')
        canvas.create_rectangle(205,S,215,210, fill='black')
        canvas.create_rectangle(225,Sc,235,210, fill='black')
        canvas.create_text(30,218,fill="black",font="Times 12 italic bold", text="se")
        canvas.create_text(50,218,fill="black",font="Times 12 italic bold", text="pl")
        canvas.create_text(70,218,fill="black",font="Times 12 italic bold", text="j")
        canvas.create_text(90,218,fill="black",font="Times 12 italic bold", text="im")
        canvas.create_text(110,218,fill="black",font="Times 12 italic bold", text="v")
        canvas.create_text(130,218,fill="black",font="Times 12 italic bold", text="g1")
        canvas.create_text(150,218,fill="black",font="Times 12 italic bold", text="g2")
        canvas.create_text(170,218,fill="black",font="Times 12 italic bold", text="g3")
        canvas.create_text(190,218,fill="black",font="Times 12 italic bold", text="ss")
        canvas.create_text(210,218,fill="black",font="Times 12 italic bold", text="s")
        canvas.create_text(230,218,fill="black",font="Times 12 italic bold", text="sc")
        canvas.create_text(10,218,fill="black",font="Times 8 italic bold", text="0")
        canvas.create_text(10,10,fill="black",font="Times 8 italic bold", text="100")
        Delta = sum(i*m for i, m in zip(ontolog, delta_coef))/sum(ontolog)
        print("\nИндекс возрастности Уранова (дельта) ценопопуляции равен: \nΔ=", Delta)
        if sum(ontolog)!=b:
            print("\n!!!Общее количество особей не совпадает с количеством введенных данных(сумма онтогенетических состояний не равна введеному количеству всех особей)")
        else:
            b==b
        return

    def omega(b=0):
        if b==0:
            b=int(input("Введите общее количество особей в ценопопуляции:_"))
        else:
            b==b
        ontolog=[]
        print("Поочередно введите количества организмов каждого онтогенетического состояния")
        print("Если данное онтогенетическое состояние не выявлено поставьте 0 и нажмите Enter")
        se=int(input("Семя (se):_"))
        ontolog.append(se)
        pl=int(input("Проросток (pl):_"))
        ontolog.append(pl)
        j=int(input("Ювенильное (j):_"))
        ontolog.append(j)
        im=int(input("Имматурное (im):_"))
        ontolog.append(im)
        v=int(input("Виргинильное (v):_"))
        ontolog.append(v)
        g1=int(input("Молодое генеративное (g1):_"))
        ontolog.append(g1)
        g2=int(input("Средне-возрастное генеративное (g2):_"))
        ontolog.append(g2)
        g3=int(input("Старое генеративное (g3):_"))
        ontolog.append(g3)
        ss=int(input("Субченильное (ss):_"))
        ontolog.append(ss)
        s=int(input("Сенильное (s):_"))
        ontolog.append(s)
        sc=int(input("Отмирающее (sc):_"))
        ontolog.append(sc)
        root=Tk()
        root.title("PoStNiche graphic")
        canvas=Canvas(root,width=260, height=240)
        canvas.pack()
        canvas.create_rectangle(0,0,270,250, fill='#fff')  
        Se=200-((se/sum(ontolog))*200)+10
        Pl=200-((pl/sum(ontolog))*200)+10
        J=200-((j/sum(ontolog))*200)+10
        Im=200-((im/sum(ontolog))*200)+10
        V=200-((v/sum(ontolog))*200)+10
        G1=200-((g1/sum(ontolog))*200)+10
        G2=200-((g2/sum(ontolog))*200)+10
        G3=200-((g3/sum(ontolog))*200)+10
        SS=200-((ss/sum(ontolog))*200)+10
        S=200-((s/sum(ontolog))*200)+10
        Sc=200-((sc/sum(ontolog))*200)+10
        canvas.create_rectangle(20,10,240,210)
        canvas.create_rectangle(25,Se,35,210, fill='black')
        canvas.create_rectangle(45,Pl,55,210, fill='black')
        canvas.create_rectangle(65,J,75,210, fill='black')
        canvas.create_rectangle(85,Im,95,210, fill='black')
        canvas.create_rectangle(105,V,115,210, fill='black')
        canvas.create_rectangle(125,G1,135,210, fill='black')
        canvas.create_rectangle(145,G2,155,210, fill='black')
        canvas.create_rectangle(165,G3,175,210, fill='black')
        canvas.create_rectangle(185,SS,195,210, fill='black')
        canvas.create_rectangle(205,S,215,210, fill='black')
        canvas.create_rectangle(225,Sc,235,210, fill='black')
        canvas.create_text(30,218,fill="black",font="Times 12 italic bold", text="se")
        canvas.create_text(50,218,fill="black",font="Times 12 italic bold", text="pl")
        canvas.create_text(70,218,fill="black",font="Times 12 italic bold", text="j")
        canvas.create_text(90,218,fill="black",font="Times 12 italic bold", text="im")
        canvas.create_text(110,218,fill="black",font="Times 12 italic bold", text="v")
        canvas.create_text(130,218,fill="black",font="Times 12 italic bold", text="g1")
        canvas.create_text(150,218,fill="black",font="Times 12 italic bold", text="g2")
        canvas.create_text(170,218,fill="black",font="Times 12 italic bold", text="g3")
        canvas.create_text(190,218,fill="black",font="Times 12 italic bold", text="ss")
        canvas.create_text(210,218,fill="black",font="Times 12 italic bold", text="s")
        canvas.create_text(230,218,fill="black",font="Times 12 italic bold", text="sc")
        canvas.create_text(10,218,fill="black",font="Times 8 italic bold", text="0")
        canvas.create_text(10,10,fill="black",font="Times 8 italic bold", text="100")
        Omega = sum(i*m for i, m in zip(ontolog, omega_coef))/sum(ontolog)
        print("\nИндекс эффективности Животовского (омега) ценопопуляции равен: \nω=", Omega)
        if sum(ontolog)!=b:
            print("\n!!!Общее количество особей не совпадает с количеством введенных данных(сумма онтогенетических состояний не равна введеному количеству всех особей)")
        else:
            b==b
        return

    def deltaomega(b=0):
        if b==0:
            b=int(input("Введите общее количество особей в ценопопуляции:_"))
        else:
            b==b
        ontolog=[]
        print("Поочередно введите количества организмов каждого онтогенетического состояния")
        print("Если данное онтогенетическое состояние не выявлено поставьте 0 и нажмите Enter")
        se=int(input("Семя (se):_"))
        ontolog.append(se)
        pl=int(input("Проросток (pl):_"))
        ontolog.append(pl)
        j=int(input("Ювенильное (j):_"))
        ontolog.append(j)
        im=int(input("Имматурное (im):_"))
        ontolog.append(im)
        v=int(input("Виргинильное (v):_"))
        ontolog.append(v)
        g1=int(input("Молодое генеративное (g1):_"))
        ontolog.append(g1)
        g2=int(input("Средне-возрастное генеративное (g2):_"))
        ontolog.append(g2)
        g3=int(input("Старое генеративное (g3):_"))
        ontolog.append(g3)
        ss=int(input("Субченильное (ss):_"))
        ontolog.append(ss)
        s=int(input("Сенильное (s):_"))
        ontolog.append(s)
        sc=int(input("Отмирающее (sc):_"))
        ontolog.append(sc)
        Omega = sum(i*m for i, m in zip(ontolog, omega_coef))/sum(ontolog)
        Delta = sum(i*m for i, m in zip(ontolog, delta_coef))/sum(ontolog)
        #table1
        root=Tk()
        root.title("PoStNiche graphic")
        canvas=Canvas(root,width=260, height=240)
        canvas.pack()
        canvas.create_rectangle(0,0,270,250, fill='#fff')  
        Se=200-((se/sum(ontolog))*200)+10
        Pl=200-((pl/sum(ontolog))*200)+10
        J=200-((j/sum(ontolog))*200)+10
        Im=200-((im/sum(ontolog))*200)+10
        V=200-((v/sum(ontolog))*200)+10
        G1=200-((g1/sum(ontolog))*200)+10
        G2=200-((g2/sum(ontolog))*200)+10
        G3=200-((g3/sum(ontolog))*200)+10
        SS=200-((ss/sum(ontolog))*200)+10
        S=200-((s/sum(ontolog))*200)+10
        Sc=200-((sc/sum(ontolog))*200)+10
        canvas.create_rectangle(20,10,240,210)
        canvas.create_rectangle(25,Se,35,210, fill='black')
        canvas.create_rectangle(45,Pl,55,210, fill='black')
        canvas.create_rectangle(65,J,75,210, fill='black')
        canvas.create_rectangle(85,Im,95,210, fill='black')
        canvas.create_rectangle(105,V,115,210, fill='black')
        canvas.create_rectangle(125,G1,135,210, fill='black')
        canvas.create_rectangle(145,G2,155,210, fill='black')
        canvas.create_rectangle(165,G3,175,210, fill='black')
        canvas.create_rectangle(185,SS,195,210, fill='black')
        canvas.create_rectangle(205,S,215,210, fill='black')
        canvas.create_rectangle(225,Sc,235,210, fill='black')
        canvas.create_text(30,218,fill="black",font="Times 12 italic bold", text="se")
        canvas.create_text(50,218,fill="black",font="Times 12 italic bold", text="pl")
        canvas.create_text(70,218,fill="black",font="Times 12 italic bold", text="j")
        canvas.create_text(90,218,fill="black",font="Times 12 italic bold", text="im")
        canvas.create_text(110,218,fill="black",font="Times 12 italic bold", text="v")
        canvas.create_text(130,218,fill="black",font="Times 12 italic bold", text="g1")
        canvas.create_text(150,218,fill="black",font="Times 12 italic bold", text="g2")
        canvas.create_text(170,218,fill="black",font="Times 12 italic bold", text="g3")
        canvas.create_text(190,218,fill="black",font="Times 12 italic bold", text="ss")
        canvas.create_text(210,218,fill="black",font="Times 12 italic bold", text="s")
        canvas.create_text(230,218,fill="black",font="Times 12 italic bold", text="sc")
        canvas.create_text(10,218,fill="black",font="Times 8 italic bold", text="0")
        canvas.create_text(10,10,fill="black",font="Times 8 italic bold", text="100")
        #table2
        root=Tk()
        root.title("PoStNiche graphic")
        canvas=Canvas(root,width=240, height=240)
        canvas.pack()
        canvas.create_rectangle(0,0,250,250, fill='#fff')
        deltaD=200-(Delta*200)+10
        omegaO=(Omega*200)+20
        delta1=0.55
        delta2=0.35
        omega1=0.6
        omega2=0.7
        Delta1=200-(delta1*200)+10
        Delta2=200-(delta2*200)+10
        Omega1=(omega1*200)+20
        Omega2=(omega2*200)+20
        canvas.create_rectangle(20, 10, Omega1, Delta1)
        canvas.create_rectangle(Omega1, 10, 230, Delta1)
        canvas.create_rectangle(20,Delta1,Omega2,Delta2)
        canvas.create_rectangle(Omega2,Delta1,230,Delta2)
        canvas.create_rectangle(20,Delta2,Omega1,220)
        canvas.create_rectangle(Omega1,Delta2,230,220)
        canvas.create_text(130,232,fill="black",font="Times 14 bold", text="ω")
        canvas.create_text(11,120,fill="black",font="Times 14 bold", text="Δ")
        canvas.create_text(15,10,fill="black",font="Times 12 bold", text="1")
        canvas.create_text(235,225,fill="black",font="Times 12 bold", text="1")
        canvas.create_text(15,225,fill="black",font="Times 12 bold", text="0")
        canvas.create_rectangle(omegaO-2,deltaD-2,omegaO+2,deltaD+2,fill="black")
        print("\nИндекс возрастности Уранова (дельта) ценопопуляции равен: \nΔ=", Delta)
        print("\nИндекс эффективности Животовского (омега) ценопопуляции равен: \nω=", Omega)
        if sum(ontolog)!=b:
            print("\n!!!Общее количество особей не совпадает с количеством введенных данных(сумма онтогенетических состояний не равна введеному количеству всех особей)")
        else:
            b==b
        print("\n")
        if Omega<0.60 and Delta<0.35:
            print("Ценопопуляция молодая")#molodoy
        elif Omega>=0.60 and Delta<0.35:
            print("Ценопопуляция зреющая")#zreyushiy
        elif Omega<0.70 and 0.35<=Delta<0.55:
            print("Ценопопуляция переходная") #perehodniy
        elif Omega>=0.70 and 0.35<=Delta<0.55:
            print("Ценопопуляция зрелая") #zreliy
        elif Omega<0.60 and Delta>=0.55:
            print("Ценопопуляция старая") #stariy
        elif Omega>0.60 and Delta>=0.55:
            print("Ценопопуляция стареющая") #stareyushiy
        else:
            print("Ошибка! Дельта и Омега числа меньше 1")
        return

    def deltaomega_class(Delta, Omega):
        root=Tk()
        root.title("PoStNiche graphic")
        canvas=Canvas(root,width=240, height=240)
        canvas.pack()
        canvas.create_rectangle(0,0,250,250, fill='#fff')
        deltaD=200-(Delta*200)+10
        omegaO=(Omega*200)+20
        delta1=0.55
        delta2=0.35
        omega1=0.6
        omega2=0.7
        Delta1=200-(delta1*200)+10
        Delta2=200-(delta2*200)+10
        Omega1=(omega1*200)+20
        Omega2=(omega2*200)+20
        canvas.create_rectangle(20, 10, Omega1, Delta1)
        canvas.create_rectangle(Omega1, 10, 230, Delta1)
        canvas.create_rectangle(20,Delta1,Omega2,Delta2)
        canvas.create_rectangle(Omega2,Delta1,230,Delta2)
        canvas.create_rectangle(20,Delta2,Omega1,220)
        canvas.create_rectangle(Omega1,Delta2,230,220)
        canvas.create_text(130,232,fill="black",font="Times 14 bold", text="ω")
        canvas.create_text(11,120,fill="black",font="Times 14 bold", text="Δ")
        canvas.create_text(15,10,fill="black",font="Times 12 bold", text="1")
        canvas.create_text(235,225,fill="black",font="Times 12 bold", text="1")
        canvas.create_text(15,225,fill="black",font="Times 12 bold", text="0")
        canvas.create_rectangle(omegaO-2,deltaD-2,omegaO+2,deltaD+2,fill="black")
        if Omega<0.60 and Delta<0.35:
            print("Ценопопуляция молодая")#molodoy
        elif 1>Omega>=0.60 and Delta<0.35:
            print("Ценопопуляция зреющая")#zreyushiy
        elif Omega<0.70 and 0.35<=Delta<0.55:
            print("Ценопопуляция переходная") #perehodniy
        elif 1>Omega>=0.70 and 0.35<=Delta<0.55:
            print("Ценопопуляция зрелая") #zreliy
        elif Omega<0.60 and 1>Delta>=0.55:
            print("Ценопопуляция старая") #stariy
        elif 1>Omega>0.60 and 1>Delta>=0.55:
            print("Ценопопуляция стареющая") #stareyushiy
        else:
            print("Ошибка! Дельта и Омега числа меньше 1")
        return

    def deltaomegas_class(b=0):
        if b==0:
            b=int(input("Введите общее количество ценопопуляций:_"))
        else:
            b==b  
        List1=[]
        List2=[]
        for i in range(b):
            Delta1=float(input("Delta:"))
            Omega1=float(input("Omega:"))
            List1.append(Omega1)
            List2.append(Delta1)
        root=Tk()
        root.title("PoStNiche graphic")
        canvas=Canvas(root,width=240, height=240)
        canvas.pack()
        canvas.create_rectangle(0,0,250,250, fill='#fff')
        delta1=0.55
        delta2=0.35
        omega1=0.6
        omega2=0.7
        Delta1=200-(delta1*200)+10
        Delta2=200-(delta2*200)+10
        Omega1=(omega1*200)+20
        Omega2=(omega2*200)+20
        canvas.create_rectangle(20, 10, Omega1, Delta1)
        canvas.create_rectangle(Omega1, 10, 230, Delta1)
        canvas.create_rectangle(20,Delta1,Omega2,Delta2)
        canvas.create_rectangle(Omega2,Delta1,230,Delta2)
        canvas.create_rectangle(20,Delta2,Omega1,220)
        canvas.create_rectangle(Omega1,Delta2,230,220)
        canvas.create_text(130,232,fill="black",font="Times 14 bold", text="ω")
        canvas.create_text(11,120,fill="black",font="Times 14 bold", text="Δ")
        canvas.create_text(15,10,fill="black",font="Times 12 bold", text="1")
        canvas.create_text(235,225,fill="black",font="Times 12 bold", text="1")
        canvas.create_text(15,225,fill="black",font="Times 12 bold", text="0")
        for p, q in zip(List1, List2):
            P=(p*200)+20
            Q=200-(q*200)+10
            canvas.create_rectangle(P-2,Q-2,P+2,Q+2,fill="black")
        return

    def deltaomegas(b=0):
        if b==0:
            b=int(input("Введите общее количество ценопопуляций:_"))
        else:
            b==b
        L=[]
        list1=[]
        for i in range(b):
            list1=list(map(int,input("Введите количество особей каждого онтогенетического состояния через запятую (без пробелов)__").split(',')))
            L.append(list1)
        Omega_list=[]
        Delta_list=[]
        for i in L:
            for p in i:
                Omega = sum(p*m for p, m in zip(i, omega_coef))/sum(i)
                Delta = sum(p*m for p, m in zip(i, delta_coef))/sum(i)
            Omega_list.append(Omega)
            Delta_list.append(Delta)
        root=Tk()
        root.title("PoStNiche graphic")
        canvas=Canvas(root,width=240, height=240)
        canvas.pack()
        canvas.create_rectangle(0,0,250,250, fill='#fff')
        delta1=0.55
        delta2=0.35
        omega1=0.6
        omega2=0.7
        Delta1=200-(delta1*200)+10
        Delta2=200-(delta2*200)+10
        Omega1=(omega1*200)+20
        Omega2=(omega2*200)+20
        canvas.create_rectangle(20, 10, Omega1, Delta1)
        canvas.create_rectangle(Omega1, 10, 230, Delta1)
        canvas.create_rectangle(20,Delta1,Omega2,Delta2)
        canvas.create_rectangle(Omega2,Delta1,230,Delta2)
        canvas.create_rectangle(20,Delta2,Omega1,220)
        canvas.create_rectangle(Omega1,Delta2,230,220)
        canvas.create_text(130,232,fill="black",font="Times 14 bold", text="ω")
        canvas.create_text(11,120,fill="black",font="Times 14 bold", text="Δ")
        canvas.create_text(15,10,fill="black",font="Times 12 bold", text="1")
        canvas.create_text(235,225,fill="black",font="Times 12 bold", text="1")
        canvas.create_text(15,225,fill="black",font="Times 12 bold", text="0")
        for Omega, Delta in zip(Omega_list, Delta_list):
            P=(Omega*200)+20
            Q=200-(Delta*200)+10
            canvas.create_rectangle(P-2,Q-2,P+2,Q+2,fill="black")
            print("\nИндекс возрастности Уранова (дельта) ценопопуляции равен: \nΔ=", Delta)
            print("Индекс эффективности Животовского (омега) ценопопуляции равен: \nω=", Omega)
            if Omega<0.60 and Delta<0.35:
                print("Ценопопуляция молодая")#molodoy
            elif 1>Omega>=0.60 and Delta<0.35:
                print("Ценопопуляция зреющая")#zreyushiy
            elif Omega<0.70 and 0.35<=Delta<0.55:
                print("Ценопопуляция переходная") #perehodniy
            elif 1>Omega>=0.70 and 0.35<=Delta<0.55:
                print("Ценопопуляция зрелая") #zreliy
            elif Omega<0.60 and 1>Delta>=0.55:
                print("Ценопопуляция старая") #stariy
            elif 1>Omega>0.60 and 1>Delta>=0.55:
                print("Ценопопуляция стареющая") #stareyushiy
            else:
                print("Ошибка! Дельта и Омега числа меньше 1")
        return

    def deltaomegas_list(List):
        Omega_list=[]
        Delta_list=[]
        for i in List:
            for p in i:
                Omega = sum(p*m for p, m in zip(i, omega_coef))/sum(i)
                Delta = sum(p*m for p, m in zip(i, delta_coef))/sum(i)
            Omega_list.append(Omega)
            Delta_list.append(Delta)
        root=Tk()
        root.title("PoStNiche graphic")
        canvas=Canvas(root,width=240, height=240)
        canvas.pack()
        canvas.create_rectangle(0,0,250,250, fill='#fff')
        delta1=0.55
        delta2=0.35
        omega1=0.6
        omega2=0.7
        Delta1=200-(delta1*200)+10
        Delta2=200-(delta2*200)+10
        Omega1=(omega1*200)+20
        Omega2=(omega2*200)+20
        canvas.create_rectangle(20, 10, Omega1, Delta1)
        canvas.create_rectangle(Omega1, 10, 230, Delta1)
        canvas.create_rectangle(20,Delta1,Omega2,Delta2)
        canvas.create_rectangle(Omega2,Delta1,230,Delta2)
        canvas.create_rectangle(20,Delta2,Omega1,220)
        canvas.create_rectangle(Omega1,Delta2,230,220)
        canvas.create_text(130,232,fill="black",font="Times 14 bold", text="ω")
        canvas.create_text(11,120,fill="black",font="Times 14 bold", text="Δ")
        canvas.create_text(15,10,fill="black",font="Times 12 bold", text="1")
        canvas.create_text(235,225,fill="black",font="Times 12 bold", text="1")
        canvas.create_text(15,225,fill="black",font="Times 12 bold", text="0")
        for Omega, Delta in zip(Omega_list, Delta_list):
            P=(Omega*200)+20
            Q=200-(Delta*200)+10
            canvas.create_rectangle(P-2,Q-2,P+2,Q+2,fill="black")
            print("\nИндекс возрастности Уранова (дельта) ценопопуляции равен: \nΔ=", Delta)
            print("Индекс эффективности Животовского (омега) ценопопуляции равен: \nω=", Omega)
            if Omega<0.60 and Delta<0.35:
                print("Ценопопуляция молодая")#molodoy
            elif 1>Omega>=0.60 and Delta<0.35:
                print("Ценопопуляция зреющая")#zreyushiy
            elif Omega<0.70 and 0.35<=Delta<0.55:
                print("Ценопопуляция переходная") #perehodniy
            elif 1>Omega>=0.70 and 0.35<=Delta<0.55:
                print("Ценопопуляция зрелая") #zreliy
            elif Omega<0.60 and 1>Delta>=0.55:
                print("Ценопопуляция старая") #stariy
            elif 1>Omega>0.60 and 1>Delta>=0.55:
                print("Ценопопуляция стареющая") #stareyushiy
            else:
                print("Ошибка! Дельта и Омега числа меньше 1")
        return

    def ontoperiodindices(b=0):
        if b==0:
            b=int(input("Введите общее количество особей в ценопопуляции:_"))
        else:
            b==b
        ontolog=[]
        print("Поочередно введите количества организмов каждого онтогенетического состояния")
        print("Если данное онтогенетическое состояние не выявлено поставьте 0 и нажмите Enter")
        j=int(input("Ювенильное (j):_"))
        ontolog.append(j)
        im=int(input("Имматурное (im):_"))
        ontolog.append(im)
        v=int(input("Виргинильное (v):_"))
        ontolog.append(v)
        g1=int(input("Молодое генеративное (g1):_"))
        ontolog.append(g1)
        g2=int(input("Средне-возрастное генеративное (g2):_"))
        ontolog.append(g2)
        g3=int(input("Старое генеративное (g3):_"))
        ontolog.append(g3)
        ss=int(input("Субченильное (ss):_"))
        ontolog.append(ss)
        s=int(input("Сенильное (s):_"))
        ontolog.append(s)
        sc=int(input("Отмирающее (sc):_"))
        ontolog.append(sc)
        Iv=sum(ontolog[0:3])/sum(ontolog)
        Ig=sum(ontolog[3:6])/sum(ontolog)
        Is=sum(ontolog[6:])/sum(ontolog)
        root=Tk()
        root.title("PoStNiche graphic")
        canvas=Canvas(root,width=260, height=240)
        canvas.pack()
        canvas.create_rectangle(0,0,270,250, fill='#fff')  
        J=200-((j/sum(ontolog))*200)+10
        Im=200-((im/sum(ontolog))*200)+10
        V=200-((v/sum(ontolog))*200)+10
        G1=200-((g1/sum(ontolog))*200)+10
        G2=200-((g2/sum(ontolog))*200)+10
        G3=200-((g3/sum(ontolog))*200)+10
        SS=200-((ss/sum(ontolog))*200)+10
        S=200-((s/sum(ontolog))*200)+10
        Sc=200-((sc/sum(ontolog))*200)+10
        canvas.create_rectangle(20,10,240,210)
        canvas.create_rectangle(65,J,75,210, fill='black')
        canvas.create_rectangle(85,Im,95,210, fill='black')
        canvas.create_rectangle(105,V,115,210, fill='black')
        canvas.create_rectangle(125,G1,135,210, fill='black')
        canvas.create_rectangle(145,G2,155,210, fill='black')
        canvas.create_rectangle(165,G3,175,210, fill='black')
        canvas.create_rectangle(185,SS,195,210, fill='black')
        canvas.create_rectangle(205,S,215,210, fill='black')
        canvas.create_rectangle(225,Sc,235,210, fill='black')
        canvas.create_text(30,218,fill="black",font="Times 12 italic bold", text="se")
        canvas.create_text(50,218,fill="black",font="Times 12 italic bold", text="pl")
        canvas.create_text(70,218,fill="black",font="Times 12 italic bold", text="j")
        canvas.create_text(90,218,fill="black",font="Times 12 italic bold", text="im")
        canvas.create_text(110,218,fill="black",font="Times 12 italic bold", text="v")
        canvas.create_text(130,218,fill="black",font="Times 12 italic bold", text="g1")
        canvas.create_text(150,218,fill="black",font="Times 12 italic bold", text="g2")
        canvas.create_text(170,218,fill="black",font="Times 12 italic bold", text="g3")
        canvas.create_text(190,218,fill="black",font="Times 12 italic bold", text="ss")
        canvas.create_text(210,218,fill="black",font="Times 12 italic bold", text="s")
        canvas.create_text(230,218,fill="black",font="Times 12 italic bold", text="sc")
        canvas.create_text(10,218,fill="black",font="Times 8 italic bold", text="0")
        canvas.create_text(10,10,fill="black",font="Times 8 italic bold", text="100")
        print("\nИндекс молодости равен: ", Iv)
        print("\nИндекс зрелости равен: ", Ig)
        print("\nИндекс старения равен: ", Is)
        return
    
    def deltaomega_list(list1):
        Omega = sum(i*m for i, m in zip(list1, omega_coef))/sum(list1)
        Delta = sum(i*m for i, m in zip(list1, delta_coef))/sum(list1)
        print("\nИндекс возрастности Уранова (дельта) ценопопуляции равен: \nΔ=", Delta)
        print("\nИндекс эффективности Животовского (омега) ценопопуляции равен: \nω=", Omega)
        print("\n")
        if Omega<0.60 and Delta<0.35:
            print("Ценопопуляция молодая")#molodoy
        elif Omega>=0.60 and Delta<0.35:
            print("Ценопопуляция зреющая")#zreyushiy
        elif Omega<0.70 and 0.35<=Delta<0.55:
            print("Ценопопуляция переходная") #perehodniy
        elif Omega>=0.70 and 0.35<=Delta<0.55:
            print("Ценопопуляция зрелая") #zreliy
        elif Omega<0.60 and Delta>=0.55:
            print("Ценопопуляция старая") #stariy
        elif Omega>0.60 and Delta>=0.55:
            print("Ценопопуляция стареющая") #stareyushiy
        else:
            print("Ошибка! Дельта и Омега числа меньше 1")
        return

    def ontoperiodindices_list(ontolog):
        Iv=sum(ontolog[0:3])/sum(ontolog)
        Ig=sum(ontolog[3:6])/sum(ontolog)
        Is=sum(ontolog[6:])/sum(ontolog)
        print("\nИндекс молодости равен: ", Iv)
        print("\nИндекс зрелости равен: ", Ig)
        print("\nИндекс старения равен: ", Is)
        return

    def zhukovindices(b=0):
        if b==0:
            b=int(input("Введите общее количество особей в ценопопуляции:_"))
        else:
            b==b
        ontolog=[]
        print("Поочередно введите количества организмов каждого онтогенетического состояния")
        print("Если данное онтогенетическое состояние не выявлено поставьте 0 и нажмите Enter")
        j=int(input("Ювенильное (j):_"))
        ontolog.append(j)
        im=int(input("Имматурное (im):_"))
        ontolog.append(im)
        v=int(input("Виргинильное (v):_"))
        ontolog.append(v)
        g1=int(input("Молодое генеративное (g1):_"))
        ontolog.append(g1)
        g2=int(input("Средне-возрастное генеративное (g2):_"))
        ontolog.append(g2)
        g3=int(input("Старое генеративное (g3):_"))
        ontolog.append(g3)
        ss=int(input("Субченильное (ss):_"))
        ontolog.append(ss)
        s=int(input("Сенильное (s):_"))
        ontolog.append(s)
        sc=int(input("Отмирающее (sc):_"))
        ontolog.append(sc)
        root=Tk()
        root.title("PoStNiche graphic")
        canvas=Canvas(root,width=260, height=240)
        canvas.pack()
        canvas.create_rectangle(0,0,270,250, fill='#fff')  
        J=200-((j/sum(ontolog))*200)+10
        Im=200-((im/sum(ontolog))*200)+10
        V=200-((v/sum(ontolog))*200)+10
        G1=200-((g1/sum(ontolog))*200)+10
        G2=200-((g2/sum(ontolog))*200)+10
        G3=200-((g3/sum(ontolog))*200)+10
        SS=200-((ss/sum(ontolog))*200)+10
        S=200-((s/sum(ontolog))*200)+10
        Sc=200-((sc/sum(ontolog))*200)+10
        canvas.create_rectangle(20,10,240,210)
        canvas.create_rectangle(65,J,75,210, fill='black')
        canvas.create_rectangle(85,Im,95,210, fill='black')
        canvas.create_rectangle(105,V,115,210, fill='black')
        canvas.create_rectangle(125,G1,135,210, fill='black')
        canvas.create_rectangle(145,G2,155,210, fill='black')
        canvas.create_rectangle(165,G3,175,210, fill='black')
        canvas.create_rectangle(185,SS,195,210, fill='black')
        canvas.create_rectangle(205,S,215,210, fill='black')
        canvas.create_rectangle(225,Sc,235,210, fill='black')
        canvas.create_text(30,218,fill="black",font="Times 12 italic bold", text="se")
        canvas.create_text(50,218,fill="black",font="Times 12 italic bold", text="pl")
        canvas.create_text(70,218,fill="black",font="Times 12 italic bold", text="j")
        canvas.create_text(90,218,fill="black",font="Times 12 italic bold", text="im")
        canvas.create_text(110,218,fill="black",font="Times 12 italic bold", text="v")
        canvas.create_text(130,218,fill="black",font="Times 12 italic bold", text="g1")
        canvas.create_text(150,218,fill="black",font="Times 12 italic bold", text="g2")
        canvas.create_text(170,218,fill="black",font="Times 12 italic bold", text="g3")
        canvas.create_text(190,218,fill="black",font="Times 12 italic bold", text="ss")
        canvas.create_text(210,218,fill="black",font="Times 12 italic bold", text="s")
        canvas.create_text(230,218,fill="black",font="Times 12 italic bold", text="sc")
        canvas.create_text(10,218,fill="black",font="Times 8 italic bold", text="0")
        canvas.create_text(10,10,fill="black",font="Times 8 italic bold", text="100")
        Ivost=sum(ontolog[0:3])/sum(ontolog[3:6])
        Izam = sum(ontolog[0:3])/sum(ontolog[3:])
        print("Индекс восстановления ценопопуляции равен: ", Ivost)
        print("Индекс замещения ценопопуляции равен: ", Izam)
        return

    def zhukovindices_list(ontolog):
        Ivost=sum(ontolog[0:3])/sum(ontolog[3:6])
        Izam = sum(ontolog[0:3])/sum(ontolog[3:])
        print("Индекс восстановления ценопопуляции равен: ", Ivost)
        print("Индекс замещения ценопопуляции равен: ", Izam)
        return

    def ontodistances_list(list1, list2):
        List1=[]
        List2=[]
        for i in list1:
            p=i/sum(list1)
            List1.append(p)
        for i in list2:
            q=i/sum(list2)
            List2.append(q)
        r=0
        for p, q in zip(List1, List2):
            c=sqrt(p*q)
            r=r+c
        print("Показатель сходства онтогенетических спектров равно: \n", r)
        return
   
    def ontodistances():
        list1=list(map(int,input("Введите количество особей каждого онтогенетического состояния через запятую (без пробелов)__").split(',')))
        list2=list(map(int,input("Введите количество особей каждого онтогенетического состояния через запятую (без пробелов)__").split(',')))
        List1=[]
        List2=[]
        for i in list1:
            p=i/sum(list1)
            List1.append(p)
        for i in list2:
            q=i/sum(list2)
            List2.append(q)
        r=0
        for p, q in zip(List1, List2):
            c=sqrt(p*q)
            r=r+c
        print("Показатель сходства онтогенетических спектров равно: \n", r)
        return

    def populationspeed(delta1=0, delta2=0, t=0):
        if delta1==0 or delta2==0 or t==0:
            delta1=float(input("Ввeдите значение Дельта1 (Δ1):_"))
            delta2=float(input("Введите значение Дельта2 (Δ2):_"))
            t=float(input("Введите интервал времени:_"))
        else:
            delta1=delta1
            delta2=delta2
            t=t
        Vdelta=(delta2-delta1)/t
        rdelta=Vdelta/delta1
        print("\nСкорость изменения онтогенетического спектра популяции равна:\n", "VΔ=", Vdelta)
        print("\nСпецифическая скорость развития ценопопуляции равна:\n", "rΔ=", rdelta)
        return      

    def effectivedensity(omega=0, M=0):
        if omega==0 or M==0:
            omega=float(input("Введите значение Омега (ω):_"))
            M=float(input("Введите физическую плотность популяции:_"))
        else:
            omega=omega
            M=M
        Me=omega*M
        print("\nЭффективная плотность популяции равна:\n", "Me=", Me)
        return

    def info_ontoperiodindices_list():
        print("\n----------------------------")
        print("ontoperiodindices_list(list)")
        print("----------------------------")
        print("\nгде list =список с количеством особей каждого онтогенетического состояния в ценопопуляции ")
        print("\nДанная функция вычисляет 1. Индекс молодости ценопопуляции, 2. Индекс зрелости ценопопуляции и 3. Индекс старения ценопопуляции")
        print("Для вычисления в аргументе функции (list1) введите заранее созданный список с количеством особей каждого онтогенетического состояния" )
        print("\n!!! В данном индексе в список долдны быть включены онтогенетические состояния в следующем порядке (если нет ввести 0):" )
        print("[j, im, v, g1, g2, g3, ss, s, sc]" )
        return
    pass


class info_onto():

    def info_effectivedensity():#!!!!!!!!!!!!!!!!!
        print("\n----------------------------")
        print("effectivedensity(omega, M)")
        print("----------------------------")
        print("\nгде omega = значение Омега (ω)")
        print("\nгде M = физическая плотность популяции")
        return
        
    def info_populationspeed():#!!!!!!!!!!!!!!!!!
        print("\n----------------------------")
        print("populationspeed(delta1, delta2, t)")
        print("----------------------------")
        print("\nгде delta1 = значение Дельта1 (Δ1)")
        print("\nгде delta2 = значение Дельта2 (Δ2)")
        print("\nгде t = интервал времени (t2-t1)")
        return

    def info_ontodistances():
        print("\n----------------------------")
        print("ontodistances()")
        print("----------------------------")
        print("\nДанная функция вычисляет показатель сходства онтогенетических спектров двух ценопопуляций")
        print("Для вычисления поочередно введите количество особей каждого онтогенетического состояния через запятую и без пробелов в появившейся строке")
        print("\n!!! Количество типов онтогенетических состояний в обоих ценопопуляциях должно быть одинаково")
        return

    def info_ontodistances_list():
        print("\n----------------------------")
        print("ontodistances_list(list1, list2)")
        print("----------------------------")
        print("\nгде list1 = список с количеством особей каждого онтогенетического состояния первой ценопопуляции")
        print("\nгде list2 = список с количеством особей каждого онтогенетического состояния второй ценопопуляции") 
        print("\nДанная функция вычисляет показатель сходства онтогенетических спектров двух ценопопуляций")
        print("Для вычисления в аргументах функции (list1, list2) введите два заранее созданных списка с количеством особей каждого онтогенетического состояния")
        print("\n!!! Количество типов онтогенетических состояний в обоих ценопопуляциях должно быть одинаково")
        return

    def info_zhukovindices_list():
        print("\n----------------------------")
        print("zhukovindices_list(list)")
        print("----------------------------")
        print("\nгде list =список с количеством особей каждого онтогенетического состояния в ценопопуляции ")
        print("\nДанная функция вычисляет 1. Индекс восстановления ценопопуляции и 2. Индекс замещения ценопопуляции")
        print("Для вычисления в аргументе функции (list1) введите заранее созданный список с количеством особей каждого онтогенетического состояния" )
        print("\n!!! В данном индексе в список долдны быть включены онтогенетические состояния в следующем порядке (если нет ввести 0):" )
        print("[j, im, v, g1, g2, g3, ss, s, sc]" )
        return

    def info_zhukovindices():
        print("\n----------------------------")
        print("zhukovindices(b)")
        print("----------------------------")
        print("\nгде b = общее количество особей в ценопопуляции")
        print("\nДанная функция вычисляет 1. Индекс восстановления ценопопуляции и 2. Индекс замещения ценопопуляции")
        print("Для вычисления поочередно введите количество особей каждого онтогенетического состояния в появившихся строках" )
        return

    def info_deltaomega_list():
        print("\n----------------------------")
        print("deltaomega_list(list)")
        print("----------------------------")
        print("\nгде list =список с количеством особей каждого онтогенетического состояния в ценопопуляции ")
        print("\nДанная функция вычисляет 1. Индекс возратсности Уранова (дельта), 2. Индекс эффективности Животновского (омега) и 3. Классифицирует ценопопуляцию по системе Дельта-Омега")
        print("Для вычисления в аргументе функции (list1) введите заранее созданный список с количеством особей каждого онтогенетического состояния" )
        print("\n!!! В данном индексе в список долдны быть включены онтогенетические состояния в следующем порядке (если нет ввести 0):" )
        print("[se, pl, j, im, v, g1, g2, g3, ss, s, sc]" )
        return

    def info_ontoperiodindices():
        print("\n----------------------------")
        print("ontoperiodindices(b)")
        print("----------------------------")
        print("\nгде b = общее количество особей в ценопопуляции")
        print("\nДанная функция вычисляет 1. Индекс молодости ценопопуляции, 2. Индекс зрелости ценопопуляции и 3. Индекс старения ценопопуляции")
        print("Для вычисления поочередно введите количество особей каждого онтогенетического состояния в появившихся строках" )
        return

    def info_deltaomegas_class():
        print("\n----------------------------")
        print("deltaomegas_class(b)")
        print("----------------------------")
        print("\nгде b = общее количество ценопопуляций")
        print("\nДанная функция классифицирует ценопопуляции и рисует их график по системе Дельта-Омега")
        print("\nДля вычисления введите соотвествующие показатели Дельта и Омега (Delta, Omega)")
        return

    def info_deltaomegas():
        print("\n----------------------------")
        print("deltaomegas(b)")
        print("----------------------------")
        print("\nгде b = общее количество ценопопуляций")
        print("\nДанная функция классифицирует ценопопуляции и рисует их график по системе Дельта-Омега")
        return

    def info_deltaomegas_list():
        print("\n----------------------------")
        print("deltaomegas_list(List)")
        print("----------------------------")
        print("\nгде List = вложенный список со значениями онтогенетических показателей разных ценопопуляций")
        print("\nДанная функция классифицирует ценопопуляции и рисует их график по системе Дельта-Омега")
        return

    def info_deltaomega_class():
        print("\n----------------------------")
        print("deltaomega_class(Delta, Omega)")
        print("----------------------------")
        print("\nгде Delta = показатель Дельта Уранова")
        print("\nгде Omega = показатель Омега Животновского")
        print("\nДанная функция классифицирует ценопопуляцию и создает график по системе Дельта-Омега")
        print("\nДля вычисления введите соотвествующие показатели Дельта и Омега вместо аргументов функции (Delta, Omega)")
        return

    def info_deltaomega():
        print("\n----------------------------")
        print("deltaomega(b)")
        print("----------------------------")
        print("\nгде b = общее количество особей в ценопопуляции")
        print("\nДанная функция вычисляет 1. Индекс возратсности Уранова (дельта), 2. Индекс эффективности Животновского (омега) и 3. Классифицирует ценопопуляцию по системе Дельта-Омега")
        print("Для вычисления поочередно введите количество особей каждого онтогенетического состояния в появившихся строках" )
        return

    def info_omega():
        print("\n----------------------------")
        print("omega(b)")
        print("----------------------------")
        print("\nгде b = общее количество особей в ценопопуляции")
        print("\nДанная функция вычисляет Индекс эффективности Животновского (омега)")
        print("Для вычисления поочередно введите количество особей каждого онтогенетического состояния в появившихся строках" )
        return

    def info_delta():
        print("\n----------------------------")
        print("delta(b)")
        print("----------------------------")
        print("\nгде b = общее количество особей в ценопопуляции")
        print("\nДанная функция вычисляет Индекс возратсности Уранова (дельта)")
        print("Для вычисления поочередно введите количество особей каждого онтогенетического состояния в появившихся строках" )
        return
    pass


class morpho():

    def metric():
        W=float(input("Общая фитомасса растений (грамм):_"))
        WL=float(input("Фитомасса листьев (грамм):_"))
        h=float(input("Высота (см):_"))
        WG=float(input("Фитомасса репродуктивных органов (грамм):_"))
        NL=int(input("Число листьев (штук):_"))
        NFl=int(input("Число цветков (штук):_"))
        NFr=int(input("Число плодов (штук):_"))
        A=float(input("Листовая поверхность (квадратные см):_"))
        Al=float(input("Площадь отдельного листа (квадратные см):_"))
        D=float(input("Диаметр стебля (см):_"))
        LWR=WL/W #fotosintetich usilie
        S0=sqrt(A)/(round(WL**(1/3)))
        SLA=A/WL
        LAR=A/W
        RE1=(WG/W)*100
        RE2=(WG/A)*100
        print("Фотосинтетическое усилие равно: ", LWR, "грамм/грамм")
        print("Удельная поверхность листьев равна: ", S0, "См^2/г")
        print("Площадь листьев на единицу фитомассы листьев: ", SLA, "См^2/г")
        print("Площадь листьев на единицу фитомассы растения: ", LAR, "См^2/г")
        print("Репродуктивное усилие RE1: ", RE1, "%")
        print("Репродуктивное усилие RE2: ", RE2, "%")
        return

    def dynamic():
        W1=float(input("Общая фитомасса растения W1 (грамм):_"))
        W2=float(input("Общая фитомасса растения W2 (грамм):_"))
        A1=float(input("Листовая поверхность A1 (кв.см):_"))
        A2=float(input("Листовая поверхность A2 (кв.см):_"))
        T=float(input("Промежуток времени Т (сутки):_"))
        AGR=(W2-W1)/T
        AGRA=(A2-A1)/T
        RGR=(log(W2)-log(W1))/T
        RGRA=(log(A2)-log(A1))/T
        NAR=((W2-W1)/T)*((log(A2)-log(A1))/(A2-A1))
        LARI=((A2-A1)/T)*((log(W2)-log(W1))/(W2-W1))
        print("Абсолютная скорость роста: ", AGR, "гр/сутки")
        print("Абсолютная скорость формирования листовой поверхности: ", AGRA, "кв.см/сутки")
        print("Относительная скорость роста: ", RGR, "гр/гр/сутки")
        print("Относительная скоротсь формирования листовой поверхности ", RGRA, "кв.см/кв.см/сутки")
        print("Нетто-ассимиляция: ", NAR, "гр/кв.см/сутки")
        print("Производительность формирования листьев: ", LARI, "кв.см/гр/сутки")
        return
    pass

class info_morpho():
    
    def metric():
        print("\n----------------------------")
        print("postniche.morpho.metric()")
        print("----------------------------")
        print("\nВычисляет аллометрические морфометрические показатели:")
        print("Фотосинтетическое усилие")
        print("Удельная поверхность листьев")
        print("Площадь листьев на единицу фитомассы листьев")
        print("Площадь листьев на единицу фитомассы растения")
        print("Репродуктивное усилие RE1")
        print("Репродуктивное усилие RE2")
        return

    def dynamic():
        print("\n----------------------------")
        print("postniche.morpho.dynamic()")
        print("----------------------------")
        print("\nВычисляет динамические морфометрические показатели:")
        print("Абсолютная скорость роста")
        print("Абсолютная скорость формирования листовой поверхности")
        print("Относительная скорость роста")
        print("Относительная скоротсь формирования листовой поверхности")
        print("Нетто-ассимиляция")
        print("Производительность формирования листьев")
        return
        
#classes
class niche():

    def importdata(a):
        if a==None:
            a=str(input("Введите месторасположение файла:__"))
        else:
            a=a
        with open(a) as f:
            matrix = [list(map(float, row.split())) for row in f.readlines()]
        return matrix

    class _import():

        def matrix(a):
            if a==None:
                a=str(input("Введите месторасположение файла:__"))
            else:
                a=a
            with open(a) as f:
                matrix = [list(map(float, row.split())) for row in f.readlines()]
            nothing, A = zip(*matrix)
            return A
        pass
       

    def matrixwork(list1):
        nothing, A = zip(*list1)
        return A

    def matrixedit(list1):
        A=[]
        for i in list1:
            if type(i)==str:
                A.append(0)
            else:
                A.append(i)
        return A

    def binary (list1, threshold):
        La=[]
        for i in list1:
            if i>=threshold:
                La.append(1)
            else:
                La.append(0)
        return La

    def binary_model (list1, threshold):
        La=[]
        for i in list1:
            if i>=threshold:
                La.append(i)
            else:
                La.append(0)
        return La


        #classes
    class cooccurrence():
        
        def cscore(list1, list2, threshold1=0, threshold2=0): #!!!!!!!!!!!!!!!!!!!!!!!
            if threshold1==0 or threshold2==0:
                threshold1=float(input("threshold1:"))
                threshold2=float(input("threshold2:"))
            else:
                threshold1=threshold1
                threshold2=threshold2
            List1=[]
            List2=[]
            for p, q in zip(list1, list2):
                if p>=threshold1:
                    List1.append(1)
                else:
                    List1.append(0)
                if q>=threshold2:
                    List2.append(1)
                else:
                    List2.append(0)
            CC=0
            for p, q in zip(List1, List2):
                if p==q==1:
                    CC=CC+1
                else:
                    CC=CC+0
            r1=0
            r2=0
            for p, q in zip(List1, List2):
                if p!=q and p==1:
                    r1=r1+1
                elif q!=p and q==1:
                    r2=r2+1
                else:
                    r1=r1+0
                    r2=r2+0
            Cscore=(r1-CC)*(r2-CC)
            Cscore_standart=((r1-CC)*(r2-CC))/(r1+r2-CC)
            print("Chekerboard score = ", Cscore)
            print("Standartized Chekerboard score = ", Cscore_standart)
            return

        def cscore_binary(list1, list2):#!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            CC=0
            for p, q in zip(list1, list2):
                if p==q==1:
                    CC=CC+1
                else:
                    CC=CC+0
            r1=0
            r2=0
            for p, q in zip(list1, list2):
                if p!=q and p==1:
                    r1=r1+1
                elif q!=p and q==1:
                    r2=r2+1
                else:
                    r1=r1+0
                    r2=r2+0
            Cscore=(r1-CC)*(r2-CC)
            print("\nChekerboard score = ", Cscore)
            try:
                Cscore_standart=((r1-CC)*(r2-CC))/(r1+r2-CC)
                print("Standartized Chekerboard score = ", Cscore_standart)
            except ZeroDivisionError:
                print("Standartized Chekerbord Index деление на ноль")
            return

            
    class breadth():

        def levin(a=0):
            if a==0:
                a=int(input("Введите количество экологических уровней"))
            else:
                a=a
            L=[]
            for i in range(a):  
                new_element = int(input("Введите количество особей на данном экологическом уровне и нажмите Enter:_"))  
                L.append(new_element)
            La=[]
            for i in L:
                p=i/sum(L)
                La.append(p)
            Levin=1/sum(p**2 for p in La)
            LevinStandart=(Levin-1)/(len(La)-1)
            print("\nШирота экологической ниши по индексу Левинa равна: \nLevin's Measure=", Levin)
            print("\nШирота экологической ниши по стандантизированному индексу Левинa равна: \nStandartized Levin's Measure=", LevinStandart)
            return

        def levin_list(list1):
            La=[]
            for i in list1:
                c=i/sum(list1)
                La.append(c)
            Levin=1/sum(p**2 for p in La)
            LevinStandart=(Levin-1)/(len(La)-1)
            print("\nШирота экологической ниши по индексу Левинa равна: \nLevin's Measure=", Levin)
            print("\nШирота экологической ниши по стандантизированному индексу Левинa равна: \nStandartized Levin's Measure=", LevinStandart)
            return

        def shannonwiener(a=0):
            if a==0:
                a=int(input("Введите количество экологических уровней"))
            else:
                a=a
            L=[]
            for i in range(a):  
                new_element = int(input("Введите количество особей на данном экологическом уровне и нажмите Enter:_"))  
                L.append(new_element)
            La=[]
            for i in L:
                if i!=0:
                    p=i/sum(L)
                    La.append(p)
                else:
                    a=a
            Shannon_Wiener = -sum(p*log(p) for p in La)
            Standart = Shannon_Wiener/log(a)
            print("\nШирота экологической ниши по индексу Шэннона-Вьенера равна: \nShannon-Wiener Measure=", Shannon_Wiener, " nits/individual")
            print("\nШирота экологической ниши по стандантизированному индексу Шэннона-Вьенера равна:\nStandartized Shannon-Wiener Measure=", Standart)
            return

        def shannonwiener_list(list1):
            La=[]
            for i in list1:
                if i!=0:
                    c=i/sum(list1)
                    La.append(c)
                else:
                    i=i
            Shannon_Wiener = -sum(p*log(p) for p in La)
            Standart = Shannon_Wiener/log(len(La))
            print("\nШирота экологической ниши по индексу Шэннона-Вьенера равна: \nShannon-Wiener Measure=", Shannon_Wiener, "nits/individual")
            print("\nШирота экологической ниши по стандантизированному индексу Шэннона-Вьенера равна:\nStandartized Shannon-Wiener Measure=", Standart)
            return

        def smith(a=0):
            if a==0:
                a=int(input("Введите количество экологических уровней"))
            else:
                a=a
            L=[]
            for i in range(a):  
                new_element = int(input("Введите количество особей на данном экологическом уровне и нажмите Enter:_"))  
                L.append(new_element)
            La=[]
            for i in L:
                o=i/sum(L)
                La.append(o)
            aj=float(1/a)
            Smith=sum(sqrt(aj*p) for p in La)
            LowerSmith=math.sin(math.asin(Smith) - 1.96/(2*sqrt(sum(L))))
            UpperSmith=math.sin(math.asin(Smith) + 1.96/(2*sqrt(sum(L))))
            print("\nШирота экологической ниши по индексу Смита равна: \nSmith's Measure=", Smith)
            print("\n Smith=", LowerSmith, "-", UpperSmith, "(LowerSmith to UpperSmith)")
            return

        def smith_list(list1):
            La=[]
            for i in list1:
                o=i/sum(list1)
                La.append(o)
            aj=float(1/len(La))
            Smith=sum(sqrt(aj*p) for p in La)
            LowerSmith=math.sin(math.asin(Smith) - 1.96/(2*sqrt(sum(list1))))
            UpperSmith=math.sin(math.asin(Smith) + 1.96/(2*sqrt(sum(list1))))
            print("\nШирота экологической ниши по индексу Смита равна: \nSmith's Measure=", Smith)
            print("\n Smith=", LowerSmith, "-", UpperSmith, "(LowerSmith to UpperSmith)")
            return

        pass

    class overlap():

        def mcarthurlevin(a=0):
            if a==0:
                a=int(input("Введите количество экологических уровней"))
            else:
                a=a
            list1=list(map(int,input("Введите количество особей первого вида через запятую (без пробелов)__").split(',')))
            list2=list(map(int,input("Введите количество особей второго вида через запятую (без пробелов)__").split(',')))
            List1=[]
            List2=[]
            for p, q in zip(list1, list2):
                p1=p/sum(list1)
                List1.append(p1)
                q1=q/sum(list2)
                List2.append(q1)
            if len(list1)!=a or len(list2)!=a:
                print("\n!!! ВВЕДЕННЫЕ ДАННЫЕ НЕ СОВПАДАЮТ, ВОЗМОЖНО ДОПУЩЕНА ОШИБКА !!!")
            else:
                a=a
            MacArthur_Levin_forS1=sum(p*q for p, q in zip(List1, List2))/sum(p**2 for p in List1)
            MacArthur_Levin_forS2=sum(p*q for p, q in zip(List1, List2))/sum(q**2 for q in List2)
            print("\nПерекрещивание экологической ниши по индексу МакАртура-Левина для первого вида равно: ", MacArthur_Levin_forS1)
            print("\nПерекрещивание экологической ниши по индексу МакАртура-Левина для второго вида равно: ", MacArthur_Levin_forS2)
            return 

        def mcarthurlevin_list(list1, list2):
            List1=[]
            List2=[]
            for p, q in zip(list1, list2):
                p1=p/sum(list1)
                List1.append(p1)
                q1=q/sum(list2)
                List2.append(q1)
            MacArthur_Levin_forS1=sum(p*q for p, q in zip(List1, List2))/sum(p**2 for p in List1)
            MacArthur_Levin_forS2=sum(p*q for p, q in zip(List1, List2))/sum(q**2 for q in List2)
            print("\nПерекрещивание экологической ниши по индексу МакАртура-Левина для первого вида равно: ", MacArthur_Levin_forS1)
            print("\nПерекрещивание экологической ниши по индексу МакАртура-Левина для второго вида равно: ", MacArthur_Levin_forS2)
            return 

        def pianka(a=0):
            if a==0:
                a=int(input("Введите количество экологических уровней"))
            else:
                a=a
            list1=list(map(int,input("Введите количество особей первого вида через запятую (без пробелов)__").split(',')))
            list2=list(map(int,input("Введите количество особей второго вида через запятую (без пробелов)__").split(',')))
            List1=[]
            List2=[]
            for p, q in zip(list1, list2):
                p1=p/sum(list1)
                List1.append(p1)
                q1=q/sum(list2)
                List2.append(q1)
            if len(list1)!=a or len(list2)!=a:
                print("\n!!! ВВЕДЕННЫЕ ДАННЫЕ НЕ СОВПАДАЮТ, ВОЗМОЖНО ДОПУЩЕНА ОШИБКА !!!")
            else:
                a=a
            Pianka=sum(p*q for p, q in zip(List1, List2))/sqrt(sum(p**2 for p in List1)*sum(q**2 for q in List2))
            print("\nПерекрещивание экологической ниши по индексу Пьянки равно: ", Pianka)
            return 

        def pianka_list(list1, list2):
            List1=[]
            List2=[]
            for p, q in zip(list1, list2):
                p1=p/sum(list1)
                List1.append(p1)
                q1=q/sum(list2)
                List2.append(q1)
            Pianka=sum(p*q for p, q in zip(List1, List2))/sqrt(sum(p**2 for p in List1)*sum(q**2 for q in List2))
            print("\nПерекрещивание экологической ниши по индексу Пьянки равно: ", Pianka)
            return 

        def percentage(a=0):
            if a==0:
                a=int(input("Введите количество экологических уровней"))
            else:
                a=a
            list1=list(map(int,input("Введите количество особей первого вида через запятую (без пробелов)__").split(',')))
            list2=list(map(int,input("Введите количество особей второго вида через запятую (без пробелов)__").split(',')))
            List1=[]
            List2=[]
            for p, q in zip(list1, list2):
                p1=p/sum(list1)
                List1.append(p1)
                q1=q/sum(list2)
                List2.append(q1)
            if len(list1)!=a or len(list2)!=a:
                print("\n!!! ВВЕДЕННЫЕ ДАННЫЕ НЕ СОВПАДАЮТ, ВОЗМОЖНО ДОПУЩЕНА ОШИБКА !!!")
            else:
                a=a
            percentage=sum(min(p, q) for p, q in zip(List1, List2))*100
            print("Процентное перекрещивание экологических ниш равно: ", percentage)
            return 

        def percentage_list(list1, list2):
            List1=[]
            List2=[]
            for p, q in zip(list1, list2):
                p1=p/sum(list1)
                List1.append(p1)
                q1=q/sum(list2)
                List2.append(q1)
            percentage=sum(min(p, q) for p, q in zip(List1, List2))*100
            print("Процентное перекрещивание экологических ниш равно: ", percentage)
            return

        def morisita(a=0):
            if a==0:
                a=int(input("Введите количество экологических уровней"))
            else:
                a=a
            list1=list(map(int,input("Введите количество особей первого вида через запятую (без пробелов)__").split(',')))
            list2=list(map(int,input("Введите количество особей второго вида через запятую (без пробелов)__").split(',')))
            List1=[]
            List2=[]
            for p, q in zip(list1, list2):
                p1=p/sum(list1)
                List1.append(p1)
                q1=q/sum(list2)
                List2.append(q1)
            if len(list1)!=a or len(list2)!=a:
                print("\n!!! ВВЕДЕННЫЕ ДАННЫЕ НЕ СОВПАДАЮТ, ВОЗМОЖНО ДОПУЩЕНА ОШИБКА !!!")
            else:
                a=a
            pp1=[]
            qq1=[]
            for n in list1:
                pp=(n-1)/(sum(list1)-1)
                pp1.append(pp)
            for n in list2:
                qq=(n-1)/(sum(list2)-1)
                qq1.append(qq)
            Morista=(2*sum(p*q for p, q in zip(List1, List2)))/((sum(p*pp for p, pp in zip(List1, pp1)))+(sum(q*qq for q, qq in zip(List2, qq1))))
            print("\nПерекрещивание экологической ниши по индексу Мористы равно:", Morista)
            return

        def morisita_list(list1, list2):
            List1=[]
            List2=[]
            for p, q in zip(list1, list2):
                p1=p/sum(list1)
                List1.append(p1)
                q1=q/sum(list2)
                List2.append(q1)
            pp1=[]
            qq1=[]
            for n in list1:
                pp=(n-1)/(sum(list1)-1)
                pp1.append(pp)
            for n in list2:
                qq=(n-1)/(sum(list2)-1)
                qq1.append(qq)
            Morista=(2*sum(p*q for p, q in zip(List1, List2)))/((sum(p*pp for p, pp in zip(List1, pp1)))+(sum(q*qq for q, qq in zip(List2, qq1))))
            print("\nПерекрещивание экологической ниши по индексу Мористы равно:", Morista)
            return 

        def morisita_simple(a=0):
            if a==0:
                a=int(input("Введите количество экологических уровней"))
            else:
                a=a
            list1=list(map(int,input("Введите количество особей первого вида через запятую (без пробелов)__").split(',')))
            list2=list(map(int,input("Введите количество особей второго вида через запятую (без пробелов)__").split(',')))
            List1=[]
            List2=[]
            for p, q in zip(list1, list2):
                p1=p/sum(list1)
                List1.append(p1)
                q1=q/sum(list2)
                List2.append(q1)
            if len(list1)!=a or len(list2)!=a:
                print("\n!!! ВВЕДЕННЫЕ ДАННЫЕ НЕ СОВПАДАЮТ, ВОЗМОЖНО ДОПУЩЕНА ОШИБКА !!!")
            else:
                a=a
            Morista=(2*sum(p*q for p, q in zip(List1, List2)))/(sum(p**2 for p in List1)+sum(q**2 for q in List2))
            print("Перекрещивание экологической ниши по упрощенному индексу Мористы равно: \n", Morista)
            return 

        def morisita_simple_list(list1, list2):
            List1=[]
            List2=[]
            for p, q in zip(list1, list2):
                p1=p/sum(list1)
                List1.append(p1)
                q1=q/sum(list2)
                List2.append(q1)
            Morista=(2*sum(p*q for p, q in zip(List1, List2)))/(sum(p**2 for p in List1)+sum(q**2 for q in List2))
            print("Перекрещивание экологической ниши по упрощенному индексу Мористы равно: \n", Morista)
            return

        def horn(a=0):
            if a==0:
                a=int(input("Введите количество экологических уровней"))
            else:
                a=a
            list1=list(map(int,input("Введите количество особей в разных экологических уровнях первого вида через запятую (без пробелов)__").split(',')))
            list2=list(map(int,input("Введите количество особей в разных экологических уровнях второго вида через запятую (без пробелов)__").split(',')))
            List1=[]
            List2=[]
            List0=[]
            List00=[]
            for p in list1:
                if p!=0:
                    p1=p/sum(list1)
                    List1.append(p1)
                    List0.append(p1)
                else:
                    List1.append(0)
                    List0.append(1)
            for q in list2:
                if q!=0:
                    q1=q/sum(list2)
                    List2.append(q1)
                    List00.append(q1)
                else:
                    List2.append(0)
                    List00.append(1)
            if len(list1)!=a or len(list2)!=a:
                print("\n!!! ВВЕДЕННЫЕ ДАННЫЕ НЕ СОВПАДАЮТ, ВОЗМОЖНО ДОПУЩЕНА ОШИБКА !!!")
            else:
                a=a         
            S=0
            Sp=0
            Sq=0
            for p, q, a, b in zip(List1,List2, List0, List00):
                c=(p+q)*(log((p+q)))
                S=S+c
                pp=p*log(a)
                Sp=Sp+pp
                qq=q*log(b)
                Sq=Sq+qq
            Horn=(S-Sp-Sq)/(2*log(2))
            print("Перекрещивание экологической ниши по индексу Хорна равно: \n", Horn)
            return

        def horn_list(list1, list2):
            List1=[]
            List2=[]
            List0=[]
            List00=[]
            for p in list1:
                if p!=0:
                    p1=p/sum(list1)
                    List1.append(p1)
                    List0.append(p1)
                else:
                    List1.append(0)
                    List0.append(1)
            for q in list2:
                if q!=0:
                    q1=q/sum(list2)
                    List2.append(q1)
                    List00.append(q1)
                else:
                    List2.append(0)
                    List00.append(1)                  
            S=0
            Sp=0
            Sq=0
            for p, q, a, b in zip(List1,List2, List0, List00):
                c=(p+q)*(log((p+q)))
                S=S+c
                pp=p*log(a)
                Sp=Sp+pp
                qq=q*log(b)
                Sq=Sq+qq
            Horn=(S-Sp-Sq)/(2*log(2))
            print("Перекрещивание экологической ниши по индексу Хорна равно: \n", Horn)
            return

        def hurlbert(a=0):
            if a==0:
                a=int(input("Введите количество экологических уровней"))
            else:
                a=a
            list1=list(map(int,input("Введите количество особей первого вида через запятую (без пробелов)__").split(',')))
            list2=list(map(int,input("Введите количество особей второго вида через запятую (без пробелов)__").split(',')))
            List1=[]
            List2=[]
            Ai=[]
            for p, q in zip(list1, list2):
                p1=p/sum(list1)
                List1.append(p1)
                q1=q/sum(list2)
                List2.append(q1)
                A=1/len(list1)
                Ai.append(A)
            if len(list1)!=a or len(list2)!=a:
                print("\n!!! ВВЕДЕННЫЕ ДАННЫЕ НЕ СОВПАДАЮТ, ВОЗМОЖНО ДОПУЩЕНА ОШИБКА !!!")
            else:
                a=a
            Hulbert=sum(p*q/a for p, q, a in zip(List1, List2, Ai))
            print("Перекрещивание экологической ниши по индексу Хурльберта равно: \n", Hulbert)
            return

        def hurlbert_list(list1, list2):
            List1=[]
            List2=[]
            Ai=[]
            for p, q in zip(list1, list2):
                p1=p/sum(list1)
                List1.append(p1)
                q1=q/sum(list2)
                List2.append(q1)
                A=1/len(list1)
                Ai.append(A)
            Hulbert=sum(p*q/a for p, q, a in zip(List1, List2, Ai))
            print("Перекрещивание экологической ниши по индексу Хурльберта равно: \n", Hulbert)
            return
        
        def schoener(a=0):
            if a==0:
                a=int(input("Введите количество экологических уровней:_"))
            else:
                a=a
            list1=list(map(int,input("Введите количество особей первого вида через запятую (без пробелов)__").split(',')))
            list2=list(map(int,input("Введите количество особей второго вида через запятую (без пробелов)__").split(',')))
            List1=[]
            List2=[]
            for p, q in zip(list1, list2):
                p1=p/sum(list1)
                List1.append(p1)
                q1=q/sum(list2)
                List2.append(q1)
            if len(list1)!=a or len(list2)!=a:
                print("\n!!! ВВЕДЕННЫЕ ДАННЫЕ НЕ СОВПАДАЮТ, ВОЗМОЖНО ДОПУЩЕНА ОШИБКА !!!")
            else:
                a=a
            SchoenerD=1-(0.5*sum([abs(a-b) for a, b in zip(List1, List2)]))
            print("Перекрещивание экологической ниши по индексу 'Schoener D' равно: \n", SchoenerD)
            return

        def schoener_list(list1, list2):
            List1=[]
            List2=[]
            for p, q in zip(list1, list2):
                p1=p/sum(list1)
                List1.append(p1)
                q1=q/sum(list2)
                List2.append(q1)
            SchoenerD=1-(0.5*sum([abs(a-b) for a, b in zip(List1, List2)]))
            print("Перекрещивание экологической ниши по индексу 'Schoener D' равно: \n", SchoenerD)
            return

        def warren(a=0):
            if a==0:
                a=int(input("Введите количество экологических уровней:_"))
            else:
                a=a
            list1=list(map(int,input("Введите количество особей первого вида через запятую (без пробелов)__").split(',')))
            list2=list(map(int,input("Введите количество особей второго вида через запятую (без пробелов)__").split(',')))
            List1=[]
            List2=[]
            for p, q in zip(list1, list2):
                p1=p/sum(list1)
                List1.append(p1)
                q1=q/sum(list2)
                List2.append(q1)
            if len(list1)!=a or len(list2)!=a:
                print("\n!!! ВВЕДЕННЫЕ ДАННЫЕ НЕ СОВПАДАЮТ, ВОЗМОЖНО ДОПУЩЕНА ОШИБКА !!!")
            else:
                a=a
            Hellinger=sqrt(sum([(sqrt(p)-sqrt(q))**2 for p, q in zip (List1, List2)]))
            WarrenI=1-((Hellinger**2)/2)
            print("Hellinger Distance = ", Hellinger)
            print("Перекрещивание экологической ниши по индексу 'Warren I' равно: \n", WarrenI)
            return

        def warren_list(list1, list2):
            List1=[]
            List2=[]
            for p, q in zip(list1, list2):
                p1=p/sum(list1)
                List1.append(p1)
                q1=q/sum(list2)
                List2.append(q1)
            Hellinger=sqrt(sum([(sqrt(p)-sqrt(q))**2 for p, q in zip (List1, List2)]))
            WarrenI=1-((Hellinger**2)/2)
            print("Hellinger Distance = ", Hellinger)
            print("Перекрещивание экологической ниши по индексу 'Warren I' равно: \n", WarrenI)
            return

#info-classes
class info_niche():

    def importdata():
        print("\n------------------------------")
        print("niche.importdata(a)")
        print("------------------------------")
        print("\nгде a = расположение файла")
        print("\nДанная функция импортирует текстовый файл в программу")
        return

    class _import():
        def matrix():
            print("\n------------------------------")
            print("niche.-import.matrix(a)")
            print("------------------------------")
            print("\nгде a = расположение файла")
            print("\nДанная функция импортирует текстовый файл в программу")
            return

    def binary():
        print("\n------------------------------")
        print("niche.binary(list1, threshold)")
        print("------------------------------")
        print("\nгде list = заранее приготовленный список со значениями распределения вида в экологических уровнях или матрицы MaxEnt")
        print("\nгде threshold = индикатор presense/absense в результатах анализа MaxEnt (10% threshold или другие)")
        print("\nДанная функция перерабатывает в биномиальный тип (1/0) заранее приготовленный список или матрицу из карты MaxEnt по пороговой величине (threshold)")
        print("\nРезультат функции: (биномиальный список), выйдет если вызвать")
        print("\nСоздать новый список, и присвоить ему значение niche.binary(list1, threshold)")
        print("\nНапример:\n NewList=niche.binary(List, threshold)\n")
        return

    def binary_model():
        print("\n-----------------------------------")
        print("niche.binary_model(list1, threshold)")
        print("------------------------------------")
        print("\nгде list = заранее приготовленный список со значениями распределения вида в экологических уровнях или матрицы MaxEnt")
        print("\nгде threshold = индикатор presense/absense в результатах анализа MaxEnt (10% threshold или другие)")
        print("\nДанная функция обнуляет все значения заранее приготовленного списка или матрицы из карты MaxEnt ниже пороговой величины (threshold)")
        print("\nРезультат функции: (новый список (i/0)), выйдет если вызвать")
        print("\nСоздать новый список, и присвоить ему значение niche.binary_model(list1, threshold)")
        print("\nНапример:\n NewList=niche.binary_model(List, threshold)\n")
        return
    pass
      
    class breadth():

        def levin():
            print("\n----------------------------")
            print("niche.breadth.levin(a)")
            print("----------------------------")
            print("\nгде a = количество экологических уровней вида")
            print("\nДанная функция определяет широту экологической ниши по индексу Левина")
            print("\nРезультат функции: 1. Индекс Левина, 2. Стандартизированный индекс Левина")
            return

        def levin_list():
            print("\n-----------------------------")
            print("niche.breadth.levin_list(list)")
            print("-----------------------------")
            print("\nгде list = список со значениями распределения вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nДанная функция определяет широту экологической ниши по индексу Левина на основе заранее приготовленного списка или матрицы из карты MaxEnt")
            print("\nРезультат функции: 1. Индекс Левина, 2. Стандартизированный индекс Левина")
            return

        def shannonwiener():
            print("\n-----------------------------")
            print("niche.breadth.shannonwiener(a)")
            print("-----------------------------")
            print("\nгде a = количество экологических уровней вида")
            print("\nДанная функция определяет широту экологической ниши по индексу Шэннона-Вьенера")
            print("\nРезультат функции: 1. Индекс Шэннона-Вьенера, 2. Стандартизированный индекс Шэннона-Вьенера")
            return

        def shannonwiener_list():
            print("\n-------------------------------------")
            print("niche.breadth.shannonwiener_list(list)")
            print("--------------------------------------")
            print("\nгде list = список со значениями распределения вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nДанная функция определяет широту экологической ниши по индексу Шэннона-Вьенера на основе заранее приготовленного списка или матрицы из карты MaxEnt")
            print("\nРезультат функции: 1. Индекс Шэннона-Вьенера, 2. Стандартизированный индекс Шэннона-Вьенера")
            return

        def smith():
            print("\n----------------------------")
            print("niche.breadth.smith(a)")
            print("----------------------------")
            print("\nгде a = количество экологических уровней вида")
            print("\nДанная функция определяет широту экологической ниши по индексу Смита")
            print("\nРезультат функции: 1. Индекс Смита, 2. Нижний и верхний пределы индекса Смита")
            return

        def smith_list():
            print("\n-----------------------------")
            print("niche.breadth.smith_list(list)")
            print("-----------------------------")
            print("\nгде list = список со значениями распределения вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nДанная функция определяет широту экологической ниши по индексу Смита на основе заранее приготовленного списка или матрицы из карты MaxEnt")
            print("\nРезультат функции: 1. Индекс Смита, 2. Нижний и верхний пределы индекса Смита")
            return
        pass

    class overlap():

        def mcarthurlevin():
            print("\n-----------------------------")
            print("niche.overlap.mcarthurlevin(a)")
            print("-----------------------------")
            print("\nгде a = общее количество экологических уровней видов")
            print("\nДанная функция определяет перекрещивание экологических ниш по индексу МакАртура-Левина")
            print("\nРезультат функции: 1. Индекс МакАртура-Левина для первого вида, 2. Индекс МакАртура-Левина для второго вида")
            return

        def mcarthurlevin_list():
            print("\n-----------------------------")
            print("niche.overlap.mcarthurlevin_list(list)")
            print("-----------------------------")
            print("\nгде list1 = список со значениями распределения первого вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nгде list2 = список со значениями распределения второго вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nДанная функция определяет перекрещивание экологических ниш по индексу МакАртура-Левина на основе заранее приготовленного списка или матрицы из карты MaxEnt")
            print("\nРезультат функции: 1. Индекс МакАртура-Левина для первого вида, 2. Индекс МакАртура-Левина для второго вида")
            return

        def pianka():
            print("\n-----------------------------")
            print("niche.overlap.pianka(a)")
            print("-----------------------------")
            print("\nгде a = общее количество экологических уровней видов")
            print("\nДанная функция определяет перекрещивание экологических ниш по индексу МакАртура-Левина модифицированному Пьянкой")
            print("\nРезультат функции: 1. Индекс Пьянки")
            return

        def pianka_list():
            print("\n-----------------------------")
            print("niche.overlap.pianka_list(list1, list2)")
            print("-----------------------------")
            print("\nгде list1 = список со значениями распределения первого вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nгде list2 = список со значениями распределения второго вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nДанная функция определяет перекрещивание экологических ниш по индексу МакАртура-Левина модифицированному Пьянкойна основе заранее приготовленного списка или матрицы из карты MaxEnt ")
            print("\nРезультат функции: 1. Индекс Пьянки")
            return

        def percentage():
            print("\n-----------------------------")
            print("niche.overlap.percentage(a)")
            print("-----------------------------")
            print("\nгде a = общее количество экологических уровней видов")
            print("\nДанная функция определяет процентное перекрещивание экологических ниш")
            print("\nРезультат функции: 1. процентное перекрещивание экологических ниш")
            return

        def percentage_list():
            print("\n-----------------------------")
            print("niche.overlap.percentage_list(list1, list2)")
            print("-----------------------------")
            print("\nгде list1 = список со значениями распределения первого вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nгде list2 = список со значениями распределения второго вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nДанная функция определяет процентное перекрещивание экологических ниш на основе заранее приготовленного списка или матрицы из карты MaxEnt")
            print("\nРезультат функции: 1. процентное перекрещивание экологических ниш")
            return

        def morisita():
            print("\n-----------------------------")
            print("niche.overlap.morisita(a)")
            print("-----------------------------")
            print("\nгде a = общее количество экологических уровней видов")
            print("\nДанная функция определяет перекрещивание экологических ниш по индексу Мористы")
            print("\nРезультат функции: 1. перекрещивание экологических ниш по индексу Мористы")
            return
        
        def morisita_list():
            print("\n-----------------------------")
            print("niche.overlap.morisita_list(list1, list2)")
            print("-----------------------------")
            print("\nгде list1 = список со значениями распределения первого вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nгде list2 = список со значениями распределения второго вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nДанная функция определяет перекрещивание экологических ниш по индексу Мористы на основе заранее приготовленного списка или матрицы из карты MaxEnt")
            print("\nРезультат функции: 1. перекрещивание экологических ниш по индексу Мористы")
            return

        def morisita_simple():
            print("\n-----------------------------")
            print("niche.overlap.morisita_simple(a)")
            print("-----------------------------")
            print("\nгде a = общее количество экологических уровней видов")
            print("\nДанная функция определяет перекрещивание экологических ниш по упрощенному индексу Мористы")
            print("\nРезультат функции: 1. перекрещивание экологических ниш по упрощенному индексу Мористы")
            return

        def morisita_simple_list():
            print("\n-----------------------------")
            print("niche.overlap.morisita_simple_list(list1, list2)")
            print("-----------------------------")
            print("\nгде list1 = список со значениями распределения первого вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nгде list2 = список со значениями распределения второго вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nДанная функция определяет перекрещивание экологических ниш по упрощенному индексу Мористы на основе заранее приготовленного списка или матрицы из карты MaxEnt")
            print("\nРезультат функции: 1. перекрещивание экологических ниш по упрощенному индексу Мористы")
            return

        def horn():
            print("\n-----------------------------")
            print("niche.overlap.horn(a)")
            print("-----------------------------")
            print("\nгде a = общее количество экологических уровней видов")
            print("\nДанная функция определяет перекрещивание экологических ниш по индексу Хорна")
            print("\nРезультат функции: 1. перекрещивание экологических ниш по индексу Хорна")
            return

        def horn_list():
            print("\n-----------------------------")
            print("niche.overlap.horn_list(list1, list2)")
            print("-----------------------------")
            print("\nгде list1 = список со значениями распределения первого вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nгде list2 = список со значениями распределения второго вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nДанная функция определяет перекрещивание экологических ниш по упрощенному индексу Хорна на основе заранее приготовленного списка или матрицы из карты MaxEnt")
            print("\nРезультат функции: 1. перекрещивание экологических ниш по упрощенному индексу Хорна")
            return

        def hurlbert():
            print("\n-----------------------------")
            print("niche.overlap.hurlbert(a)")
            print("-----------------------------")
            print("\nгде a = общее количество экологических уровней видов")
            print("\nДанная функция определяет перекрещивание экологических ниш по индексу Хурльберта")
            print("\nРезультат функции: 1. перекрещивание экологических ниш по индексу Хурльберта")
            return

        def hurlbert_list():
            print("\n-----------------------------")
            print("niche.overlap.hurlbert_list(list1, list2)")
            print("-----------------------------")
            print("\nгде list1 = список со значениями распределения первого вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nгде list2 = список со значениями распределения второго вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nДанная функция определяет перекрещивание экологических ниш по упрощенному индексу Хурльберта на основе заранее приготовленного списка или матрицы из карты MaxEnt")
            print("\nРезультат функции: 1. перекрещивание экологических ниш по упрощенному индексу Хурльберта")
            return
 
        def schoener():
            print("\n-----------------------------")
            print("niche.overlap.schoener(a)")
            print("-----------------------------")
            print("\nгде a = общее количество экологических уровней видов")
            print("\nДанная функция определяет показатель 'D' перекрещивание экологических ниш по Schoener")
            print("\nРезультат функции: 1. показатель перекрещивания экологических ниш Shoener D")
            return

        def schoener_list():
            print("\n-----------------------------")
            print("niche.overlap.hurlbert_list(list1, list2)")
            print("-----------------------------")
            print("\nгде list1 = список со значениями распределения первого вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nгде list2 = список со значениями распределения второго вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nДанная функция определяет показатель 'D' перекрещивание экологических ниш по Schoener на основе заранее приготовленного списка или матрицы из карты MaxEnt")
            print("\nРезультат функции: 1. показатель перекрещивания экологических ниш Shoener D")
            return

        def warren():
            print("\n-----------------------------")
            print("niche.overlap.schoener(a)")
            print("-----------------------------")
            print("\nгде a = общее количество экологических уровней видов")
            print("\nДанная функция определяет показатель 'I' перекрещивание экологических ниш по Warren")
            print("\nРезультат функции: 1. показатель перекрещивания экологических ниш Warren I, 2. Дистанции Хэллингера")
            return

        def warren_list():
            print("\n-----------------------------")
            print("niche.overlap.hurlbert_list(list1, list2)")
            print("-----------------------------")
            print("\nгде list1 = список со значениями распределения первого вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nгде list2 = список со значениями распределения второго вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nДанная функция определяет показатель 'I' перекрещивание экологических ниш по Warren на основе заранее приготовленного списка или матрицы из карты MaxEnt")
            print("\nРезультат функции: 1. показатель перекрещивания экологических ниш Warren I, 2. Дистанции Хэллингера")
            return
        pass

    class cooccurrence():

        def cscore():
            print("\n--------------------------------------------------------------")
            print("niche.cooccurrence.cscore(list1, list2, threshold1, threshold2)")
            print("---------------------------------------------------------------")
            print("\nгде list1 = список со значениями распределения первого вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nгде list2 = список со значениями распределения второго вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nгде threshold1 = индикатор presense/absense в результатах анализа MaxEnt (10% threshold или другие) для первого вида")
            print("\nгде threshold2 = индикатор presense/absense в результатах анализа MaxEnt (10% threshold или другие) для второго вида")
            print("\nДанная функция определяет показатель взаимовстречаемости двух видов С-score (Chekerboard score) на основе заранее приготовленного списка или матрицы из карты MaxEnt")
            print("\nРезультат функции: 1. показатель взаимовстречаемости двух видов С-score (Chekerboard score)")
            return

        def cscore_binary():
            print("\n---------------------------------------------")
            print("niche.cooccurrence.cscore_binary(list1, list2)")
            print("----------------------------------------------")
            print("\nгде list1 = бинарный список со значениями распределения первого вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nгде list2 = бинарный список со значениями распределения второго вида в экологических уровнях (вводить через запятую, без пробела)")
            print("\nДанная функция определяет показатель взаимовстречаемости двух видов С-score (Chekerboard score) на основе заранее приготовленного бинарного списка")
            print("\nРезультат функции: 1. показатель взаимовстречаемости двух видов С-score (Chekerboard score)")
            print("\n!!!Бинарный список готовится на основе матрицы Maxent при помощи функции: \n\nniche.binary()\n")
            return
        pass
    pass
pass


Study=("Все функции вводятся со скобками: введите study()")
def study():
    print("Добро пожаловать в учебный модуль PoStNiche v 1.0.0")
    print("Здесь Вы можете ознакомится с основными функциями нашей программы. \nА сейчас введите внизу цифру 1 чтобы продолжить")
    a=int(input(">>>"))
    while a!=1:
        print("Упс, вы ввели что-то не то! Введите 1")
        a=int(input(">>>"))
    else:
        print("Отлично")
    print("Модуль PoStNiche работает в программе Python, в коммандном окне, которого вы сейчас находитесь")
    print("Python - язык программирования. В самом простом виде он может вычислять разные арифметические действия:")
    print("Сложить два числа можно используя знак +: например введите внизу 1+1")
    a=str(input(">>>"))
    while a!='1+1':
        print("Упс, вы ввели что-то не то! Введите 1+1")
        a=str(input(">>>"))
    else:
        print(">>>",2)
        print("\nОтлично!")
    print("Чтобы отнять одно число от другого используйте '-'. Введите внизу: 2-1")
    a=str(input(">>>"))
    while a!='2-1':
        print("Упс, вы ввели что-то не то! Введите 2-1")
        a=str(input(">>>"))
    else:
        print(">>>",1)
        print("\nОтлично!")
    print("Для умножения используется оператор '*'. Введите 3*3")
    a=str(input(">>>"))
    while a!='3*3':
        print("Упс, вы ввели что-то не то! Введите 3*3")
        a=str(input(">>>"))
    else:
        print(">>>",9)
        print("\nОтлично!")
    print("Для деления используется оператор '/'. Введите 12/3")
    a=str(input(">>>"))
    while a!='12/3':
        print("Упс, вы ввели что-то не то! Введите 12/3")
        a=str(input(">>>"))
    else:
        print(">>>",4)
        print("\nОтлично!")
    print("В Python можно сохранять числа в каких-то переменных, например в переменной 'a'.")
    print("Для этого надо дать переменной 'а' значение числа")
    print("Чтобы это сделать используется оператор '='. Если вы введете а=5, то значение переменной 'а' будет равно 5")
    print("Введите: a=5")
    a=str(input(">>>"))
    while a!='a=5':
        print("Упс, вы ввели что-то не то! Введите a=5, используя клавиатуру на английском языке")
        a=str(input(">>>"))
    else:
        print(">>>")
    print("\nТеперь создайте переменную 'b' со значением равным 6")
    b=str(input(">>>"))
    while b!='b=6':
        print("Упс, вы ввели что-то не то! Введите b=6, используя клавиатуру на английском языке")
        b=str(input(">>>"))
    else:
        print(">>>")
    print("\nА теперь прибавьте переменную 'а' к переменной 'b', и посмотрите что получится")
    c=str(input(">>>"))
    while c!='a+b':
        print("Упс, вы ввели что-то не то! Введите a+b, используя клавиатуру на английском языке")
        c=str(input(">>>"))
    else:
        print(">>>", 11)
        print("\nВау! Вышел ответ для 5+6, которые хранились в переменных а+b")
    print("\nПоздравляем вы прошли 1 урок, для продолжения обучения введите: \nstudy2() обязательно со скобками")
    return

def study2():
    print("В переменной можно сохранять также дробные числа в десятичной форме \n(9.1234, 10.15211 и тд)")
    print("Дробные числа в Python пишутся с точкой. \nТочка разделяет целую часть от десятичной (!!не запятая!!)")
    print("Правильно: 1.23, Неправильно: 1,23")
    print("Введите дробное число: 1.23")
    a=float(input(">>>"))
    while a!=1.23:
        print("Упс, вы ввели что-то не то! Введите дробное число через точку 1.23")
        a=float(input(">>>"))
    else:
        print(">>>")
    print("Отлично!")
    print("Присвоение переменной дробного числа такое же как и для целых (а=5.63)")
    print("Сложение, вычитание, умножение, деление для дробных чисел такое же как и для целых")
    print("Создайте переменную 'а' со значением 4.5, \nпотом умножьте 'а' на 6 и разделите на 3")
    a=str(input(">>>"))
    while a!='a=4.5':
        print("Упс, вы ввели что-то не то! Введите a=4.5")
        a=str(input(">>>"))
    a=str(input(">>>"))
    while a!='a*6/3':
        print("Упс, вы ввели что-то не то! Введите a*6/3")
        a=str(input(">>>"))
    else:
        print(">>>9")
    print("\nОтлично")
    print("Одна переменная может быть равна другой. Например, с=а")
    print("Создайте переменную 'С' (с большой буквы) и приравняйте ее к 'a'")
    a=str(input(">>>"))
    while a!='C=a':
        print("Упс, вы ввели что-то не то! Введите C=a")
        a=str(input(">>>"))
    else:
        print(">>>")
    print("Создавая переменную, можно проводить действия со старой переменной")
    print("Например запись 'C=a+5.5' означает что новая переменная С равна а(4.5)+5.5, \nв результате новая переменная С будет равна сумме 4.5 и 5.5")
    print("Создайте переменную С, равной произведению переменной 'a' и числа 2")
    a=str(input(">>>"))
    while a!='C=a*2':
        print("Упс, вы ввели что-то не то! Введите C=a*2")
        a=str(input(">>>"))
    else:
        print(">>>")
    print("Чтобы увидеть значение новой переменной, просто введите ее название")
    print("Введите имя переменной С")
    a=str(input(">>>"))
    while a!='C':
        print("Упс, вы ввели что-то не то! Введите C")
        a=str(input(">>>"))
    else:
        print(">>>9")
    print("\nОтлично!")
    print("Если вы заметили, переменная С и с разные. Язык программирования Python обращает внимание на регистр. \nТак что будьте внимательны. Чтобы перейти на следующий урок введите: \nstudy3() обязательно со скобками")
    return

def study3():
    print("В Python одной переменной можно передать несколько значений")
    print("Одним из способов сделать это - является создание списка")
    print("В Python списки могут хранить в себе несколько значений от слов до чисел")
    print("В самом простом виде списки выглядят так: \n\nList=[1,0,56.1,82]")
    print("\nВ данном случае элементами списка являются четыре числа: '1' '0' '56.1' '82'")
    print("Обратите внимание в списке элементы разделяются запятыми, точка определяет конец целой части для дробных чисел")
    print("Через запятую и без пробелов введите 4 элемента списка: '9' '8' '7' '6'")
    a=str(input(">>>"))
    while a!='9,8,7,6':
        print("Упс, вы ввели что-то не то! Введите 9,8,7,6")
        a=str(input(">>>"))
    else:
        print(">>>")
    print("\nЧтобы создать список нам нужно передать значение списка одной переменной, например переменной А")
    print("Для этого после знака '=' введите элементы списка внутри квадратных скобок [] через запятую и без пробелов")
    print("Создайте список А с элементами 5, 6, 7, 18")
    a=str(input(">>>"))
    while a!='A=[5,6,7,18]':
        print("Упс, вы ввели что-то не то! Введите A=[5,6,7,18], используя клавиатуру на английском языке")
        a=str(input(">>>"))
    else:
        print(">>>")
    print("Отлично, чтобы увидеть список просто введите его название, в нашем случае А")
    print("Введите А")
    a=str(input(">>>"))
    while a!="A":
        print("Упс, вы ввели что-то не то! Введите A, используя клавиатуру на английском языке")
        a=str(input(">>>"))
    else:
        print(">>>[5,6,7,18]")
    print("\nОтлично")
    print("Можно узнать количество элементов списка введя len(A), \nlen - специальная функция, \nА - ее аргумент, в нашем случае список А")
    print("Введите len(A):")
    a=str(input(">>>"))
    while a!='len(A)':
        print("Упс, вы ввели что-то не то! Введите len(A), используя клавиатуру на английском языке")
        a=str(input(">>>"))
    else:
        print(">>>4")
    print("\nОтлично")
    print("Чтобы узнать сумму всех элементов списка введите sum(A), \nsum - специальная функция, \nА - ее аргумент, в нашем случае список А") 
    print("Введите sum(A):")
    a=str(input(">>>"))
    while a!='sum(A)':
        print("Упс, вы ввели что-то не то! Введите sum(A), используя клавиатуру на английском языке")
        a=str(input(">>>"))
    else:
        print(">>>36")
    print("\nОтлично, Вы узнали основные методы работы со списками на языке программирования Python, \nтеперь можно начать знакомится с функциями программы PoStNiche, \nдля этого study4()")

def study4():
    print("\n--------------------------------------------------------------------------------")
    print("\n                                   ФУНКЦИИ                                      ")
    print("\n--------------------------------------------------------------------------------")
    print("\nОсновными элементами работы модуля PoStNiche являются функции:")
    print("Вы уже знакомы с функциями: info(), study(), len(), sum()")
    print("Функция выполняет определенный алгоритм действий, \nкоторый был в ней запрограммирован")
    print("Всякая функция заканчивается скобками, \nбез скобок работать с функцией не получится")
    print("Например функция avstat() высчитывает среднюю арифметическую \nвсех введенных данных и среднеквадратичное отклонение (±)")
    print("Введите avstat()")
    a=str(input(">>>"))
    while a!='avstat()':
        print("Упс, вы ввели что-то не то! Введите avstat()")
        a=str(input(">>>"))
    b=int(input("Введите общее число организмов:_"))
    a = []  
    for i in range(b):  
        new_element = float(input("Введите данные и нажмите Enter:_"))
        a.append(new_element)
    srznach=sum(a)/len(a)
    sigma=sqrt(sum((i-(sum(a)/len(a)))**2 for i in a)/(len(a)-1))
    print("\nСреднее значение и его стандартное отклонение равно:\n", srznach, '±', sigma)
    print("\nВсю информацию о функции можно написав info_ перед названием функции: \ninfo_avstat()")
    print("Узнайте информацию о функции avstat()")
    a=str(input(">>>"))
    while a!='info_avstat()':
        print("Упс, вы ввели что-то не то! Введите info_avstat()")
        a=str(input(">>>"))
    print("\n----------------------------")
    print("avstat(b)")
    print("----------------------------")
    print("\nгде b = общее количество организмов")
    print("\nДанная функция оценивает среднее арифметическое значение показателя и его стандартное отклонение. Эти показатели необходимы при составлении таблиц по статистике популяций. Внутри скобок указать общее количество изучаемых организмов")
    print("\nНазвание функции от англ. average - средний")
    print("\n\nВнутри скобок у функций находятся аргументы. В основном в модуле PoStNiche функции можно использовать без аргумента, оставляя скобки пустыми, ну а для удобства конесно же можно вводить функции с аргументами.")
    print("Например агрументом функции avstat(b) является b = общее количество организмов. Если вы хотите узнать среднее арифметическое 4 организмов просто введите avstat(4)")
    print("Введите avstat(4):")
    a=str(input(">>>"))
    while a!='avstat(4)':
        print("Упс, вы ввели что-то не то! Введите avstat(4)")
        a=str(input(">>>"))
    a = []  
    for i in range(4):  
        new_element = float(input("Введите данные и нажмите Enter:_"))
        a.append(new_element)
    srznach=sum(a)/len(a)
    sigma=sqrt(sum((i-(sum(a)/len(a)))**2 for i in a)/(len(a)-1))
    print("\nСреднее значение и его стандартное отклонение равно:\n", srznach, '±', sigma)
    print("\n--------------------------------------------------------------------------------")
    print("\n--------------------------------------------------------------------------------")
    print("ПОЗДРАВЛЯЕМ!!! ВЫ ЗАВЕРШИЛИ НАЧАЛЬНОЕ ОБУЧЕНИЕ И ИМЕЕТЕ ВСЕ НАВЫКИ ДЛЯ")
    print("ИСПОЛЬЗОВАНИЯ МОДУЛЯ POSTNICHE В PYTHON. ВСЕ ДОПОЛЬНИТЕЛЬНУЮ ИНФОРМАЦИЮ")
    print("О ФУНКЦИЯХ ВЫ МОЖЕТЕ ПОЛУЧИТЬ О КАЖДОЙ ФУНКЦИИ ИСПОЛЬЗУЯ info_функция()")
    print("А ТАКЖЕ В ОСНОВНОЙ ДОКУМЕНТАЦИИ МОДУЛЯ. УДАЧНОЙ РАБОТЫ")
    return

def cyte():
    print("Цитировать модуль PoStNiche слудует так:")
    print("")




