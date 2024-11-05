
#Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. Hyödynnä toteutuksessa
# aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa:
# http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, request

app = Flask(__name__)
@app.route('/prime_number')
def prime_number():
    args = request.args
    number = int(args['number'])
    if number > 1:
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                answer = {"Number": number,
                          "isPrime": False}
                break
        else:
            answer = {"Number": number,
                      "isPrime": True}
    else:
        answer = {"Number": number,
                  "isPrime": False}
    return answer

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)