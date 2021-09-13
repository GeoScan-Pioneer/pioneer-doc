document.addEventListener("DOMContentLoaded", () => {
    let tileHeight = getComputedStyle(document.documentElement).getPropertyValue('--tile-height');
    document.querySelectorAll(".tile").forEach(plate => {
        plate.addEventListener('click', event => {
            if (tileHeight.includes(plate.style.height) || plate.style.height == '') {
                plate.style.height = plate.scrollHeight + 'px';
                plate.classList.toggle('large');
            }
            else {
                plate.style.height = tileHeight;
                plate.classList.toggle('large');
            }
        });
        window.addEventListener('resize', event => {
            if (!tileHeight.includes(plate.style.height) && plate.style.height != '')
                plate.style.height = plate.scrollHeight + 'px';
        });
    });

});

