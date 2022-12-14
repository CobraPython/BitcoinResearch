# 馃 Telegram Bot

 ![Telebot](images/telebot.png)

El Nodo Bitcoin tendr谩 un canal de comunicaci贸n mediante telegram. Usando un Bot que esta corriendo en un punto dedicado (otro Rpi) se comunicar谩 con el nodo para realizar consultas. 


El bot de telegram para el Nodo tiene las siguientes caracter铆sticas:

- Desplegar r谩pidamente informaci贸n del nodo: temperatura, memoria, estado de procesos, ip, etc a solicitud de una (o varias) cuentas maestras. Se puede tener acceso remoto al nodo por medio de esta red. En un caso de emergencia puede ser una alternativa para tener a mano esta direcci贸n (se debe tener extremo cuidado en la manipulaci贸n de estas por seguridad, este es solo un experimento).
  
- Interactuar con otros usuarios brindando informaci贸n:
	- Informaci贸n del clima. 
	  Usando un API que entrega datos meteorol贸gicos podemos recopilar y facilitar esta informaci贸n para todo el territorio. De ser posible brindar info como la radiaci贸n solar, atardecer, etc.
	- Verificaci贸n de exposici贸n de filtraci贸n de datos.
	  En 2021 se filtraron mas de 3 millones de cuentas Bolivianas de facebook con nombres, n煤mero celular, perfil, etc. Diversas estafas pueden usar esta informaci贸n que es p煤blica con prop贸sitos maliciosos. Puedes verificar si tu n煤mero de celular (solo de Bolivia) esta asociada a alguna cuenta de facebook filtrada.
	- Gr谩ficas y series de tiempo Bitcoin.
	  El nodo puede comunicarse y extraer informaci贸n de la red Bitcoin de manera directa. Se puede brindar algunas gr谩ficas como la mempool el como varia el precio. A futuro an谩lisis onchain.
	- Paga por aprender.
	  Este punto es por ahora una idea. Trata de construir un sistema de pagos en satoshis que por cada pdf que pueda ser entregado y superado un breve test libera una factura en la red lightning 鈿?. Existen ejemplos de servicios como Fountain que lo hacen con podcasts. 
- Interactuar con otros usuarios brindando informaci贸n que puede ser 煤til para potenciales usuarios de todo Hispano Am茅rica:
	- Verificador de transacci贸n. 
	  Una transacci贸n bitcoin no se considera irreversible cuando llega a la mempool sino cuando es confirmada al menos 6 veces (confirmaci贸n en el contexto de nuevos bloques adelante). Algunos exchanges y servicios crypto consideran suficiente la verificaci贸n de 2 bloques. Se busca que el nodo pueda notificar cuando tenga 2 verificaciones de una transacci贸n dada (o se pueda configurar cuantas se quiera). Telegram tiene la ventaja de mantener un poco mas el anonimato para realizar esta consulta, el nodo realiza la verificaci贸n directa sin recurrir a ning煤n otro servicio protegiendo los datos de los interesados. 
	- Blockclock, mempool stats, price.

## 01 noviembre 2022

Inicialmente solo desplegamos un Bot que se comunique con la cuenta maestra. 

> En [Montando un bot base](https://github.com/CobraPython/BitcoinResearch/blob/main/Telegram-Bot/Montando%20un%20bot%20base.md) detallamos paso a paso como configurar un bot. 

