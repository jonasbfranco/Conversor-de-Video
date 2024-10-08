# Conversor de Video

<img src="imagens/conversor-de-video-2.png" alt="Texto Alternativo">

*  * *
### [Link para a parte 1 do vídeo no Youtube](https://youtu.be/VHznI5_ou58)

### [Link para a parte 2 do vídeo no Youtube](https://youtu.be/YApJwCvbH2I)
* * * 

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/VHznI5_ou58/maxresdefault.jpg)](https://youtu.be/VHznI5_ou58)

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YApJwCvbH2I/maxresdefault.jpg)](https://youtu.be/YApJwCvbH2I)

* * *



### Configuração e Instalação

1. Criar ambiente virtual e ativá-lo

#### Windows
```bash
md first-flet-app
cd first-flet-app
python -m venv .venv
.venv\Scripts\activate
```

#### macOS
```bash
mkdir first-flet-app
cd first-flet-app
python3 -m venv .venv
source .venv/bin/activate
```

#### Linux
```bash
mkdir first-flet-app
cd first-flet-app
python3 -m venv .venv
source .venv/bin/activate
```

* * * 
<br> <br>


2. Instalação dos pacotes:

```bash
pip install -r requirements.txt
```

```bash
pip install flet moviepy
```
<br>

3. Atualizar o arquivo requirements.txt:

```bash
pip freeze > requirements.txt
```
<br>

### Executar aplicativo

4. Executar aplicação:

```bash
phyton conversor.py
```

```bash
flet main.py
```

4. 🚨 Atenção, instalar FFMPEG:

- procurar tutorias de Instalação, ou baixar do site ffmpeg.org [link para download](https://www.ffmpeg.org/download.html), descompactar e renomear para ffmpeg, copiar e colar no C:\, depois abrir o CMD como Administrador e executar o comandoabaixo
```bash
setx /m PATH "C:\ffmpeg\bin;%PATH%"
```

<img src="imagens/cmd.png" alt="Texto Alternativo" width="420">

<br>

5. Verificar versão instalada:

```bash
ffmpeg -version
```


#### Flet é um framework moderno que combina a simplicidade do Python com o poder do Flutter para o desenvolvimento de interfaces. Com ele, você pode construir aplicações web e móveis com uma única base de código, aproveitando a flexibilidade do HTML/CSS e a performance nativa.


