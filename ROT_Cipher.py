

```
#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# --author：valecalida--
# Edit time: 2020/1/30 14:26
import string
import sys
import time


def rot13():
    keys_rot13 = list((str(string.digits) + str(string.ascii_lowercase) + str(string.ascii_uppercase)))
    values_rot13 = list(string.digits) + [chr((ord(i)+13-97)%26+97) for i in string.ascii_lowercase] + [chr((ord(i)+13-65)%26+65) for i in string.ascii_uppercase]
    dict_rot13 = dict(zip(keys_rot13,values_rot13))
    res = ''
    msg = input("\t\t请输入您要加/解密的字符串：")
    try:
        for index_key in msg:
            res += dict_rot13[index_key]
    except Exception:
        print("您输入的字符串中含有非法字符，加/解密仅支持英文大小写及数字。")
    finally:
        print("\t\t\t经过ROT13加/解密之后的值是：", res,"\n")


def rot5():
    print("\t您正在使用rot5加解密")
    res = ''
    dict_rot5 = {'0': '5', '1': '6', '2': '7', '3': '8', '4': '9', '5': '0', '6': '1','7': '2', '8': '3', '9': '4'}
    msg = input("\t\t请输入您要加/解密的字符串：")
    for i in msg:
        value = ord(i)
        if (value <= 57) and (value >= 48):
            res += dict_rot5[i]
        else:
            print("您输入的字符串看起来不能用于rot5解密，请尝试一下别的操作吧。")
            break
    print("\t\t\t经过ROT5加/解密之后的值是：", res, "\n")


def rot18():
    print("\t您正在使用rot18加解密")
    res = ''
    dict_rot5 = {'0': '5', '1': '6', '2': '7', '3': '8', '4': '9', '5': '0', '6': '1','7': '2', '8': '3', '9': '4'}
    keys_rot18 = str(string.ascii_lowercase) + str(string.ascii_uppercase)
    values_rot18 = [chr((ord(i) + 13 - 97) % 26 + 97) for i in string.ascii_lowercase] + [chr((ord(i) + 13 - 65) % 26 + 65) for i in string.ascii_uppercase]
    dict_rot18 = dict((zip(keys_rot18, values_rot18)), **dict_rot5)
    msg = input("\t\t请输入您要加/解密的字符串：")
    try:
        for index_key in msg:
            res += dict_rot18[index_key]
    except Exception:
        print("您输入的字符串中含有非法字符，加/解密仅支持英文大小写及数字。")
    finally:
        print("\t\t\t经过ROT18加/解密之后的值是：", res, "\n")


def rot47():
    print("\t您正在使用rot47加解密")
    res = ''
    msg = input("\t\t请输入您要加/解密的字符串：")
    for i in msg:
        index_i = ord(i)
        if index_i < 33 or index_i >126:
            print("\t\t您的输入不在ROT47的加解密之内，请核对。")
            break
        else:
            res += chr(index_i - 47)
    print("\t\t\t经过ROT47加/解密之后的值是：", res, "\n")


def rot_menu():
    print("ROT 5/13/18/47解密程序-------Provided_by:valecalida：")
    print("\t\t1、ROT 5 加解密：")
    print("\t\t2、ROT 13 加解密：")
    print("\t\t3、ROT 18 加解密：")
    print("\t\t4、ROT 47 加解密：")
    print("\t\t5、查看ROT系列密码加密原理")
    print("\t\t0、退出本程序")



def principle():
    print("ROT5 是 rotate by 5 places 的简写，意思是旋转5个位置，其它皆同。下面分别说说它们的编码方式：")
    print("ROT5：只对数字进行编码，用当前数字往前数的第5个数字替换当前数字，例如当前为0，编码后变成5，当前为1，编码后变成6，以此类推顺序循环。")
    print("ROT13：只对字母进行编码，用当前字母往前数的第13个字母替换当前字母，例如当前为A，编码后变成N，当前为B，编码后变成O，以此类推顺序循环。")
    print("ROT18：这是一个异类，本来没有，它是将ROT5和ROT13组合在一起，为了好称呼，将其命名为ROT18。")
    print("ROT47：对数字、字母、常用符号进行编码，按照它们的ASCII值进行位置替换，用当前字符ASCII值往前数的第47位对应字符替换当前字符，例如当前为小写字母z，编码后变成大写字母K，当前为数字0，编码后变成符号_。用于ROT47编码的字符其ASCII值范围是33－126.\n")


def rot_quit():
    print("感谢使用由valecalida创建的ROT密码加解密程序")
    time.sleep(1)
    sys.exit()


def main():
    while True:
        rot_menu()
        choice = input("请选择您想要进行操作:")
        choice = choice[0]
        if choice == '1':
            rot5()
        elif choice == '2':
            rot13()
        elif choice == '3':
            rot18()
        elif choice == '4':
            rot47()
        elif choice == '5':
            principle()
        elif choice == '0':
            rot_quit()
        else:
            print("\t请确保您的输入是正确的！")


if __name__ == '__main__':
    main()
```

