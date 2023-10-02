from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
from mobile_OCR import OCRInterface

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = ""
CORS(app)

def ocr_process(image_path, phrases):
    ocr_interface = OCRInterface()
    return ocr_interface.ocr_process(image_path, phrases)

@app.route('/')
def menu():
    return "F"

@app.route('/home', methods=['POST', 'GET'])
def upload_image():
    try:
        if request.method == "POST":
            image = request.files.get('file')
            image_path = "/home/pedro/Documents/NotasFiscais/images/temp.jpg"  # Salvar temporariamente a imagem
            image.save(image_path)
            
            process_img = ocr_process(image_path, "VALOR")
            print(process_img)
            
            return jsonify({"Txts": process_img})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)
    
#     try:
#         uploaded_file = request.files['file']
#         text_lines = ocr_process(uploaded_file, "TOTAL")
#         return jsonify({"lines": f'{text_lines}'})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
    
    
    
# @app.route('/processar_imagem', methods=['GET', 'POST'])
# def processar_imagem():
#     try:
#         # imagem = request.files['imagem']
#         imagem = '/home/pedro/Pictures/Screenshots/print_nf.png'
#         # Verifica se o tipo MIME é uma imagem
#         # allowed_mimes = {'image/jpeg', 'image/png', 'image/gif'}
#         # if imagem.mimetype not in allowed_mimes:
#         #     return jsonify({"error": "Tipo de arquivo inválido. Apenas imagens são permitidas."}), 400

#         # imagem_pil = Image.open(imagem)
#         imagem_ = cv2.imread(imagem)
#         # print(imagem_)
#         text_lines = ocr_process(imagem_, ["total"])
#         print(text_lines)
#         return jsonify({"lines": f'{text_lines}'}) # Retorna os textos identificados como uma string

#     # return "chegou"
    
