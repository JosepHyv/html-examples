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

