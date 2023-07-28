skill = [3,2,5,1,3,4]
def prod(ls):
        return ls[0]*ls[1]
def test(skill):
        n = len(skill)//2
        target = sum(skill)//n
        skill.sort()
        print(skill)
        a = []
        res = []
        i = 0
        j = len(skill) - 1
        while j > i:
                if (skill[i] + skill[j]) != target:
                        return -1
                a.append(skill[i])
                a.append(skill[j])
                res.append(a.copy())
                a.pop()
                a.pop()
                i += 1
                j -= 1
        summ = 0
        for i in range(len(res)):
                summ += prod(res[i])
        return summ
print(test(skill))