# ChatbotAIStreamlitG1SI

**Título de la aplicación:** Chatbot Starfly

**Objetivo:** Este chatbot esta basado en el API de ChatGPT. Al brindar un contexto, el chatbot es capaz de responder preguntas a los usuarios respecto al servicio StarFly (servicio ficticio) .

> Starfly es un servicio de streamming para ver películas y series. Este servicio está disponible por el momento para dispositivos iOS y Android, así como para TV mediante ChromeCast y Apple TV. Existe dos tipos de suscripciones en este servicio: La suscripción mensual por 25 soles y la suscripción anual de 225 soles. En la suscripción anual ofrecemos un descuento de 3 meses gratis, incluido ya en el precio final. Si el cliente desea cancelar su suscripción, debe hacerlo llamando al número 505-1212 o mediante el correo starfly@suscription.com.

## Instrucciones:

**NOTA:** Si bien este código puede ejecutarse sin problemas, se recomienda realizarlo en un entorno virtual de Python para evitar que afecte e interfiera con otros proyectos de Python.
Si ud. aún está iniciando en Python le recomendamos realizarlo mediante venv.

1. Instala las dependencias del archivo "requirements.txt" mediante el comando en la terminal:
<code>pip install -r requirements.txt</code>

2. Una vez instalado las dependencias, diríjase al archivo "secrets.toml" y en la variable api_secret, cambie el valor entre comillas por su API Key de Open AI que puede obtenerlo en este [enlace](https://platform.openai.com/account/api-keys). No borre las comillas.

>**NOTA:** Para obtener el API Key deberá iniciar sesión con su cuenta de Open AI, en caso de no tener una, deberá registrarse en la plataforma.

3. Por último, para poder ejecutar el proyecto, inserte el siguiente comando en la terminal:
<code>streamlit run Hello.py</code>
