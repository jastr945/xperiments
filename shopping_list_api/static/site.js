'use strict';


// removes placeholder from the search tab on focus and brings it back on blur
$('.form-control').focus(function(){
   $(this).data('placeholder', $(this).attr('placeholder'))
    .attr('placeholder','');
  }).blur(function(){
    $(this).attr('placeholder', $(this).data('placeholder'));
});


// opens the login form
$('#loginChoice').click(function (e) {
  e.preventDefault();
  $('#loginForm').show();
  $('#choices').hide();
});


// opens the signup form
$('#signupChoice').click(function (e) {
  e.preventDefault();
  $('#signupForm').show();
  $('#choices').hide();
});


// sends data from the signup form
$('#signupForm').submit(function (e) {
  e.preventDefault();
  var href = "/api/v1.0/signup";
  var form_data = $(this).serialize();
  console.log(form_data);
  var that = this;
  $.ajax({
    url: href,
    type: "POST",
    data: form_data,
    success: function (data) {
      $(that).hide();
      $(that).siblings('#choices').show();
      $('#messages').html("<h4 class='green'>New user was created. Please log in.</h4>")
    },
    error: function(jqXhr, textStatus, errorThrown) {
      console.log(errorThrown);
      $('#messages').html("<h4 class='red'>Something went wrong. Try another username.</h4>")
    }
  });
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
        $(that).parent().siblings('.listInfo').html(newdata.data.title + '&nbsp;|&nbsp;<i>' + newdata.data.note + '</i>').show();
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
