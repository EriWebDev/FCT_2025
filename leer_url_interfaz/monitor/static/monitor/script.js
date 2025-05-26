document.querySelectorAll('.windows .barra button').forEach(boton => {
    boton.addEventListener('click', () => {
        const filtro = boton.getAttribute('data-filtro');
        const urlParams = new URLSearchParams(window.location.search);
        urlParams.set('tab', filtro);
        window.location.search = urlParams.toString();
    });
});


document.addEventListener('DOMContentLoaded', () => {
    const botones = document.querySelectorAll('.windows button');
    const params = new URLSearchParams(window.location.search);
    const pestañaActiva = params.get('tab') || 'todos';

    botones.forEach(boton => {
        const filtro = boton.getAttribute('data-filtro');
        if (filtro === pestañaActiva) {
            boton.classList.add('activo');
        } else {
            boton.classList.remove('activo');
        }
        boton.addEventListener('click', () => {
            botones.forEach(b => b.classList.remove('activo')); // Quitar todos
            boton.classList.add('activo'); // Agregar al actual

            const nuevoFiltro = boton.getAttribute('data-filtro');
            const nuevaURL = new URL(window.location);
            nuevaURL.searchParams.set('tab', nuevoFiltro);
            window.location.href = nuevaURL.toString();
        });
    });
});


// NUEVO: Mostrar/ocultar filtro de opciones
document.getElementById('filter-toggle').addEventListener('click', () => {
    const opciones = document.getElementById('filter-options');
    opciones.style.display = (opciones.style.display === 'none') ? 'block' : 'none';
});

// NUEVO: Hash MD5
document.getElementById("filter-md5").addEventListener("click", async function () {
    const texto = prompt("Introduce el texto para calcular su hash MD5:");
    if (texto) {
        const hash = await md5(texto);
        alert("Hash MD5:\n" + hash);
    }
});

// NUEVO: Filtro general
document.getElementById("filter-general").addEventListener("click", function () {
    alert("Filtro general activado (simulado).");
});

// NUEVO: Subida de archivo y análisis de palabras clave
document.getElementById("filter-keywords").addEventListener("click", function () {
    document.getElementById("file-input").click();
});

document.getElementById("file-input").addEventListener("change", function (e) {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function (event) {
        const text = event.target.result;
        const palabras = text.match(/\b[\wáéíóúñ]{5,}\b/gi) || [];
        const comunes = ['para', 'este', 'esas', 'estos', 'sobre', 'donde'];
        const claves = [...new Set(palabras.filter(p => !comunes.includes(p.toLowerCase())))];
        document.getElementById("keyword-output").innerText = "Palabras clave encontradas:\n" + claves.join(', ');
    };
    reader.readAsText(file);
});

// Función MD5 con Web Crypto
async function md5(message) {
    const msgUint8 = new TextEncoder().encode(message);
    const hashBuffer = await crypto.subtle.digest('MD5', msgUint8);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    return hashHex;
}

//Modo oscuro
//🟣​ 07/05/2025 - Actualización del Modo oscuro para que funcione con botón en vez de checkbox
document.addEventListener("DOMContentLoaded", () => {
    const toggleButton = document.getElementById("toggle-theme");
    const icon = document.getElementById("theme-icon");

    if (localStorage.getItem("theme") === "dark") {
        document.documentElement.classList.add("dark-mode");
    }

    //Cambiar icono
    //🟣​ 08/05/2025 - Cambio de función
    const lightIcon = toggleButton.getAttribute("data-light-icon");
    const darkIcon = toggleButton.getAttribute("data-dark-icon");
    
    function updateThemeIcon() {
        icon.src = document.documentElement.classList.contains("dark-mode") ? lightIcon : darkIcon;
    }    
    updateThemeIcon();

    //Cambiar tema
    toggleButton.addEventListener("click", () => {
        document.documentElement.classList.toggle("dark-mode");
        const nuevoTema = document.documentElement.classList.contains("dark-mode") ? "dark" : "light";
        localStorage.setItem("theme", nuevoTema);
        updateThemeIcon();
    });
});

//Buscador no es lo que se busca
function buscarURL() {
  const input = document.getElementById('urlInput').value.trim();  
  if (input) {
    document.getElementById('contenido').innerHTML = `<p>Buscando resultados para: <strong>${input}</strong></p>`;
  } else {
    alert("Por favor, escribe una URL o término de búsqueda.");
  }
}

// nuevo codigo 14/5/2025 se implementa codigo para guardar el check y que se quede guardado
document.querySelectorAll('input.check').forEach(checkbox => {
    checkbox.addEventListener('change', function () {
        const formData = new FormData();
        formData.append('id', this.value);
        formData.append('estado', this.checked);
        fetch('/ajax/marcar/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCSRFToken(),
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (!data.success) {
                alert('Error al guardar el estado del checkbox.');
            }
        });
    });
});

function getCSRFToken() {
    const name = 'csrftoken';
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const c = cookies[i].trim();
        if (c.startsWith(name + '=')) {
            return decodeURIComponent(c.substring(name.length + 1));
        }
    }
    return '';
}
// nuevo codigo 14/5/2025 se implementa codigo para guardar el check y que se quede guardado

//Barra lateral
        function toggleSidebar() {
            const sidebar = document.getElementById('sidebar');
            const collapsed = sidebar.classList.toggle('collapsed');
            localStorage.setItem('sidebar-collapsed', collapsed);
        }

        window.addEventListener('DOMContentLoaded', () => {
            const sidebar = document.getElementById('sidebar');
            const isCollapsed = localStorage.getItem('sidebar-collapsed') === 'true';
            if (isCollapsed) {
                sidebar.classList.add('collapsed');
            }
        });