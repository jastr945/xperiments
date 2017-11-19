'use strict';


// Background pictures slider; images change upon cllicking right or left arrow

var images = [ 'coffee.jpg', 'coffee3.jpeg', 'coffee2.jpg', 'coffee4.jpg', 'coffee5.jpg'];
var i = 0;


function reset() {
  $('#main').css({'background-image': 'none'});
};

$(document).ready(function() {
  $('#arrow-right').click(function() {
    reset();
    if (i === images.length - 1) {
      i = 0;
      $('#main').css({'background-image': 'url(' + images[i] + ')'});
    } else {
      i++;
      $('#main').css({'background-image': 'url(' + images[i] + ')'});
    }
  });

  $('#arrow-left').click(function() {
    reset();
    if (i <= 0) {
      i = images.length - 1;
      $('#main').css({'background-image': 'url(' + images[images.length - 1] + ')'});
    } else {
      i = i - 1;
      $('#main').css({'background-image': 'url(' + images[i] + ')'});
    }
  });
});


// footer shows and hides upon the info-button click
$(document).ready(function() {
  $('#infoButton').click(function() {
    if ($('footer').hasClass('invisible')) {
      $('footer').removeClass('invisible').addClass('visible');
    } else {
      $('footer').removeClass('visible').addClass('invisible');
    }
  });
});


// selected menu item shows a corresponding recipe segment
$(document).ready(function() {
  $('.menu-item').click(function() {
    $('.menu-item').not(this).removeClass('clicked');
    $(this).toggleClass('clicked');
    var index = $('.menu-item').index(this);
    $('.text-item').eq(index).show(); // showing a corresponding text item
    $('.text-item').not($('.text-item').eq(index)).hide(); // hiding all other text items
  });
});
