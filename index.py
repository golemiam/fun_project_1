import random

def main():



    random_list = []
    def char():
        int_index_one = int(random.random() * 10)
        if int_index_one == 1:
            random_two = int(random.random() * 10)
            if random_two == 1:
                random_list.append("Al")
            if random_two == 2:
                random_list.append("ph")
            if random_two == 3:
                random_list.append("a")
            if random_two == 4:
                random_list.append("Be")
            if random_two == 5:
                random_list.append("ta")
            if random_two == 6:
                random_list.append("th")
            if random_two == 7:
                random_list.append("e")
            if random_two == 8:
                random_list.append("te")
            if random_two == 9:
                random_list.append("il")
            random_list.append("!")
        elif int_index_one == 2:
            random_two = int(random.random() * 10)
            if random_two == 1:
                random_list.append("po")
            if random_two == 2:
                random_list.append("ll")
            if random_two == 3:
                random_list.append("o")
            if random_two == 4:
                random_list.append("Da")
            if random_two == 5:
                random_list.append("sh")
            if random_two == 6:
                random_list.append("en")
            if random_two == 7:
                random_list.append("sc")
            if random_two == 8:
                random_list.append("he")
            if random_two == 9:
                random_list.append("n")
            random_list.append("#")
        elif int_index_one == 3:
            random_two = int(random.random() * 10)
            if random_two == 1:
                random_list.append("@#")
            if random_two == 2:
                random_list.append("$%")
            if random_two == 3:
                random_list.append("^&")
            if random_two == 4:
                random_list.append("&*")
            if random_two == 5:
                random_list.append("()")
            if random_two == 6:
                random_list.append("_+")
            if random_two == 7:
                random_list.append("=-")
            if random_two == 8:
                random_list.append("{}")
            if random_two == 9:
                random_list.append("[]")
            random_list.append("@")
        elif int_index_one == 4:
            random_two = int(random.random() * 10)
            if random_two == 1:
                random_list.append("Je")
            if random_two == 2:
                random_list.append("su")
            if random_two == 3:
                random_list.append("sc")
            if random_two == 4:
                random_list.append("hr")
            if random_two == 5:
                random_list.append("is")
            if random_two == 6:
                random_list.append("tu")
            if random_two == 7:
                random_list.append("s")
            if random_two == 8:
                random_list.append(":;")
            if random_two == 9:
                random_list.append(",.")
            random_list.append("$")
        elif int_index_one == 5:
            random_two = int(random.random() * 10)
            if random_two == 1:
                random_list.append("?/")
            if random_two == 2:
                random_list.append("\|")
            if random_two == 3:
                random_list.append("1")
            if random_two == 4:
                random_list.append("&2")
            if random_two == 5:
                random_list.append("3")
            if random_two == 6:
                random_list.append("4")
            if random_two == 7:
                random_list.append("5")
            if random_two == 8:
                random_list.append("6")
            if random_two == 9:
                random_list.append("7")
            random_list.append("%")
        elif int_index_one == 6:
            random_two = int(random.random() * 10)
            if random_two == 1:
                random_list.append("~`")
            if random_two == 2:
                random_list.append("~")
            if random_two == 3:
                random_list.append("`")
            if random_two == 4:
                random_list.append("!")
            if random_two == 5:
                random_list.append("@")
            if random_two == 6:
                random_list.append("#")
            if random_two == 7:
                random_list.append("$")
            if random_two == 8:
                random_list.append("%")
            if random_two == 9:
                random_list.append("^")
            random_list.append("5")
        elif int_index_one == 7:
            random_two = int(random.random() * 10)
            if random_two == 1:
                random_list.append("la")
            if random_two == 2:
                random_list.append("le")
            if random_two == 3:
                random_list.append("las")
            if random_two == 4:
                random_list.append("los")
            if random_two == 5:
                random_list.append("Mog")
            if random_two == 6:
                random_list.append("lie")
            if random_two == 7:
                random_list.append("Mar")
            if random_two == 8:
                random_list.append("ito")
            if random_two == 9:
                random_list.append("mat")
            random_list.append("^")
        elif int_index_one == 8:
            random_two = int(random.random() * 10)
            if random_two == 1:
                random_list.append("ri")
            if random_two == 2:
                random_list.append("mo")
            if random_two == 3:
                random_list.append("nio")
            if random_two == 4:
                random_list.append("bene")
            if random_two == 5:
                random_list.append("frit")
            if random_two == 6:
                random_list.append("olio")
            if random_two == 7:
                random_list.append("ban")
            if random_two == 8:
                random_list.append("ana")
            if random_two == 9:
                random_list.append("blob")
            random_list.append("&")
        else:
            random_two = int(random.random() * 10)
            if random_two == 1:
                random_list.append("ri")
            if random_two == 2:
                random_list.append("mo")
            if random_two == 3:
                random_list.append("nio")
            if random_two == 4:
                random_list.append("bene")
            if random_two == 5:
                random_list.append("frit")
            if random_two == 6:
                random_list.append("olio")
            if random_two == 7:
                random_list.append("ban")
            if random_two == 8:
                random_list.append("ana")
            if random_two == 9:
                random_list.append("blob")
            random_list.append("7")
    for i in range(20):
        char()
    print(random_list)
    print(random.random() * 10)


if __name__ == '__main__':
    main()
