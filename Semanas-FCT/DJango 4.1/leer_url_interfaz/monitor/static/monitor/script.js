document.querySelectorAll('.windows button').forEach(boton => {
    boton.addEventListener('click', () => {
        const filtro = boton.getAttribute('data-filtro');
        const urlParams = new URLSearchParams(window.location.search);
        urlParams.set('tab', filtro);
        window.location.search = urlParams.toString();
    });
});

// NUEVO: Mostrar/ocultar filtro de opciones
document.getElementById("filter-toggle").addEventListener("click", function () {
    const menu = document.getElementById("filter-options");
    menu.style.display = menu.style.display === "flex" ? "none" : "flex";
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
document.addEventListener("DOMContentLoaded", () => {
    const lightcheck = document.getElementById("light-mode");
    const darkcheck = document.getElementById("dark-mode");

    function updateTheme() {
        if (darkcheck.checked) {
            document.body.classList.add("dark-mode");
            lightcheck.checked = false;
        } else {
            document.body.classList.remove("dark-mode");
            lightcheck.checked = true;
        }
    }

    lightcheck.addEventListener("change", () => {
        darkcheck.checked = !lightcheck.checked;
        updateTheme();
    });

    darkcheck.addEventListener("change", () => {
        lightcheck.checked = !darkcheck.checked;
        updateTheme();
    });

    updateTheme();
});