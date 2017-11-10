'use strict';


// randomly changing a background image on reload
$(document).ready(function() {
  var images = ['cannon.jpg', 'cannon2.JPG', 'cannon3.JPG', 'cannon4.jpg'];
  $('#main').css({'background-image': 'url(/static/searchapp/img/' + images[Math.floor(Math.random() * images.length)] + ')'});
});


// removing placeholder from the search tab on focus and bringing it back on blur
$('.form-control').focus(function(){
   $(this).data('placeholder', $(this).attr('placeholder'))
          .attr('placeholder','');
}).blur(function(){
   $(this).attr('placeholder', $(this).data('placeholder'));
});


// media section layout rearranges on small screen devices
$(window).resize(function(){
	if ($(window).width() <= 550){
		$('.pic').removeClass("media-left").addClass("media-top").css("margin-bottom", "1em");
	}
}).resize(); // causes an initial widow.resize to occur


// Jquery Autocomplete plugin working on the search field
$(document).ready(function() {
  $( "#ed-srch-term" ).autocomplete({
    source: "/get_titles"
  });
});
