var canvas = document.getElementById("canvas");

if (canvas.getContext) {

    var ctx = canvas.getContext("2d");

    ctx.fillStyle = `rgba(255,255,255,1)`;
    ctx.fillRect(0,0,1000,1000);

    var filerect = 10;

    for (var i = 1; i < 10; i++) {
    	ctx.fillStyle = `rgba(0,0,200,${i/10})`;
    	ctx.fillRect(filerect+5, 10, 50,50);
    	filerect += 70;
    }

    var filerect = 10;

    for (var i = 1; i < 10; i++) {
    	ctx.fillStyle = `rgba(191, 2, 2,${i/10})`;
    	ctx.fillRect(filerect+5, 70, 50,50);
    	filerect += 70;
    }

    var filerect = 10;
    
    for (var i = 1; i < 10; i++) {
    	ctx.fillStyle = `rgba(31, 184, 4,${i/10})`;
    	ctx.fillRect(filerect+5, 130, 50,50);
    	filerect += 70;
    }

    var filerect = 10;
    
    for (var i = 1; i < 10; i++) {
    	ctx.fillStyle = `rgba(184, 4, 118,${i/10})`;
    	ctx.fillRect(filerect+5, 190, 50,50);
    	filerect += 70;
    }

    var filerect = 10;
    
    for (var i = 1; i < 10; i++) {
    	ctx.fillStyle = `rgba(27, 38, 49,${i/10})`;
    	ctx.fillRect(filerect+5, 190, 50,50);
    	filerect += 70;
    }

    var filerect = 10;
    
    for (var i = 1; i < 10; i++) {
    	ctx.fillStyle = `rgba(74, 35, 90,${i/10})`;
    	ctx.fillRect(filerect+5, 250, 50,50);
    	filerect += 70;
    }

    var filerect = 10;
    
    for (var i = 1; i < 10; i++) {
    	ctx.fillStyle = `rgba(23, 32, 42,${i/10})`;
    	ctx.fillRect(filerect+5, 310, 50,50);
    	filerect += 70;
    }

    var filerect = 10;
    
    for (var i = 1; i < 10; i++) {
    	ctx.fillStyle = `rgba(100, 30, 22,${i/10})`;
    	ctx.fillRect(filerect+5, 370, 50,50);
    	filerect += 70;
    }

    var filerect = 10;
    
    for (var i = 1; i < 10; i++) {
    	ctx.fillStyle = `rgba(123, 125, 125,${i/10})`;
    	ctx.fillRect(filerect+5, 430, 50,50);
    	filerect += 70;
    }
}