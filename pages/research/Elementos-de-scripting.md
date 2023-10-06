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
