'use strict';

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
