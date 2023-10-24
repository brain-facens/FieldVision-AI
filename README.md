# FieldVision AI

https://github.com/brain-facens/OCR-notas/assets/64169072/8078be88-cb17-4616-9e03-8646b638b623

API for processing text on invoices, with the aim of identifying relevant fields on an invoice and optimizing bonus or validation systems. Making life easier for logisticians, merchants and managers, the application has an interface that captures images from the webcam, processes the image using OCR and provides a visualization of the results obtained.

## First Steps

This project was developed to run a web interface, where the user will have access to the image capture system and the data processed from that image. Follow the steps below to use this project, the stable version is in the main branch.

### Requirements

The following requirements should ideally be met for proper operation:

- Ubuntu 20.04 (Original development environment, but compatible with 18.04 and 22.04)
- Docker Engine or Docker Desktop
- Python 3.8
- Git
- Anaconda/Miniconda
- Create a virtual environment for the project if you want to work without conda;
 
  ```
  conda create --name fielvision python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

  # Activate the environment
  conda activate fielvision
  ```

---
**Warning!**
**We recommend that you use the Docker container developed for this project, as the application is stable. This avoids the risk of incorrect installations, path errors and library versions.**

---

### Installation 

Local:

```
# Activate the environment
conda activate fielvision

# Clone repository
git clone https://github.com/brain-facens/FieldVision-AI.git

# Install requirements
cd FieldVision-AI/
pip install -r requirements.txt
```

Docker:
```
# Pull image
docker pull brain20/ocr-notas
```


## Usage

Local:

```
# Applicable filter of up to 3 words 
# python src/field_vision_API/main.py <fist, second, third>

# Run API
python src/field_vision_API/main.py
```

Docker:
```
# Running the container with the application
docker run -it --rm -p 8080:8080 brain20/ocr-notas
```
---
**Warning!**
Running the container will start the API, which is the interface between OCR processing and the end user. The API is documented in a Swagger, where you can test it.

---

## Demo


https://github.com/brain-facens/OCR-notas/assets/64169072/fcb7e222-cb14-4963-8ef6-a1e8f77f521b



---

## 🤝 Collaborators

We would like to thank the following people who contributed to this project:

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/64169072?v=4" width="100px;" alt="Foto do Natanael Vitorino no GitHub"/><br>
        <sub>
          <b>Natanael Vitorino</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/102334565?v=4" width="100px;" alt="Foto do Natanael Vitorino no GitHub"/><br>
        <sub>
          <b>Lucas Oliveira</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/98903288?v=4" width="100px;" alt="Foto do Pedro Gabriel no GitHub"/><br>
        <sub>
          <b>Pedro Gabriel</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## 📝 License

This project is under license. See the file [LICENSE](LICENSE) for more details.

---
