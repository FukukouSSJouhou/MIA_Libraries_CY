import sys
from src.MIA_Libraries_CY.KyokoLoggingkun import KyokoLoggingkun
def baseoutkun24(colorcode,text):
    r = int(colorcode[1:3], 16)
    g = int(colorcode[3:5], 16)
    b = int(colorcode[5:7], 16)
    print("\033[38;2;{};{};{}m{}\033[0m".format(r,g,b,text))
def logging_print_nocrcode(text):
    print(text)
def main():
    objkun=KyokoLoggingkun(baseoutkun24,logging_print_nocrcode)
    objkun.errout("tdn")
    print("aaaadd")
if __name__ == '__main__':
    main()