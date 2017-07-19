 // targeting the window
 // event handler on scroll - call funciton
 // if scrollTop is greater than 100 pixels - it'll add shrink

$(window).scroll(function() {
  if ($(document).scrollTop() > 100) {
    $('nav').addClass('shrink');
  }
  else {
    $('nav').removeClass('shrink');
  }
});
