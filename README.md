### Produzido por Henrique Eissmann Buzzi ###

# Algoritmo para detecção de borda pelo método de Canny

## Modo de usar:

Forneça uma imagem em escala de cinza para o sistema, defina os limiares em porcentagem (de 0 até 1, que seria 0% até 100%), e defina o sigma/desvio padrão utilizado para o kernel gaussiano (valores baixos são suficientes e melhores)
Ao fornecer isto ao algoritmo, o mesmo retorna as 2 imagens de borda, uma levando em consideração o limiar superior e outro o limiar inferior.

## Executando:

Idêntico ao explicado no modo de usar. Apenas altere os valores na parte de INPUTS e experimente com os resultados

## Conceitos aplicados

Aplicação de filtro gaussiano, Imagem do gradiente de magnitude, Imagem do gradiente da fase, Supressão de não máximos locais, Limiarização dupla, Análise de conectividade

## Possíveis implementações futuras

...
