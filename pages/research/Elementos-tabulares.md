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
