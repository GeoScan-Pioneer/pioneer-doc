document.addEventListener("DOMContentLoaded", () => {
    let tileHeight = getComputedStyle(document.documentElement).getPropertyValue('--tile-height');
    document.querySelectorAll(".tile").forEach(plate => {
        var a = [
            plate.getElementsByClassName('icon'),
            plate.getElementsByClassName('header'),
            plate.getElementsByClassName('caption'),
            plate.getElementsByClassName('spacer')
            ].forEach(aKey => {
                if (aKey.length > 0) {
                console.log(aKey)
                aKey[0].addEventListener('click', event => {
                    if (tileHeight.includes(plate.style.height) || plate.style.height == '') {
                        plate.style.height = plate.scrollHeight + 'px';
                        plate.classList.toggle('large');
                    } else {
                        plate.style.height = tileHeight;
                        plate.classList.toggle('large');
                    }
                });
            }
        })
        window.addEventListener('resize', event => {
            if (!tileHeight.includes(plate.style.height) && plate.style.height != '')
                plate.style.height = plate.scrollHeight + 'px';
        });
    });

});

