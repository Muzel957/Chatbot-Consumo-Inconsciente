
from flask import Flask, render_template, request

app = Flask(__name__)

def classificar_consumo(consumo, media):
    if consumo <= media * 0.9: return "baixo"
    elif consumo <= media: return "na_media"
    else: return "alto"

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            pessoas = int(request.form.get('pessoas', 1))
            agua_total = float(request.form.get('agua', 0))
            energia_total = float(request.form.get('energia', 0))
            tentou = request.form.get('tentou_economizar')

            # Médias de referência (Região Sudeste)
            media_agua = 5.0
            media_energia = 120.0
            c_agua_pp = agua_total / pessoas
            c_energia_pp = energia_total / pessoas

            # --- LÓGICA ÁGUA ---
            status_a = classificar_consumo(c_agua_pp, media_agua)
            diag_agua = ""
            dicas_agua = []

            if status_a == "baixo":
                diag_agua = "Parabéns! Seu consumo de água está abaixo da média. Você é um exemplo de sustentabilidade!"
            elif status_a == "na_media":
                diag_agua = "Você está na média da sua região para consumo de água. Continue assim!"
            else:
                diag_agua = "Seu consumo de água está muito alto em comparação com a média da sua região."
                if tentou == "sim":
                    dicas_agua = ["Instale redutores de vazão em chuveiros e torneiras", "Instale sistemas de reaproveitamento de água de chuva", "Monitore o hidrômetro para detectar vazamentos ocultos"]
                else:
                    dicas_agua = ["Feche a torneira ao escovar os dentes", "Conserte vazamentos visíveis", "Reaproveite água da máquina de lavar", "Tome banhos de até 5 minutos"]

            # --- LÓGICA ENERGIA ---
            status_e = classificar_consumo(c_energia_pp, media_energia)
            diag_energia = ""
            dicas_energia = []

            if status_e == "baixo":
                diag_energia = "Parabéns! Seu consumo de energia está abaixo da média."
            elif status_e == "na_media":
                diag_energia = "Você está na média da sua região para consumo de energia."
            else:
                diag_energia = "Seu consumo de energia está muito alto."
                if tentou == "sim":
                    dicas_energia = ["Instale painéis solares fotovoltaicos", "Use tomadas inteligentes para cortar o stand-by", "Troque eletrodomésticos antigos por selo PROCEL A+++"]
                else:
                    dicas_energia = ["Troque lâmpadas antigas por LED", "Desligue aparelhos da tomada quando não usados", "Use ar-condicionado com timer", "Aproveite a luz natural do dia"]

            resultado = {
                "agua": {"diag": diag_agua, "consumo": round(c_agua_pp, 1), "media": media_agua, "dicas": dicas_agua},
                "energia": {"diag": diag_energia, "consumo": round(c_energia_pp, 1), "media": media_energia, "dicas": dicas_energia}
            }
        except: resultado = "erro"

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)

