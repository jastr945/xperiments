'use strict';


// removes placeholder from the search tab on focus and brings it back on blur
$('.form-control').focus(function(){
   $(this).data('placeholder', $(this).attr('placeholder'))
    .attr('placeholder','');
  }).blur(function(){
    $(this).attr('placeholder', $(this).data('placeholder'));
});


// Shows the edit form upon clicking the specific edit button
$('.edit').each(function () {
  $(this).click(function (e) {
    e.preventDefault();
    $(this).parent().siblings('.editItemForm').show();
    $(this).parent().siblings('.listInfo').hide();
  });
});


// Sends updated entry to the server, shows updated entry on the website
$('.update').each(function () {
  $(this).click(function (e) {
    e.preventDefault();
    var elementId = $(this).attr("value");
    var href = "http://localhost:5000/api/v1.0/items/" + elementId;
    var form_data = $(this).parent('.editItemForm').serialize();
    var that = this;
    $.ajax({
      url: href,
      type: "PUT",
      data: form_data,
      success: function (data) {
        var newdata = $.parseJSON(JSON.stringify(data));
        // console.log(newdata.data.title, newdata.data.note);
        $(that).parent('.editItemForm').hide();
        $(that).parent().siblings('.listInfo').text(newdata.data.title + " | " + newdata.data.note).show();
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
