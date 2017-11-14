'use strict';


var images = [ 'sea1.JPG', 'sea2.JPG', 'passiflora.JPG'];
var i = 0;


function reset() {
  $('#main').css({'background-image': 'none'});
};

$(document).ready(function() {
  $('#arrow-right').click(function() {
    reset();
    if (i < images.length) {
      $('#main').css({'background-image': 'url(' + images[i] + ')'});
      i++;
    } else {
      $('#main').css({'background-image': 'url(' + images[0] + ')'});
      i = 0;
    }
  });
});

$(document).ready(function() {
  $('#arrow-left').click(function() {
    reset();
    if (i < 0) {
      $('#main').css({'background-image': 'url(' + images[images.length - 1] + ')'});
      i=images.length-2;
    } else {
      $('#main').css({'background-image': 'url(' + images[i] + ')'});
      i=i-1;
    }
  });
});
