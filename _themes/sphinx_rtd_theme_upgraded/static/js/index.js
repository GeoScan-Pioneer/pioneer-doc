document.addEventListener('DOMContentLoaded', () => {
    if (location.pathname.indexOf('/index.html') >= 0) {
        document.getElementsByClassName('rst-footer-buttons')[0].style.display = "none";
        document.getElementsByClassName('headerlink')[0].style.display = "none";
    }
});