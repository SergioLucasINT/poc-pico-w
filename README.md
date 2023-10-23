# Prova de Conceito Raspberry Pi Pico W

Nesta prova de conceito, há o foco em mostrar a interface de rede Wi-Fi integrada no microcontrolador, com o intuito de fazer uma requisição GET para um site qualquer. 

## Ferramentas

Para realização dessa prova de conceito foi utilizado a plataforma Wokwi, o microcontrolador utilizado foi o Raspberry Pi Pico W, e a linguagem utilizada para programar o sistema foi o MicroPython com auxílio das bibliotecas network, time, machine e usocket. [O projeto está disponível neste link](https://wokwi.com/projects/379349465776406529)

## Entendimento do Código (Alto nível)

O código utiliza das bibliotecas mencionadas acima e da rede aberta Wokwi para realizar uma requisição ao site http://google.com/. O microcontrolador está conectado a um LED RGB que irá acender em 3 cores diferentes dependendo de seu estado; amarelo, enquanto a requisição não recebe resposta, verde, caso a requisição tenha sido bem sucedida (código 200 OK), e vermelho, caso a requisição tenha falhado (qualquer código que não seja este)

## Explicação do Código

1. Definição dos pinos que servirão de output para o LED utilizado como feedback do status do código, utilizando a biblioteca machine.
2. Função para definir as cores do LED.
3. Utilização da Biblioteca network para conectar-se a rede aberta Wokwi de acordo com a [documentação oficial](https://docs.wokwi.com/pt-BR/guides/esp32-wifi).
4. Caso a conexão tenha sido bem sucedida, o código continua, caso contrário, entrará em um loop eterno, utilizando da biblioteca time.
5. Definição da função de realizar o request.
6. Criação de conexão socket na url escolhida, utilizando a biblioteca socket.
7. Envio da request e acende o led RGB na cor amarela
8. Ao receber a resposta, caso o retorno do status seja 200 OK, o led RGB irá trocar para a cor verde, caso contrário, irá trocar para cor vermelha.

## Conclusão

É possível concluir com essa prova de conceito as capacidades do microcontrolador de se comunicar via internet e utilizar sockets, abrindo portas para possibilidades mais complexas de uso deste produto.
