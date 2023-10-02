# pdfconversor

Conversor de PDF > imagen > texto.

# Dependencias

- [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/)

# Testing

Se realizó la transcripción de las páginas 5-10 del reglamento regimen general de estudios, mediante una 
[herramienta online](https://www.online-convert.com/) y luego de manera local con las librerías `pdf2image` para la separación 
de cada página del pdf por imágenes y `easyocr` para la transcripción de dichas imágenes.

Esto resulta en un texto con errores, para intentar corregir algunos se propone utilizar `gpt3.5` dando uso del
siguiente prompt: 

`Revisa el siguiente texto y corrígelo. Solo realiza correcciones ortográficas, elimina las oraciones sin sentido, 
pero no cambies el orden ni la estructura del texto.`

Sin embargo, algunos errores persisten, sobre todo con ciertos caracteres especiales.

El tiempo de operación entre ambas opciones fue similar.