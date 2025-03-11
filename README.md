# Crawler

Memoria Técnica: Crawler de Detección de URLs con Errores 4XX
1. Objetivo del Proyecto
El objetivo de este proyecto es desarrollar un crawler web utilizando Python y Selenium para explorar de manera recursiva el dominio web www.insbaixcamp.org y detectar todas las URLs que devuelvan códigos de error 4XX. Los errores 4XX indican que el servidor ha recibido una solicitud incorrecta o que el recurso solicitado no está disponible. El crawler identifica estos enlaces con error y genera un informe en formato CSV con la URL del error, el código de error y la página de origen desde donde se accedió al enlace problemático.

2. Decisiones de Diseño
2.1 Tecnologías Utilizadas
Python: Python es el lenguaje elegido para implementar el crawler debido a su sintaxis sencilla y su extensa biblioteca de soporte. La librería requests se utiliza para realizar las solicitudes HTTP y verificar el estado de las URLs, mientras que BeautifulSoup ayuda a parsear el contenido HTML y extraer los enlaces.

Selenium: Selenium se emplea para la automatización del navegador web. Se utiliza para obtener el contenido dinámico de las páginas y explorar enlaces, ya que permite interactuar con páginas web que cargan contenido mediante JavaScript.

CSV: Se ha seleccionado el formato CSV para almacenar los resultados del crawler, ya que es fácil de manejar, procesar y utilizar en otras herramientas de análisis o visualización.

2.2 Exploración de Dominio Recursiva
El crawler realiza una exploración recursiva del dominio www.insbaixcamp.org. A partir de la página principal, el crawler obtiene todos los enlaces internos de la página, asegurándose de que no sean enlaces externos. Este proceso se repite de manera recursiva para cada enlace encontrado, lo que permite explorar todo el dominio de manera exhaustiva.

2.3 Detección de Errores 4XX
El crawler verifica el estado de cada URL interna utilizando la librería requests. Si una URL devuelve un código de error en el rango 4XX, como "404 - Página no encontrada" o "403 - Acceso prohibido", se registra la URL junto con el código de error y la página de origen. Los códigos de error 4XX son importantes ya que indican problemas con las URLs del sitio que deben corregirse.

2.4 Generación de Informe CSV
Una vez completada la exploración, el crawler genera un informe en formato CSV que contiene los siguientes campos:

URL con Error: La URL que ha devuelto un código de error 4XX.
Código de Error HTTP: El código de error correspondiente (por ejemplo, "404").
Página de Origen: La página desde la que se accedió a la URL con error.
El informe se guarda en un archivo denominado errores_4xx.csv, lo que permite a los administradores del sitio web analizar y corregir los enlaces rotos.

3. Proceso de Implementación
El proceso de implementación se ha realizado en varios pasos:

Configuración de Selenium: Se configura Selenium para que utilice el navegador Chrome en modo headless (sin interfaz gráfica), lo que permite ejecutar el crawler de manera eficiente en un servidor o entorno sin GUI.

Obtención de enlaces internos: Se utiliza BeautifulSoup para analizar el HTML de cada página y extraer los enlaces internos. Estos enlaces se validan para asegurarse de que pertenezcan al mismo dominio.

Verificación de códigos de error HTTP: Para cada enlace interno, se realiza una solicitud HTTP utilizando requests para obtener el código de estado de la respuesta. Si el código está en el rango 4XX, se guarda la URL y el código de error.

Exploración recursiva: La exploración de enlaces se realiza de manera recursiva. Si un enlace lleva a otra página dentro del mismo dominio, se explora también, manteniendo un registro de las páginas ya visitadas para evitar explorarlas nuevamente.

Generación del informe: Una vez terminada la exploración, se generan los resultados en un archivo CSV que incluye la URL con el error, el código de error y la página de origen.
