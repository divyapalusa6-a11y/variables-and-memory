def challenge_01():
    apples = 1729
    oranges = 42
    papaya = apples

    print(f"Before reassignment: apples={apples}, papaya={papaya}")
    apples = apples + oranges
    print(f"After reassignment: apples={apples}, papaya={papaya}")


def challenge_02():
    apples = 1729
    oranges = 42
    bananas = [apples, oranges]

    print(f"Initially: bananas={bananas}, apples={apples}, oranges={oranges}")
    oranges = oranges + 10
    print(f"After changing oranges: bananas={bananas}, oranges={oranges}")


def challenge_03():
    apples = 1729
    oranges = 42
    bananas = [apples, oranges]

    print(f"Before helper: bananas={bananas}")
    challenge_03_helper(bananas)
    print(f"After helper: bananas={bananas}")


def challenge_03_helper(kiwis):
    mangos = 315
    kiwis.append(mangos)
    print(f"Inside helper: kiwis={kiwis}, mangos={mangos}")


def challenge_04():
    a = [1, 2]
    b = a
    print(f"Before alias mutation: a={a}, b={b}")
    b.append(3)
    print(f"After alias mutation: a={a}, b={b}")


def challenge_05():
    items = []
    print(f"Before append: items={items}")
    items.append("first")
    print(f"After append: items={items}")


def challenge_06():
    word = "apple"
    print(f"Before reassigning string: word={word}")
    word = word + "s"
    print(f"After reassigning string: word={word}")


if __name__ == "__main__":
    challenge_01()
    challenge_02()
    challenge_03()
    challenge_04()
    challenge_05()
    challenge_06()