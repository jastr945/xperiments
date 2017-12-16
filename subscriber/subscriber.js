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


// The Infobutton toggles footer; the view slides to the footer when appeared.
$(document).ready(function() {
  $('#infoButton').click(function() {
    var element = document.getElementById("footer");
    if ($('#footer').hasClass('invisible')) {
      $('#footer').removeClass('invisible').addClass('visible');
      element.scrollIntoView({behavior: "smooth", block: "end", inline: "nearest"});
    } else {
      $('#footer').removeClass('visible').addClass('invisible');
    }
  });
});

$(document).ready(function() {
  $('#coffeeButton').click(function() {
    if ($('.content').hasClass('invisible')) {
    $('.content').removeClass('invisible').addClass('visible');
    $('.subscribe').removeClass('visible').addClass('invisible');
  } else { $('.content').removeClass('visible').addClass('invisible');}
  });

  $('#subscribeButton').click(function() {
    if ($('.subscribe').hasClass('invisible')) {
    $('.subscribe').removeClass('invisible').addClass('visible');
    $('.content').removeClass('visible').addClass('invisible');
  } else { $('.subscribe').removeClass('visible').addClass('invisible');}
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
