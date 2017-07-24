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


  /* Scroll on buttons */
  $('.js--scroll-to-plans').click(function() {
    $('html, body').animate({
      scrollTop: $('.js--section-plans').offset().top
    }, 1000);
  });

  $('.js--scroll-to-start').click(function() {
    $('html, body').animate({
      scrollTop: $('.js--section-features').offset().top
    }, 1000);
  });

  // click flash it button
  $('.js--scroll-to-latest').click(function() {
    $('html, body').animate({
      scrollTop: $('.js--section-news').offset().top
    }, 1000);
  });

  // click Subscribe  button
  $('.js--scroll-to-subscription').click(function() {
    $('html, body').animate({
      scrollTop: $('.js--subscription').offset().top
    }, 1000);
  });

  // click tech  button
  $('.js--scroll-to-tech').click(function() {
    $('html, body').animate({
      scrollTop: $('.js--tech').offset().top
    }, 1000);
  });


  //   // Animations on scroll
  $('.js--wp-1').waypoint(function(direction) {
    $('.js--wp-1').addClass('animated fadeIn');
  }, {
    offset: '50%'
  });

  $('.js--wp-2').waypoint(function(direction) {
    $('.js--wp-2').addClass('animated fadeInUp');
  }, {
    offset: '35%'
  });

  $('.js--wp-3').waypoint(function(direction) {
    $('.js--wp-4').addClass('animated slideInLeft');
  }, {
    offset: '50%'
  });

  $('.js--wp-4').waypoint(function(direction) {
    $('.js--wp-5').addClass('animated slideInRight');
  }, {
    offset: '50%'
  });

  $('.js--wp-6').waypoint(function(direction) {
    $('.js--wp-7').addClass('animated slideInLeft');
  }, {
    offset: '70%'
  });

  $('.js--wp-6').waypoint(function(direction) {
    $('.js--wp-8').addClass('animated slideInRight');
  }, {
    offset: '70%'
  });

  $('.js--wp-19').waypoint(function(direction) {
    $('.js--wp-20').addClass('animated fadeInUp');
  }, {
    offset: '70%'
  });

  $('.js--wp-19').waypoint(function(direction) {
    $('.js--wp-21').addClass('animated fadeInUp');
  }, {
    offset: '20%'
  });

  $('.js--wp-20').waypoint(function(direction) {
    $('.js--wp-22').addClass('animated fadeInUp');
  }, {
    offset: '5%'
  });

  $('.js--wp-20').waypoint(function(direction) {
    $('.js--wp-23').addClass('animated fadeInUp');
  }, {
    offset: '20%'
  });

  $('.js--wp-24').waypoint(function(direction) {
    $('.js--wp-24').addClass('animated fadeInUp');
  }, {
    offset: '60%'
  });

  $('.js--wp-24').waypoint(function(direction) {
    $('.js--wp-25').addClass('animated fadeInUp');
  }, {
    offset: '50%'
  });

  //Tech section Animations

  $('.js--wp-29').waypoint(function(direction) {
    $('.js--wp-37').addClass('animated zoomIn');
  }, {
    offset: '70%'
  });

  $('.js--wp-30').waypoint(function(direction) {
    $('.js--wp-31').addClass('animated zoomIn');
  }, {
    offset: '50%'
  });

  $('.js--wp-31').waypoint(function(direction) {
    $('.js--wp-34').addClass('animated zoomIn');
  }, {
    offset: '60%'
  });

  $('.js--wp-31').waypoint(function(direction) {
    $('.js--wp-36').addClass('animated zoomIn');
  }, {
    offset: '10%'
  });

  $('.js--wp-34').waypoint(function(direction) {
    $('.js--wp-33').addClass('animated zoomIn');
  }, {
    offset: '40%'
  });

  $('.js--wp-33').waypoint(function(direction) {
    $('.js--wp-30').addClass('animated zoomIn');
  }, {
    offset: '30%'
  });

  $('.js--wp-29').waypoint(function(direction) {
    $('.js--wp-35').addClass('animated zoomIn');
  }, {
    offset: '40%'
  });

  $('.js--wp-33').waypoint(function(direction) {
    $('.js--wp-32').addClass('animated zoomIn');
  }, {
    offset: '50%'
  });

  /* Mobile navigation */
  $('.js--nav-icon').click(function() {
    var nav = $('.js--main-nav');
    var icon = $('.js--nav-icon i');

    nav.slideToggle(200);

    if (icon.hasClass('ion-navicon-round')) {
      icon.addClass('ion-close-round');
      icon.removeClass('ion-navicon-round');
    } else {
      icon.addClass('ion-navicon-round');
      icon.removeClass('ion-close-round');
    }
  });
});
