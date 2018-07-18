/*
to modify total time, just input on variable totaltime
*/
var totaltime = 60;

function update(percent) {
    var deg;
    if (percent < (totaltime / 2)) {
        deg = 90 + (360 * percent / totaltime);
        $('.pie').css('background-image',
            'linear-gradient(' + deg + 'deg, transparent 50%, white 50%),linear-gradient(90deg, white 50%, transparent 50%)'
        );
    } else if (percent >= (totaltime / 2)) {
        deg = -90 + (360 * percent / totaltime);
        $('.pie').css('background-image',
            'linear-gradient(' + deg + 'deg, transparent 50%, #00b5e8 50%),linear-gradient(90deg, white 50%, transparent 50%)'
        );
    }
}
var count = parseInt($('#time').text());
myCounter = setInterval(function () {
    count -= 1;
    if(count<10){
      $('#time').html('0'+count);
    }
    else{
      $('#time').html(count);
    }
    update(count);
    if (count == 0) clearInterval(myCounter);
}, 1000);