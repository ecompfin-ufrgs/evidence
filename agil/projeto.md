# Projeto

1. A arquitetura do e-Vidence será componentizada por pacotes científicos, de coleta de dados, pacotes controllers e um frontend.
2. Os pacotes científicos serão desenvolvidos em Python, Julia ou R e executados no servidor de pesquisa da FCE ou da UFRGS.
3. O pacote de coleta de dados será desenolvido em Python e executado no servidor de pesquisa da FCE ou da UFRGS.
4. Os pacotes controllers, escritos em Python Flask, consumirão os resultados dos pacotes científicos e de coleta de dados, provendo Rest API's para o runtime web PHP da UFRGS direcionar ao frontend e paralelamente gravação no na base MySQL do servidor departamental da UFRGS. 
5. O pacote frontend será servido pelo runtime web PHP da UFRGS como uma aplicação Flutter compilada para web, mobile ou desktop.
