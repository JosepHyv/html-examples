# Elementos para Agrupar Contenido


### Elemento `<div>`
El elemento `<div>` se utiliza para agrupar contenido en una sección genérica o contenedor sin un significado específico. Es ampliamente utilizado para aplicar estilos CSS o para manipular grupos de elementos con JavaScript. Ejemplo:

```html
<div class="contenedor">
    <p>Este es un párrafo dentro de un contenedor div.</p>
    <ul>
        <li>Elemento 1</li>
        <li>Elemento 2</li>
    </ul>
</div>
```

### Elemento `<span>`
El elemento `<span>` se utiliza para aplicar estilos o manipular texto u otros elementos en línea. A menudo se utiliza dentro de párrafos o encabezados para resaltar partes específicas del texto. Ejemplo:

```html
<p>Este es un ejemplo de texto <span style="color: blue;">resaltado en azul</span> en un párrafo.</p>
```

### Elemento `<fieldset>` y `<legend>`
Los elementos `<fieldset>` y `<legend>` se utilizan para agrupar y etiquetar controles de formulario relacionados. `<fieldset>` crea un contenedor y `<legend>` proporciona una etiqueta descriptiva para el grupo. Ejemplo:

```html
<fieldset>
    <legend>Datos Personales</legend>
    <label for="nombre">Nombre:</label>
    <input type="text" id="nombre" name="nombre"><br>
    <label for="email">Correo Electrónico:</label>
    <input type="text" id="email" name="email"><br>
</fieldset>
```

### Elemento `<figure>` y `<figcaption>`
Los elementos `<figure>` y `<figcaption>` se utilizan para agrupar contenido multimedia, como imágenes o videos, junto con una descripción o título. `<figure>` crea el contenedor y `<figcaption>` proporciona la descripción. Ejemplo:

```html
<figure>
    <img src="imagen.jpg" alt="Descripción de la imagen">
    <figcaption>Esta es una imagen de ejemplo.</figcaption>
</figure>
```

### Elemento `<ul>` y `<li>`
Los elementos `<ul>` (lista desordenada) y `<li>` (elemento de lista) se utilizan para crear listas, ya sean listas de elementos o elementos de navegación. Ejemplo:

```html
<ul>
    <li>Elemento 1</li>
    <li>Elemento 2</li>
    <li>Elemento 3</li>
</ul>
```

# Elementos para establecer secciones

### Elemento `<header>`
El elemento `<header>` se utiliza para definir la cabecera o encabezado de una sección o contenido. Generalmente, contiene elementos como títulos, logotipos y enlaces de navegación relacionados con la sección. Aquí tienes un ejemplo:

```html
<header>
    <h1>Mi Página Web</h1>
    <nav>
        <ul>
            <li><a href="#">Inicio</a></li>
            <li><a href="#">Acerca de</a></li>
            <li><a href="#">Contacto</a></li>
        </ul>
    </nav>
</header>
```

### Elemento `<footer>`
El elemento `<footer>` se utiliza para definir el pie de una sección o contenido. Usualmente contiene información de contacto, derechos de autor o enlaces relacionados con la sección. Ejemplo:

```html
<footer>
    <p>&copy; 2023 Mi Empresa</p>
    <p>Contacto: info@miempresa.com</p>
</footer>
```

### Elemento `<section>`
El elemento `<section>` se utiliza para dividir el contenido en secciones temáticas o agrupar contenido relacionado. Cada `<section>` puede tener su propio encabezado (`<header>`) y pie (`<footer>`) si es necesario. Ejemplo:

```html
<section>
    <header>
        <h2>Noticias</h2>
    </header>
    <p>Últimas noticias sobre tecnología.</p>
    <footer>
        <p>Más noticias en nuestra sección de tecnología.</p>
    </footer>
</section>
```

### Elemento `<article>`
El elemento `<article>` se utiliza para representar contenido independiente y autocontenido dentro de una página, como noticias, publicaciones de blog o comentarios. Ejemplo:

