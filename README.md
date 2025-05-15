# Projeto OpenGL em Python

Este projeto é uma implementação básica de renderização 3D utilizando **OpenGL** com Python. Ele utiliza GLFW para criação da janela e gerenciamento de input, PyOpenGL para interação com a API OpenGL, e PyGLM para manipulação de vetores e matrizes.

O projeto inclui uma câmera controlável, objetos 3D (cubos texturizados) e manipulação via mouse e teclado.

---

## Requisitos

Este projeto depende das seguintes bibliotecas Python:

- `glfw==2.9.0`
- `numpy==2.2.5`
- `pillow==11.2.1`
- `pyglm==2.8.2`
- `PyOpenGL==3.1.9`
- `PyOpenGL-accelerate==3.1.9`

---

## Como instalar as dependências

Recomenda-se usar um ambiente virtual para evitar conflitos. Para criar e ativar um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate.bat  # Windows
```

Com o ambiente virtual ativado, instale as dependências com:

```
pip install -r requirements.txt
```

---

## Como executar o projeto

Após instalar as dependências, rode o arquivo principal do projeto:

```
python3 main.py
```

---

## Créditos

* LearnOpenGL (https://learnopengl.com/)
* Professor Rafael Ivo (https://www.youtube.com/@ProfessorRafaelIvo)
