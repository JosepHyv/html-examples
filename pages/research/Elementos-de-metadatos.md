# Elementos de metadatos
Los elementos de metadatos del documento en HTML5 se utilizan para proporcionar información sobre el documento web, como su título, conjunto de caracteres, autor, descripción, palabras clave y más. Aquí tienes algunos de los elementos más comunes en esta categoría:

1. `<head>`: El elemento `<head>` contiene metadatos que no se muestran directamente en la página web, como enlaces a hojas de estilo, scripts y otros elementos importantes para la configuración del documento.

   Ejemplo:
   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <title>Título de la Página</title>
       <meta charset="UTF-8">
       <link rel="stylesheet" href="styles.css">
     </head>
     <body>
       <!-- Contenido de la página -->
     </body>
   </html>
   ```

2. `<title>`: El elemento `<title>` define el título de la página que se muestra en la pestaña del navegador o en los resultados de búsqueda.

   Ejemplo:
   ```html
   <title>Mi Página Web</title>
   ```

3. `<meta>`: El elemento `<meta>` se utiliza para proporcionar metadatos sobre el documento, como el conjunto de caracteres, la descripción de la página, palabras clave y más.

   Ejemplo:
   ```html
   <meta charset="UTF-8">
   <meta name="description" content="Descripción de mi página web">
   <meta name="keywords" content="HTML, CSS, JavaScript">
   ```

4. `<link>`: El elemento `<link>` se usa para vincular recursos externos, como hojas de estilo CSS o fuentes personalizadas, al documento.

   Ejemplo:
   ```html
   <link rel="stylesheet" href="styles.css">
   ```

5. `<style>`: El elemento `<style>` permite agregar estilos CSS directamente en el documento HTML.

   Ejemplo:
   ```html
   <style>
     body {
       background-color: #f0f0f0;
     }
   </style>
   ```

6. `<base>`: El elemento `<base>` especifica una URL base para todas las URL relativas en el documento.

   Ejemplo:
   ```html
   <base href="https://www.ejemplo.com/">
   ```

7. `<script>`: El elemento `<script>` se usa para agregar scripts JavaScript al documento. Puede estar dentro del `<head>` o al final del `<body>`.

   Ejemplo:
   ```html
   <script src="script.js"></script>
   ```

