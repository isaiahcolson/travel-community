/* signup modal events */
$('#signup-modal-button').click(function() {
    $('#signup-modal').addClass('modal-active');
    $(document.body).css('overflow', 'hidden');
});

$('#signup-close').click(function() {
    $('#signup-modal').removeClass('modal-active');
    $(document.body).css('overflow', 'visible');
});

$('#signup-underlay').click(function() {
    $('#signup-modal').removeClass('modal-active');
    $(document.body).css('overflow', 'visible');
});

$('.signup-login').click(function() {
    $('#signup-modal').removeClass('modal-active');
    $('#login-modal').addClass('modal-active');
});



/* login modal events */
$('#login-modal-button').click(function() {
    $('#login-modal').addClass('modal-active');
    $(document.body).css('overflow', 'hidden');
});

$('#login-close').click(function() {
    $('#login-modal').removeClass('modal-active');
    $(document.body).css('overflow', 'visible');
});

$('#login-underlay').click(function() {
    $('#login-modal').removeClass('modal-active');
    $(document.body).css('overflow', 'visible');
});

$('.login-signup').click(function() {
    $('#login-modal').removeClass('modal-active');
    $('#signup-modal').addClass('modal-active');
});



/* signup edit modal events */
$('#edit-profile-button').click(function() {
    $('#edit-profile').addClass('modal-active');
    $(document.body).css('overflow', 'hidden');
});

$('#edit-profile-close').click(function() {
    $('#edit-profile').removeClass('modal-active');
    $(document.body).css('overflow', 'visible');
});

$('#edit-profile-underlay').click(function() {
    $('#edit-profile').removeClass('modal-active');
    $(document.body).css('overflow', 'visible');
});