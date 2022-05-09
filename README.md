# 04-NLTK-Detecting_Emotions_In_Text

## **Detecção de emoções em texto com o Naive Bayes utilizando a biblioteca NLTK**

### Definição do Projeto

As soluções de análise de sentimento são usadas para extrair significado de milhões de mensagens. Elas identificam o sentimento entre uma ou várias sentenças de uma notícia veiculada, para medir a opinião pública geral sobre uma determinada marca ou evento. A emoção em tais postagens pode não ser explicitamente expressa ou pode ser difusa, e as soluções de análise de sentimento precisam lidar com esse problema. A análise de sentimento pode ajudar as empresas com as seguintes tarefas:

- Análise de sentimento como vantagem competitiva
- Análise de sentimento para melhorar a experiência do cliente
- Análise de sentimento para percepção adequada de marca

Fonte:
https://www.viacognitiva.com.br/single-post/aplicacoes-pln-importantes

Para esse trabalho utilizamos a biblioteca NLTK e o classificador Naive Bayes da própria biblioteca.

As emoções utilizadas nesse trabalho são as seis emoções básicas definidas pelo psicólogo Paul Ekman, sendo elas:
- Surpresa
- Alegria
- Tristeza
- Medo
- Desgosto ou nojo
- Raiva

Os arquivos estão divididos em:

**functions.py**
- Contém as funções utilizadas durante o trabalho

**main.py**
- Treinamento e classificação utilizando os seis tipos de emoções básicas definidas pelo psicólogo Paul Ekman

**twoclass.py**
- Treinamento e classificação utilizando apenas duas emoções, desgosto e tristeza
