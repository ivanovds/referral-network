var copyTextareaBtn = document.querySelector('.copy-invite');

copyTextareaBtn.addEventListener('click', function(event) {
  var copyTextarea = document.querySelector('.invite-text');
  copyTextarea.focus();
  copyTextarea.select();

  try {
    var successful = document.execCommand('copy');
    var msg = successful ? 'successful' : 'unsuccessful';
    console.log('Copying text command was ' + msg);
  } catch (err) {
    console.log('Oops, unable to copy');
  }
});