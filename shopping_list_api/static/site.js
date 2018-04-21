'use strict';

// removing placeholder from the search tab on focus and bringing it back on blur
$('.form-control').focus(function(){
   $(this).data('placeholder', $(this).attr('placeholder'))
    .attr('placeholder','');
  }).blur(function(){
    $(this).attr('placeholder', $(this).data('placeholder'));
});

// Adding an item to the list
// $('#addItem').click(function (e) {
//   e.preventDefault();
//   var href = "api/v1.0/items";
//   var form_data = $('form').serialize();
//   $.ajax({
//     url: href,
//     type: "POST",
//     dataType: "json",
//     processData: false,
//     contentType: 'application/json',
//     data: form_data,
//     success: function(data){
//       console.log("Item posted" + data);
//     },
//     error: function( jqXhr, textStatus, errorThrown ){
//         console.log( errorThrown );
//     }
//   })
// });

// Removes an entry from the list upon clicking on the cross icon
$('.delete').each(function () {
  $(this).click(function (e) {
    e.preventDefault();
    var entry = $(this).parent().parent();
    var elementId = $(this).attr("value");
    var href = "http://localhost:5000/api/v1.0/items/" + elementId;
    $.ajax({
      url: href,
      type: "DELETE",
      success: function (e) {
        entry.fadeOut("fast");
        console.log("delete request sent");
      },
      error: function(jqXhr, textStatus, errorThrown) {
        console.log(errorThrown);
      }
    });
  });
});
