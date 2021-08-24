document.addEventListener('DOMContentLoaded', () => {
    if (location.pathname.indexOf('/index.html') >= 0) {
        document.getElementsByClassName('rst-footer-buttons')[0].style.display = "none";
        document.getElementsByClassName('headerlink')[0].style.display = "none";
        let toclist = document.getElementsByClassName('wy-menu-vertical')[0].children;
        console.log(toclist.length);
        if (toclist.length > 2) {
            for (let i = 0; i < toclist.length - 2; i++) {
                toclist[i].style.display = "none";
            }
        }
    }
});