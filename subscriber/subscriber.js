'use strict';


// Background pictures slider; images change upon cllicking right or left arrow

var images = [ 'coffee.jpg', 'coffee3.jpg', 'coffee2.jpg', 'coffee4.jpg', 'coffee5.jpg'];
var i = 0;


function reset() {
  $('#main').css({'background-image': 'none'});
};

$(document).ready(function() {
  $('#arrow-right').click(function() {
    console.log(i);
    reset();
    if (i === images.length - 1) {
      $('#main').css({'background-image': 'url(' + images[i] + ')'});
      i = 0;
    } else {
      $('#main').css({'background-image': 'url(' + images[i] + ')'});
      i++;
    }
  });

  $('#arrow-left').click(function() {
    reset();
    console.log(i);
    if (i <= 0) {
      $('#main').css({'background-image': 'url(' + images[images.length - 1] + ')'});
      i = images.length - 2;
    } else {
      $('#main').css({'background-image': 'url(' + images[i] + ')'});
      i = i - 1;
    }
  });
});
