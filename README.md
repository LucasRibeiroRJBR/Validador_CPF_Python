# Validador de CPF em Python

>ScreeShots  

**Tela inicial**  
![](https://snipboard.io/TbkrNj.jpg)

**Tela indicando que o número CPF é válido**  
![](https://snipboard.io/cN9eIm.jpg)

**Tela indicando que o número CPF é válido**  
![](https://snipboard.io/MOb3he.jpg)

**Também funciona utilizando pontos e traços padrões do CPF**  
![](https://snipboard.io/K9itvp.jpg)

>Regras

Regras para a validação do **primeiro dígito verificador**:

* Os primeiros 9 dígitos são multiplicados de 2 até 10 em ordem decrescente;
* O resultado de cada multiplicação é somado, multiplicado por 10 e então se obtém o resto da divisão por 11;
* Primeiro dígito obtido com sucesso.

Regras para a validação do **segundo dígito verificador**:

* Os primeiros 9 dígitos são multiplicados de 2 até 11 em ordem decrescente;
* Usando o primeiro dígito verificador obtido, multiplicamos ele por 2;
* O resultado de todas as multiplicações somamos e então multiplicamos por 10 e obtemos o resto da divisão por 11;
* Segundo dígito verificados obtido com sucesso.  

---  

>Validação  

Igualamos se os resultados são compatíveis ou não e assim é feito a validação.  

---  

>Exemplo  

|1|1|6|8|4|0|4|5|0|9|6|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|10|9|8|7|6|5|4|3|2|
|**10**|**9**|**48**|**56**|**24**|**0**|**16**|**15**|**0**|**---**|**---**|  
</br>  

10 + 9 + 48 + 56 + 24 + 0 + 16 + 15 + 0 = <span style="color: green; bold">**178**</span>  
178 * 10 = <span style="color: green; bold">**1780**</span>  
1780 % 11 = <span style="color: yellow; bold">**9**</span>  
</br>
---  
</br>  

|1|1|6|8|4|0|4|5|0|<span style="color: yellow; bold">**9**</span>|6|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|11|10|9|8|7|6|5|4|3|<span style="color: yellow; bold">**2**</span>|
|**11**|**10**|**54**|**64**|**28**|**0**|**20**|**20**|**0**|**82**|**---**|  
</br>  

11 + 10 + 54 + 64 + 28 + 0 + 20 + 20 + 0 + 18 = <span style="color: green; bold">**225**</span>  
225 * 10 = <span style="color: green; bold">**2250**</span>  
2250 % 11 = <span style="color: yellow; bold">**6**</span>  
</br>  
---

116.840.450-**96** 

---
>Créditos  

Icons designed by <a href="https://www.flaticon.es/autores/iconixar" title="iconixar">iconixar</a> from <a href="https://www.flaticon.es/" title="Flaticon"> www.flaticon.es</a>

---
## Lucas Ribeiro
[![GitHub](https://user-images.githubusercontent.com/53449579/95284130-c9631400-0833-11eb-8948-41471baf8c88.png)](https://github.com/LucasRibeiroRJBR)   [**LucasRibeiroRJBR**](https://github.com/LucasRibeiroRJBR)  
[![LinkedIn](https://user-images.githubusercontent.com/53449579/95283692-c4519500-0832-11eb-803e-75db4a3bd1ef.png)](https://www.linkedin.com/in/lucas-santos-ribeiro/)   [**Lucas Ribeiro**](https://www.linkedin.com/in/lucas-santos-ribeiro/)  
[![Twitter](https://user-images.githubusercontent.com/53449579/95283384-1219cd80-0832-11eb-8ec3-c2c44c020030.png)](https://www.twitter.com/lucas_sanri)   [**@lucas_sanri**](https://www.twitter.com/lucas_sanri)  
[![Instagram](https://user-images.githubusercontent.com/53449579/95283610-99674100-0832-11eb-86c5-fd3e71647f57.png)](https://www.instagram.com/lucas_sanri/)   [**@lucas_sanri**](https://www.instagram.com/lucas_sanri/)

