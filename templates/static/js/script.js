  // JavaScript para resaltar el líder de la tabla
        var tabla = document.getElementById('tabla-posiciones');
        var filas = tabla.getElementsByTagName('tr');
        for (var i = 1; i < filas.length; i++) {
            filas[i].addEventListener('mouseover', function() {
                this.classList.add('highlight');
            });
            filas[i].addEventListener('mouseout', function() {
                this.classList.remove('highlight');
            });
        }