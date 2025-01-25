**Date: 06/01/25**

### Capítulo 2
- Como desenvolver modelos (quando $y \in \mathbb{R}$)
	- Quem é $f$?
	- Por que estimar $f$?
	- Como estimar $f$?
	- Trade-off: previsão vs interpretabilidade

- Como medir a acurácia de modelos (quando $y \in \mathbb{R}$)
	- Medindo a qualidade da previsão
	- Trade-off: viés-variância

- Generalizações (quando $y \in \mathbb{R}$)

#### Parte 1 - Como desenvolver modelos
##### Quem é $f$?
- Assumimos que $Y = f(X) + \epsilon$, onde $\epsilon$ é um ruído independente de $X$ e possui média $0$.

- A esperança de $Y$ dado $X$ é $\mathbb{E}\left[ Y \mid X \right] = \mathbb{E}\left[ f(X) \mid X \right] + \mathbb{E}\left[ \epsilon \mid X \right] = f(X)$.

- Mesmo sem fazer hipóteses sobre a forma de $Y$, vale que $\mathbb{E}\left[ Y \mid X = x \right] = \underset{g(x)}{\text{argmin}} \ \mathbb{E}\left[ (Y - g(X))^2 \mid X = x \right]$
- Como $$\mathbb{E}\left[ (Y - g(X))^2 \mid X = x \right] = \mathbb{E}\left[ Y^2 \mid X = x \right] - 2 g(x) \mathbb{E}\left[ Y \mid X\right] + g^2(x)$$podemos derivar em $g(x)$ e igualar a $0$ para obter $$2 g(x) - 2 \mathbb{E}\left[Y \mid X \right] = 0 \implies g(x) = \mathbb{E}\left[Y \mid X \right]$$
- Ou seja, a esperança de $Y$ dado $X$ realmente é o melhor preditor em termos de erro médio quadrático.

Basicamente vimos duas formas de chegar na conclusão de que $f(x) = \mathbb{E}\left[Y \mid X = x \right]$.

##### Por que estimar $f$?
- Previsão
	- Se $\hat{f}$ é uma estimativa de $f$, podemos prever $\hat{y} = \hat{f}(X)$.

- Inferência
	- Se $\hat{f}$ é uma estimativa de $f$, podemos responder perguntas sobre $f$ como quais features são as mais importantes ou se há evidências de que $f$ é linear.

##### Como estimar $f$?
- $f$ vai ser aprendida a partir dos dados.

- Se hipóteses são aproximadamente válidas, métodos paramétricos são melhores.

- Com muitos dados, métodos não paramétricos podem ser melhores.

##### Trade-off: previsão vs interpretabilidade
- Modelos lineares são simples de interpretar; thin-plate splines, não.

- Preferimos modelos simples com poucas variáveis, a modelos caixa-preta com muitas.

#### Parte 2 - Como medir a acurácia de modelos
##### Medindo a qualidade da previsão


##### Trade-off: viés-variância


#### Parte 3 - Generalizações



#### Perguntas para revisão
###### Em regressão, como podemos expressar a função matemática $f(X)$ que queremos estimar? Por que ela é tipicamente inacessível?
Como estamos usando um modelo de regressão linear, estamos assumindo que $f(X) = \beta_0 + \beta_1 X_1 + \cdots + \beta_p X_p$, com $\beta_0, \beta_1, \cdots, \beta_p \in \mathbb{R}$.

Assumir essa forma para $f(X)$ transforma o problema em "como estimar os coeficientes $\beta$?".

###### Qual é a diferença de previsão vs inferência em machine learning?
A *previsão* está preocupada em achar uma função $\hat{f}$ que pode prever $\hat{y}$ para um $x$ não observado.

Já a *inferência* se importa em responder perguntas sobre as características da função $\hat{f}$ que estima $f$.

###### Qual é a diferença de métodos paramétricos e não-paramétricos? Dê um exemplo de cada
Métodos paramétricos exigem que seja feita uma assunção sobre a forma de $f(X)$ para encontrarmos a função daquela forma que melhor se aproxima do $f$ verdadeiro. *Ex. Regressão Linear, Análise Discriminante Linear.*

Os métodos não-paramétricos não assumem nenhuma forma para a função que estamos estimando, tornando elas mais versáteis e mais eficientes quando temos muitos dados. *Ex. kNN.*

*Redes Neurais* é um caso estranho, é um método paramétrico no sentido de que assumimos uma forma para a função, mas ela se comporta de maneira não-paramétrica pela quantidade de coeficientes que é estimada.







