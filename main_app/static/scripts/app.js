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



/* create post modal events */
$('#create-post-button').click(function() {
  $('#create-post').addClass('modal-active');
  $(document.body).css('overflow', 'hidden');
});

$('#create-post-close').click(function() {
  $('#create-post').removeClass('modal-active');
  $(document.body).css('overflow', 'visible');
});

$('#create-post-underlay').click(function() {
  $('#create-post').removeClass('modal-active');
  $(document.body).css('overflow', 'visible');
});



/* delete post modal events */
$('#delete-post-button').click(function() {
    $('#delete-post').addClass('modal-active');
    $(document.body).css('overflow', 'hidden');
});

$('.delete-post-close').click(function() {
    $('#delete-post').removeClass('modal-active');
    $(document.body).css('overflow', 'visible');
});

$('#delete-post-underlay').click(function() {
    $('#delete-post').removeClass('modal-active');
    $(document.body).css('overflow', 'visible');
});



/* edit post modal events */
$('#edit-post-button').click(function() {
    $('#edit-post').addClass('modal-active');
    $(document.body).css('overflow', 'hidden');
});

$('#edit-post-close').click(function() {
    $('#edit-post').removeClass('modal-active');
    $(document.body).css('overflow', 'visible');
});

$('#edit-post-underlay').click(function() {
    $('#edit-post').removeClass('modal-active');
    $(document.body).css('overflow', 'visible');
});