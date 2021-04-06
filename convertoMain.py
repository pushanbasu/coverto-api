import math
from flask import Flask,jsonify


def listAsString(array):
    j = ''
    for i in array:
        j += str(i)
    return j

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    return "Hello Converto!"

@app.route('/converto/<int:number>',methods=["POST","GET"])
def converto_script(number):

    def square_root(n):
        ans=round(math.sqrt(n),3)
        return ans

    def cube_root(n):
        ans = round(n**(1/3), 3)
        return ans

    def toBinary(num):

        if num > 9999999999:
            return "Sorry. Number out of range"
        else:

            resultRev = []
            while num / 2 != 0:
                resultRev.append(math.floor(num % 2))
                num = num / 2
            result = list(resultRev[:32])[-1::-1]

            return listAsString(result)

    def toOctal(num):

        if num > 9999999999:
            return "Sorry. Number out of range"
        else:

            resultRev = []
            while num / 8 !=0:
                resultRev.append(math.floor(num % 8))
                num = num / 8
            result = list(resultRev[:13])[-1::-1]

            return listAsString(result)


    def toHex(number):
        hex_dict = [
            {'sym': 'A', 'val': 10},
            {'sym': 'B', 'val': 11},
            {'sym': 'C', 'val': 12},
            {'sym': 'D', 'val': 13},
            {'sym': 'E', 'val': 14},
            {'sym': 'F', 'val': 15}
        ]
        result = []
        if number <= 0:
            print("Sorry.Only positive non-zero integers are accepted.")
        while number > 0:
            q = math.floor(number / 16)
            rem = number % 16
            if rem < 10:
                result.append(rem)
            elif rem >= 10:
                for i in hex_dict:
                    if i['val'] == rem:
                        result.append(i['sym'])

            number = q
        return listAsString(result[-1::-1])


    def toRoman(decInt):

        value_list = [
            {'sym': 'M', 'val': 1000}, {'sym': 'CM', 'val': 900}, {'sym': 'D', 'val': 500},
            {'sym': 'CD', 'val': 400}, {'sym': 'C', 'val': 100}, {'sym': 'XC', 'val': 90},
            {'sym': 'L', 'val': 50}, {'sym': 'XL', 'val': 40}, {'sym': 'X', 'val': 10},
            {'sym': 'IX', 'val': 9}, {'sym': 'V', 'val': 5}, {'sym': 'IV', 'val': 4}, {'sym': 'I', 'val': 1}
        ]



        def getSymAndRem(n):
            result = []
            cof = []

            for j in range(len(value_list)):
                c = math.floor(n / value_list[int(j)]['val'])
                if c >= 1:
                    cof.append(math.floor(n / value_list[int(j)]['val']))
                    rem = n % value_list[int(j)]['val']
                    symbol = value_list[int(j)]['sym']
                    result = [c * symbol, rem]
                    break
            return result

        arrSym = []

        x = getSymAndRem(decInt)

        while x[1] != 0:
            arrSym.append(x[0])
            y = getSymAndRem(x[1])
            x[1] = y[1]
            x[0] = y[0]
            if x[1] == 0:
                arrSym.append(x[0])
        return listAsString(arrSym)


# Calling the Functions here onwards -----------
    if number==0:
        return 'Very Sorry. Only non-zero integer input is accepted.'
    else:
        outPut={
            'Note':'You are completely welcome to get rid of those redundant 0s at the LEFT.',
            'Number_Given':number,
            'Square_root':square_root(number),
            'cube_root':cube_root(number),
            'in_Roman_Format':toRoman(number),
            'in_Binary_Format':toBinary(number),
            'in_Octal_Format':toOctal(number),
            'in_Hexadecimal_Format': toHex(number)
    }
        return jsonify(outPut)


if __name__=='__main__':
    app.run(debug=True)