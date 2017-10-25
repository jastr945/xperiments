'use strict';

// removing placeholder from the search tab on focus and bringing it back on blur
$('.form-control').focus(function(){
   $(this).data('placeholder', $(this).attr('placeholder'))
          .attr('placeholder','');
}).blur(function(){
   $(this).attr('placeholder', $(this).data('placeholder'));
});
