var canvas = document.getElementById('canvas');
var canvass = document.getElementById('canvas1');

if (canvas.getContext) {
    var ctx = canvas.getContext('2d');

    ctx.beginPath();
    ctx.fillStyle = "rgba(245, 245, 245, 0.7)";
    ctx.arc(100, 100, 45, 0, Math.PI*0.7, false);  // Mouth (clockwise)
    ctx.moveTo(65, 65);
    ctx.stroke();
    ctx.fill();

    ctx.beginPath();
    ctx.fillStyle = "rgba(245, 245, 245, 0.7)";
    ctx.arc(200, 200, 45, 0, Math.PI*1, false);  // Mouth (clockwise)
    ctx.moveTo(65, 65);
    ctx.stroke();
    ctx.fill();

    ctx.beginPath();
    ctx.fillStyle = "rgba(245, 245, 245, 0.7)";
    ctx.arc(300, 300, 45, 0, Math.PI*1.3, false);  // Mouth (clockwise)
    ctx.moveTo(65, 65);
    ctx.stroke();
    ctx.fill();

    ctx.beginPath();
    ctx.fillStyle = "rgba(245, 245, 245, 0.7)";
    ctx.arc(400, 400, 45, 0, Math.PI*2, false);  // Mouth (clockwise)
    ctx.moveTo(65, 65);
    ctx.stroke();
    ctx.fill();

}

if (canvass.getContext) {
    var ctxx = canvass.getContext('2d');

    ctxx.beginPath();
    ctxx.fillStyle = "rgba(255, 255, 255, 1)";
    ctxx.arc(250, 250, 200, 0, Math.PI*2, false);  // Mouth (clockwise)
    ctxx.moveTo(65, 65);
    ctxx.stroke();
    ctxx.fill();

    ctxx.beginPath();
    ctxx.fillStyle = "rgba(255, 255, 255, 1)";
    ctxx.arc(340,200,30,0, Math.PI*2, false);
    ctxx.moveTo(65,65);
    ctxx.lineWidth = 5;
    ctxx.stroke();
    ctxx.fill();

    ctxx.beginPath();
    ctxx.fillStyle = "rgba(255, 255, 255, 1)";
    ctxx.arc(160,200,30,0, Math.PI*2, false);
    ctxx.moveTo(65,65);
    ctxx.lineWidth = 5;
    ctxx.stroke();
    ctxx.fill();

    ctxx.beginPath();
    ctxx.fillStyle = "rgba(255, 255, 255, 1)";
    ctxx.arc(250,300,60,0, Math.PI*1, false);
    ctxx.moveTo(65,65);
    ctxx.lineWidth = 5;
    ctxx.stroke();
    ctxx.fill();
}