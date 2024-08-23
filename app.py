from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as gemini

app = Flask(__name__)
CORS(app)  # Habilita o CORS
gemini.configure(api_key="Sua chave API")
model = gemini.GenerativeModel('gemini-1.5-flash')

@app.route('/plano_dieta', methods=['POST'])
def criar_plano_dieta():
    try:
        dados = request.json
        peso = dados.get('peso')
        altura = dados.get('altura')
        genero = dados.get('genero')
        objetivo = dados.get('objetivo')

        if not all([peso, altura, genero, objetivo]):
            return jsonify({"Erro": "Informações incompletas"}), 400

        prompt = f"""
        Gere um plano de dieta para uma pessoa com as seguintes características:
        Peso: {peso}kg,
        Altura: {altura}cm,
        Gênero: {genero},
        Objetivo: {objetivo}.
        
        A dieta deve incluir a quantidade recomendada de alimentos para café da manhã, almoço, jantar e lanches, 
        com base no peso, altura e objetivo. Apresente o plano em formato HTML com codificação UTF-8, com título em h1, 
        subtítulos em h2 e a quantidade dos alimentos especificada em gramas, mililitros ou unidades.
        NÃO GERAR DIETAS COM ALTURAS E PESOS HUMANAMENTE IMPOSSÍVEIS, AO INVÉS DISSO EXIBA COM UM H5 "Dados Inválidos.
         Atualize o site e tente novamente." NÃO GERAR DIETAS ABSURDAS COM PALAVRAS ALEATÓRIAS.
        gerar dieta em forma de item uma embaixo da outra. NA SUA RESPOSTA NÃO COLOQUE "'''html".
        QUANDO GERAR A DIETA, NAO COLOCAR "*" AO INVÉS DISSO COLOQUE "<STRONG>"
        """

        resposta = model.generate_content(prompt)
        dieta = resposta.text.strip()

        return jsonify({"dieta": dieta}), 200

    except Exception as e:
        return jsonify({"Erro": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
