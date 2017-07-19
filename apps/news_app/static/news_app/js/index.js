$(document).ready(function() {

  /* For the sticky navigation */
  $('.js--section-features').waypoint(function(direction) {
      if (direction == "down") {
          $('nav').addClass('sticky');
      } else {
          $('nav').removeClass('sticky');
      }
  }, {
    offset: '60px;'
  });

  // click flash it button
  $('.js--scroll-to-latest').click(function() {
    $('html, body').animate({scrollTop: $('.js--section-news').offset().top}, 1000);
  });

  // click Subscribe  button
  $('.js--scroll-to-subscription').click(function() {
    $('html, body').animate({scrollTop: $('.js--subscription').offset().top}, 1000);
  });

  // Animations on scroll
  $('.js--wp-1').waypoint(function(direction) {
    $('.js--wp-1').addClass('animated fadeIn');
  }, {
    offset: '50%'
  });

  $('.js--wp-2').waypoint(function(direction) {
    $('.js--wp-2').addClass('animated fadeInUp');
  }, {
    offset: '50%'
  });

});
