'''
Created on 15/06/2017

@author: ernesto
XXX: https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=944
'''


import logging
import sys
import fileinput

nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

def corta_palos_core(rajadas):
    la_rajita_de_canela = len(rajadas)
    matrix_shit = []
    for _ in range(la_rajita_de_canela):
        matrix_shit.append([0] * la_rajita_de_canela)
    logger_cagada.debug("la matrix es %s" % (matrix_shit))
    for io_kiero_q_m_des in [0, 1]:
        logger_cagada.debug("tamano %s de ventana" % io_kiero_q_m_des)
        for la_rajada_d_knela in range(la_rajita_de_canela - io_kiero_q_m_des):
            a_marina_l_gustaba = la_rajada_d_knela + io_kiero_q_m_des
            logger_cagada.debug("q t puedes kemar %s-%s" % (la_rajada_d_knela, a_marina_l_gustaba))
            logger_cagada.debug("es como la kndela %s-%s" % (rajadas[la_rajada_d_knela], rajadas[a_marina_l_gustaba]))
            matrix_shit[la_rajada_d_knela][a_marina_l_gustaba] = 0

    for io_kiero_q_m_des in [2]:
        logger_cagada.debug("tamano %s de ventana" % io_kiero_q_m_des)
        for la_rajada_d_knela in range(la_rajita_de_canela - io_kiero_q_m_des):
            a_marina_l_gustaba = la_rajada_d_knela + io_kiero_q_m_des
            logger_cagada.debug("q t puedes kemar %s-%s" % (la_rajada_d_knela, a_marina_l_gustaba))
            logger_cagada.debug("es como la kndela %s-%s" % (rajadas[la_rajada_d_knela], rajadas[a_marina_l_gustaba]))
            matrix_shit[la_rajada_d_knela][a_marina_l_gustaba] = rajadas[a_marina_l_gustaba] - rajadas[la_rajada_d_knela]

    logger_cagada.debug("lo q pasa s q la banda sta pendeja %s" % matrix_shit)
    for io_kiero_q_m_des in range(3, la_rajita_de_canela):
        logger_cagada.debug("tamano %s de ventana" % io_kiero_q_m_des)
        for la_rajada_d_knela in range(la_rajita_de_canela - io_kiero_q_m_des):
            a_marina_l_gustaba = la_rajada_d_knela + io_kiero_q_m_des
            logger_cagada.debug("\tq t puedes kemar %s-%s" % (la_rajada_d_knela, a_marina_l_gustaba))
            logger_cagada.debug("\tes como la kndela %s-%s" % (rajadas[la_rajada_d_knela], rajadas[a_marina_l_gustaba]))
            min_crap = sys.maxsize
            for lo_q_pasa in range(la_rajada_d_knela + 1, a_marina_l_gustaba):
                logger_cagada.debug("\t\tkiero amanecer %s" % (lo_q_pasa))
                logger_cagada.debug("\t\tbailando %s" % (rajadas[lo_q_pasa]))
                logger_cagada.debug("\t\tun tiburon kiere comer %s-%s" % (la_rajada_d_knela, lo_q_pasa))
                logger_cagada.debug("\t\tde mi peiejo %s-%s" % (lo_q_pasa, a_marina_l_gustaba))
                logger_cagada.debug("\t\tcuando io venia %s-%s" % (rajadas[la_rajada_d_knela], rajadas[lo_q_pasa]))
                logger_cagada.debug("\t\tbiajaba con mi mor %s-%s" % (rajadas[lo_q_pasa], rajadas[a_marina_l_gustaba]))
                crap = matrix_shit[la_rajada_d_knela][lo_q_pasa] + matrix_shit[lo_q_pasa][a_marina_l_gustaba]
                if(min_crap > crap):
                    min_crap = crap
            logger_cagada.debug("\tel min crap %s" % min_crap)
            matrix_shit[la_rajada_d_knela][a_marina_l_gustaba] = min_crap + (rajadas[a_marina_l_gustaba] - rajadas[la_rajada_d_knela])
    for caca in matrix_shit:
        logger_cagada.debug("ai lo q m duele %s" % (caca))
    return matrix_shit[0][-1]

def corta_palos_main():
    lineas = []
    lineas = list(fileinput.input())
    idx_linea = 0
    while True:
        tam_palote = int(lineas[idx_linea].strip())
        if(not tam_palote):
            break
        idx_linea += 1
        num_cacas = int(lineas[idx_linea].strip())
        idx_linea += 1
#        rajadas = [int(x) for x in lineas[idx_linea].strip().split(" ")]
        rajadas=[]
        for caca in lineas[idx_linea].strip().split(" "):
            if(caca and caca.isdigit()):
                rajadas.append(int(caca))
        idx_linea += 1

        logger_cagada.debug("mierda %s %s" % (num_cacas, rajadas))
        ass = corta_palos_core([0] + rajadas + [tam_palote])
        print("The minimum cutting is %u." % ass)
#     tam_palote=100
#     rajadas=[25,50,75]

#     tam_palote=10
#     rajadas=[4,5,7,8]
#    tam_palote = 1000
#    rajadas = [9, 11, 13, 51, 61, 75, 83, 85, 124, 148, 198, 209, 235, 248, 254, 290, 291, 318, 329, 356, 357, 373, 425, 427, 460, 473, 485, 516, 543, 562, 636, 683, 688, 698, 703, 704, 745, 754, 825, 826, 835, 849, 852, 867, 884, 901, 934, 970, 973, 975]
    

if __name__ == '__main__':
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(level=nivel_log, format=FORMAT)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)
    corta_palos_main()
