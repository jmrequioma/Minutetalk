$(document).ready(function($) {
    var Body = $('body');
    Body.addClass('preloader-site');
});
$(window).load(function() {
    $('.preloader-wrapper').delay(500).fadeOut(200);
    $('body').removeClass('preloader-site');
});