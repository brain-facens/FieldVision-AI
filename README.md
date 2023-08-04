# OCR Notas

Sistema para processamento de texto em notas fiscais para identificação de boneficação.

## Primeiros passos

Este projeto foi desenvolvido para executar uma interface web, onde o usuário terá acesso ao sistema de captura de imagens e os dados processados desta mesma imagem. Siga os passos a seguir para utilizar este projeto, a versão estável está na branch master.

### Prerequisitos

Para o bom funcionamento, é ideal que os requsitos abaixo sejam atendidos:

* Ubuntu 20.04 (Ambiente de desenvolvimento original, mas é compatível com 18.04 e 22.04)
* Docker Engine ou Docker Desktop
* Python 3.8
* Git
* Anaconda/Miniconda
* Desejaveis
  * CUDA 10.1 / CUDA 10.2
  * cuDNN 7.6
* Crie um ambiente virtual para o projeto caso queira trabalhar sem virtualização;
 
  ```
  conda create --name paddle_env python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

  # Ative o ambiente
  conda activate paddle_env
  ```

**Note**
Recomendamos que utilizer Docker pois a aplicação é estável, não correndo o risco de instalações erradas, erros de paths e versões de bibliotecas.


### Instalação 

Localmente:

```
# Ative o ambiente
conda activate paddle_env

git clone https://github.com/brain-facens/OCR-notas.git

cd OCR-notas
pip install -r requirements.txt
```

Docker:
```
# Download da imagem do projeto
docker push natavitorino/ocr_paddle:1.2

```


## Utilização

Localmente:

```
streamlit run interface.py
```

Docker:
```
# Execução do conteiner com a aplicação
docker run -it --rm --name OCR --privileged --net=host --env=NVIDIA_VISIBLE_DEVICES=all --env=NVIDIA_DRIVER_CAPABILITIES=all --env=DISPLAY --env=QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix natavitorino/ocr_paddle:1.2 bash
```

## Deployment

Additional notes on how to deploy this on a live or release system. Explaining the most important branches, what pipelines they trigger and how to update the database (if anything special).

### Server

* Live:
* Release:
* Development:

### Branches

* Master:
* Feature:
* Bugfix:
* etc...

## Additional Documentation and Acknowledgments

* Project folder on server:
* Confluence link:
* Asana board:
* etc...
