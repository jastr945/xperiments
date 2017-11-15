'use strict';


// Background pictures slider; images change upon cllicking right or left arrow

var images = [ 'coffee.jpg', 'coffee3.jpg', 'coffee2.jpg', 'coffee4.jpg', 'coffee5.jpg'];
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
