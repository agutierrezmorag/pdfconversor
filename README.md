# pdfconversor, tesseract

# Dependencias

- [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)

Descargar instalador y ejecutarlo. Una vez instalado, agregar el directorio de instalacion
a la variable de entorno PATH. En un command prompt `cmd` con permisos de administrador, ejecutar
el siguiente comando:

`setx PATH "%PATH%;C:\Program Files\Tesseract-OCR"`

Reemplazar `C:\Program Files\Tesseract-OCR` por el directorio donde Tesseract esté instalado
en caso de haber seleccionado otro directorio durante su instalacion.

Confirmar que fue instalado correctamente ejecutar el siguiente comando:

`tesseract --version`

En caso de no tirar error, el programa fue instalado correctamente. Es posible que se necesite
reinicar el PC para que los cambios al PATH surgan efecto.

# Uso

Simplemente ejecutar `tesseract.py`. Todos los documentos en la carpeta `documentos` seran
transcritos a texto en una subcarpeta de `PostProcesado`. 

Considerar que la ejecucion del programa puede tomar tiempo dependiendo de la cantidad
de documentos a transcribir y del hardware donde se ejecuta, con la cantidad actual de documentos (12)
no demora más de 5 minutos en el hardware testeado.