def funcOne():
    funcTwo()
    print("One")
                             # when Function One is called within stack function 1 is created then function 2 is called it comes above function 1 in stack it
                             # calls function 3 and it is created above function 2 now first function 3 is executed first and it is poped and it goes one and
                             # stack will become empty when completely excecuted see using Run and Debug

def funcTwo():
    funcThree()
    print("Two")

def funcThree():
    print("Three")

funcOne()
