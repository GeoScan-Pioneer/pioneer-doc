document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".tile").forEach(plate => {
        plate.addEventListener('click', event => {
            if (plate.style.height == '100px' || plate.style.height == '') {
                plate.style.height = plate.scrollHeight + 'px'
                plate.classList.toggle('large')
            }
            else {
                plate.style.height = '90px'
                plate.classList.toggle('large')
            }
        });
        window.addEventListener('resize', event => {
            if (plate.style.height != '90px' && plate.style.height != '')
                plate.style.height = plate.scrollHeight + 'px'
        });
    });

});

