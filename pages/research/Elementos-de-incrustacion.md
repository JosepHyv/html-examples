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
