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
