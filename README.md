# SEVID

El proyecto "SEVID" fue elaborado como parte del curso de "Proyecto De Diseño De Ingenieria En Computadores" de la carrera de Ingeniería en Computadores en el Instituto Tecnológico de Costa Rica.

## Descripción

"SEVID" es un sistema para la verificación de documentos de identidad costarricense utilizando la placa Raspberry Pi Zero W como sistema embebido. Este sistema consta de módulos de captura de imágenes, procesamiento de imágenes y validación de datos. El objetivo principal del proyecto es desarrollar un sistema automatizado y de bajo costo que pueda verificar la autenticidad de los documentos de identidad emitidos por el gobierno de Costa Rica.

El módulo de captura de imágenes utiliza una cámara integrada en la Raspberry Pi Zero W para capturar imágenes de los documentos de identidad. El módulo de procesamiento de imágenes utiliza una API de Google Cloud para extraer información relevante, como el número de identificación y el nombre del titular. El módulo de validación de datos compara la información extraída del documento escaneado con una base de datos de documentos proporcionada por el TSE. 

El modo de uso del sistema es mediante una aplicación web, donde el usuario puede cargar la imagen del documento de identidad y/o fotografiar el documento de identidad y así recibir una respuesta en tiempo real sobre la autenticidad del mismo. El sistema mostrará en pantalla si el documento escaneado coincide o no con ninguno de los documentos auténticos almacenados en la base de datos.

[Diagrama de bloques]()


## Herramientas utilizadas

-	Angular
-   Python
-   Flask

## Instalación

Para obtener detalles sobre la instalación, consulta la documentación [aquí](https://github.com/davidaqc/embsys_sevid/tree/main/documentos).

## Instrucciones de uso

Para obtener instrucciones detalladas sobre el uso del sistema, consulta la documentación [aquí](https://github.com/davidaqc/embsys_sevid/tree/main/documentos).
