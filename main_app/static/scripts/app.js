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