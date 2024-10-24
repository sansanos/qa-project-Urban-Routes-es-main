# Proyecto Urban Routes 

***Elaborado por Santiago Sánchez Ospina (14avo grupo, SPRINT #8)***

## Descripción del proyecto
Este proyecto tiene como propósito desarrollar una 
solución de automatización empleando **Selenium**, 
una herramienta que permite la automatización de 
navegadores web. El objetivo general de este trabajo es 
automatizar el proceso de solicitud de un viaje, simulando 
las interacciones que un usuario realizaría de forma manual
en la plataforma de transporte Urban Routes. A través de esta automatización, 
se busca optimizar y simplificar dicho proceso, garantizando su 
correcta ejecución de manera repetitiva y eficiente.

## Sobre la aplicación

**Urban routes** es una aplicación web que cumple con la 
funcion de dar  un servicio de transporte al usuario. 
La aplicación consta de 3 tipos de viaje, cada uno con sus opciónes
de solicitud y modos de transpporte, los cuales son seleccionados por el usuario.

## Proceso:

Este proceso de automatización cuenta un patrón de diseño llamado
**POM** (Page Object Model), que 
ayuda a organizar y mantener el código de prueba mediante la creación de 
clases independientes para cada página web o componente. 

Se debe instalar el paquete Pytest, este se encuentra dentro de la 
opción "Python Packages" de Pycharm, o por medio de la terminal usando el comando 
"pip3 install pytest". El comando usado para correr las pruebas en la terminal es 
"pytest qa-project-Urban-Routes-es-main/test_cases.py".

Primero se organizan los datos a usar para las pruebas (data).
Luego se seleccionan todos los difentes localizadores necesarios (locators), 
se definen todos los metodos a usar (methods), y por último se realizan
todas las pruebas relcionadas al servicio de pedir un automóvil (test_cases).

## Solicitudes requeridas:
1. Configurar la dirección 
2. Seleccionar la tarifa Comfort
3. Rellenar el número de teléfono
4. Agregar una tarjeta de crédito
5. Escribir un mensaje para el controlador
6. Pedir una manta y pañuelos
7. Pedir 2 helados
8. Aparece el modal para buscar un taxi

## Tecnologías

En la elaboración de este proyecto, se implementó una automatización basada 
en un flujo secuencial que contemplaba un escenario general donde se simula 
el proceso completo de solicitar un automóvil a través de la plataforma Urban Routes. 
Para ello, se empleó el lenguaje de programación Python y el patrón de diseño POM, 
por medio entorno del desarrollo integrado PyCharm, se procedió a 
descargar e instalar la herramienta Selenium Web Driver, la cual fue configurada 
para el navegador Chrome, permitiendo la interacción automática con el 
entorno web.

Durante las diferentes fases del desarrollo, se ejecutaron diversas 
actividades de verificación y validación (asserts), asegurando que cada paso 
del flujo automatizado cumpliera con las expectativas funcionales. 
Estas verificaciones permitieron identificar posibles mejoras y ajustes 
en el proceso. Como resultado de estas etapas de verificación, se llevaron 
a cabo un total de 8 pruebas distintas, cada una de ellas diseñada para 
evaluar diferentes aspectos del sistema y garantizar el correcto desempeño 
del flujo automatizado en su conjunto.


