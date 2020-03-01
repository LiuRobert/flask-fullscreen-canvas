var ctx = null

function init() {
    ctx = document.querySelector('canvas').getContext('2d');
    resize()
}

function resize() {
    ctx.canvas.width = document.body.offsetWidth;
    ctx.canvas.height = document.body.offsetHeight;
    clear()
}

function clear() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "#FF0000";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
}