```html
<article>
    <header>
        <h2>Titular de la Noticia</h2>
    </header>
    <p>Texto de la noticia...</p>
    <footer>
        <p>Autor: John Doe</p>
        <p>Fecha: 5 de octubre de 2023</p>
    </footer>
</article>
```

### Elemento `<nav>`
El elemento `<nav>` se utiliza para definir una sección de navegación que contiene enlaces a otras partes de la página o a otras páginas web. Ejemplo:

```html
<nav>
    <ul>
        <li><a href="#">Inicio</a></li>
        <li><a href="#">Acerca de</a></li>
        <li><a href="#">Contacto</a></li>
    </ul>
</nav>
```
# Elementos de Formularios

### Elemento `<form>`
El elemento `<form>` se utiliza para crear un formulario en HTML. Dentro de `<form>`, puedes incluir elementos de entrada, como campos de texto, casillas de verificación, botones de radio y más. Aquí tienes un ejemplo básico de un formulario:

```html
<form action="procesar.php" method="post">
    <label for="nombre">Nombre:</label>
    <input type="text" id="nombre" name="nombre"><br>
    
    <label for="email">Correo Electrónico:</label>
    <input type="email" id="email" name="email"><br>
    
    <label for="mensaje">Mensaje:</label>
    <textarea id="mensaje" name="mensaje"></textarea><br>
    
    <input type="submit" value="Enviar">
</form>
```

### Elemento `<input>`
El elemento `<input>` se utiliza para crear campos de entrada en un formulario. Puedes especificar el tipo de entrada utilizando el atributo `type`, que puede ser `text`, `password`, `radio`, `checkbox`, `email`, `number`, entre otros. Ejemplo:

```html
<input type="text" id="nombre" name="nombre">
<input type="password" id="contraseña" name="contraseña">
<input type="checkbox" id="suscribir" name="suscribir" value="si">
```

### Elemento `<textarea>`
El elemento `<textarea>` se utiliza para crear un área de texto de varias líneas en un formulario, ideal para que los usuarios ingresen texto extenso. Ejemplo:

```html
<textarea id="comentarios" name="comentarios" rows="4" cols="50"></textarea>
```

### Elemento `<select>` y `<option>`
El elemento `<select>` se utiliza para crear listas desplegables en un formulario, mientras que `<option>` se utiliza para definir las opciones dentro de la lista. Ejemplo:

```html
<select id="ciudad" name="ciudad">
    <option value="nueva-york">Nueva York</option>
    <option value="los-angeles">Los Ángeles</option>
    <option value="chicago">Chicago</option>
</select>
```

### Elemento `<button>`
El elemento `<button>` se utiliza para crear botones en un formulario, que pueden ser de envío (`type="submit"`), restablecimiento (`type="reset"`), o simplemente un botón (`type="button"`) para realizar acciones personalizadas. Ejemplo:

```html
<button type="submit">Enviar</button>
<button type="reset">Restablecer</button>
<button type="button" onclick="miFuncion()">Hacer Algo</button>
```
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

# Elementos de Incrustacion


### Elemento `<img>`
El elemento `<img>` se utiliza para incrustar imágenes en una página web. Puedes especificar la ruta de la imagen en el atributo `src` y proporcionar texto alternativo en el atributo `alt` para accesibilidad. Ejemplo:

```html
<img src="imagen.jpg" alt="Descripción de la imagen">
```

### Elemento `<audio>`
El elemento `<audio>` se utiliza para incrustar audio en una página web. Puedes proporcionar múltiples fuentes de audio para garantizar la compatibilidad con diferentes navegadores. Ejemplo:

```html
<audio controls>
    <source src="audio.mp3" type="audio/mpeg">
    <source src="audio.ogg" type="audio/ogg">
    Tu navegador no admite elementos de audio.
</audio>
```

### Elemento `<video>`
El elemento `<video>` se utiliza para incrustar videos en una página web. Al igual que con el elemento `<audio>`, puedes proporcionar múltiples fuentes de video para la compatibilidad con diferentes navegadores. Ejemplo:

