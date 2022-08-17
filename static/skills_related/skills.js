const fadeout = () => {
    const loadwrapper = document.querySelector('.wrapper');
    loadwrapper.classList.add('fade');
}
window.addEventListener('load' , fadeout);