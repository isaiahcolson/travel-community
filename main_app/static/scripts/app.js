/* signup modal events */
$('#signup-modal-button').click(function() {
    $('#signup-modal').addClass('modal-active');
});

$('#signup-close').click(function() {
    $('#signup-modal').removeClass('modal-active');
});

$('#signup-underlay').click(function() {
    $('#signup-modal').removeClass('modal-active');
});



/* login modal events */
$('#login-modal-button').click(function() {
    $('#login-modal').addClass('modal-active');
});

$('#login-close').click(function() {
    $('#login-modal').removeClass('modal-active');
});

$('#login-underlay').click(function() {
    $('#login-modal').removeClass('modal-active');
});