'use strict';

// removes placeholder from the search tab on focus and brings it back on blur
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


// Shows the edit form upon clicking the specific edit button
$('.edit').each(function () {
  $(this).click(function (e) {
    e.preventDefault();
    $(this).parent().siblings('.editItemForm').show();
    $(this).parent().siblings('.listInfo').hide();
  });
});


// Sends updated entry to the server
$('.update').each(function () {
  $(this).click(function (e) {
    e.preventDefault();
    var elementId = $(this).attr("value");
    var href = "http://localhost:5000/api/v1.0/items/" + elementId;
    var form_data = $(this).parent('.editItemForm').serialize();
    $.ajax({
      url: href,
      type: "PUT",
      data: form_data,
      success: function (e) {
        console.log("update request sent");
        $(this).parent('.editItemForm').hide();
      },
      error: function(jqXhr, textStatus, errorThrown) {
        console.log(errorThrown);
      }
    });
  });
});


// Removes an entry from the list
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