```html
<video controls width="320" height="240">
    <source src="video.mp4" type="video/mp4">
    <source src="video.webm" type="video/webm">
    Tu navegador no admite elementos de video.
</video>
```

### Elemento `<iframe>`
El elemento `<iframe>` se utiliza para incrustar contenido de otro sitio web dentro de tu página. Puedes especificar la URL del contenido que deseas incrustar en el atributo `src`. Ejemplo:

```html
<iframe src="https://www.ejemplo.com"></iframe>
```

### Elemento `<embed>`
El elemento `<embed>` se utiliza para incrustar contenido multimedia, como Flash, en una página web. Puedes especificar la URL del recurso y ajustar el tamaño y otros atributos según sea necesario. Ejemplo:

```html
<embed src="reproductor.swf" width="400" height="300">
```
# Elementos Tabulares 


### Elemento `<table>`
El elemento `<table>` se utiliza para crear una tabla en HTML. Dentro de `<table>`, utilizas `<tr>` para definir filas de la tabla y `<td>` o `<th>` para definir celdas de datos. `<th>` se utiliza para encabezados de columna o fila, mientras que `<td>` se utiliza para datos regulares. Ejemplo:

```html
<table>
    <tr>
        <th>Nombre</th>
        <th>Edad</th>
    </tr>
    <tr>
        <td>Juan</td>
        <td>30</td>
    </tr>
    <tr>
        <td>María</td>
        <td>25</td>
    </tr>
</table>
```

### Elemento `<thead>`, `<tbody>`, y `<tfoot>`
Puedes utilizar los elementos `<thead>`, `<tbody>`, y `<tfoot>` para dividir una tabla en secciones. `<thead>` se utiliza para encabezados de tabla, `<tbody>` para el cuerpo principal de la tabla, y `<tfoot>` para los resúmenes o totales de la tabla. Ejemplo:

```html
<table>
    <thead>
        <tr>
            <th>Producto</th>
            <th>Precio</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Zapatos</td>
            <td>$50</td>
        </tr>
        <tr>
            <td>Camisa</td>
            <td>$25</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td>Total</td>
            <td>$75</td>
        </tr>
    </tfoot>
</table>
```

### Elemento `<caption>`
El elemento `<caption>` se utiliza para agregar un título o descripción a una tabla. Debe estar dentro del elemento `<table>`. Ejemplo:

```html
<table>
    <caption>Lista de Empleados</caption>
    <tr>
        <th>Nombre</th>
        <th>Departamento</th>
    </tr>
    <tr>
        <td>José</td>
        <td>Finanzas</td>
    </tr>
</table>
```
# Elementos de Scripting 

### Elemento `<script>`
El elemento `<script>` se utiliza para agregar scripts o código JavaScript a una página HTML. Puedes incluir scripts en el encabezado `<head>` o en el cuerpo `<body>` de tu documento HTML. Aquí tienes un ejemplo básico:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Ejemplo de Script</title>
    <script>
        function saludar() {
            alert('¡Hola, mundo!');
        }
    </script>
</head>
<body>
    <button onclick="saludar()">Saludar</button>
</body>
</html>
```

### Elemento `<noscript>`
El elemento `<noscript>` se utiliza para proporcionar contenido alternativo que se muestra si el navegador del usuario no admite scripts o si los scripts están deshabilitados. Aquí tienes un ejemplo:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Contenido Alternativo</title>
    <script>
        document.write("Este es el contenido generado por JavaScript.");
    </script>
    <noscript>
        <p>Por favor, habilita JavaScript para ver el contenido completo.</p>
    </noscript>
</head>
<body>
</body>
</html>
```

### Atributo `async` y `defer`
Los atributos `async` y `defer` se pueden usar en el elemento `<script>` para controlar cuándo se ejecuta el script en relación con la carga de la página. `async` indica que el script se ejecutará de forma asincrónica mientras se carga la página, mientras que `defer` indica que el script se ejecutará después de que se haya analizado el documento HTML.

```html
<script src="mi-script.js" async></script>
<script src="mi-script.js" defer></script>
```
