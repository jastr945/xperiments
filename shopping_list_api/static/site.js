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
  // console.log(form_data);
  var that = this;
  $.ajax({
    url: href,
    type: "POST",
    data: form_data,
    success: function (data) {
      $(that).hide();
      $(that).siblings('#choices').show();
      $('#messages').html("<h4 class='green'>New user was created. Please log in.</h4>");
      $('input[type="text"]').val('');
    },
    error: function(jqXhr, textStatus, errorThrown) {
      console.log(errorThrown);
      $('#messages').html("<h4 class='red'>Something went wrong. Try another username.</h4>")
    }
  });
});


// sends data from the login form
$('#loginForm').submit(function (e) {
  e.preventDefault();
  var href = "/api/v1.0/login";
  var form_data = $(this).serialize();
  // console.log(form_data);
  var that = this;
  $.ajax({
    url: href,
    type: "POST",
    data: form_data,
    success: function (data) {
      $(that).hide();
      $('#messages').html("<h4 class='green'>Login successful.</h4>");
      $('input[type="text"]').val('');
      if (data.redirect !== undefined && data.redirect) {
        setTimeout(function() {
          window.location.href = data.redirect_url;
        }, 1200);
      };
    },
    error: function(jqXhr, textStatus, errorThrown) {
      console.log(errorThrown);
      $('#messages').html("<h4 class='red'>Something went wrong. Please try again.</h4>")
    }
  });
});


// logs the user out
$('#logout').click(function (e) {
  e.preventDefault();
  var href = "/api/v1.0/logout";
  $.ajax({
    url: href,
    type: "GET",
    success: function (data) {
      $('#messages').html("<h4 class='green'>Logout successful.</h4>");
      // $('#welcome').hide();
      if (data.redirect !== undefined && data.redirect) {
        setTimeout(function() {
          window.location.href = data.redirect_url;
        }, 1200);
      };
    },
    error: function(jqXhr, textStatus, errorThrown) {
      console.log(errorThrown);
      $('#messages').html("<h4 class='red'>Something went wrong. Please try again.</h4>")
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


// posts a new entry to the server
$('#addItemForm').submit(function (e) {
  e.preventDefault();
  var href = "/api/v1.0/items";
  var form_data = $(this).serialize();
  // console.log(form_data);
  $.ajax({
    url: href,
    type: "POST",
    data: form_data,
    success: function (data) {
      $('#messages').html("<h4 class='green'>A new item was added.</h4>");
      $('input[type="text"]').val('');
      if (data.redirect !== undefined && data.redirect) {
        setTimeout(function() {
          window.location.href = data.redirect_url;
        }, 1200);
      };
    },
    error: function(jqXhr, textStatus, errorThrown) {
      console.log(errorThrown);
      $('#messages').html("<h4 class='red'>Something went wrong. Please try again. Login required.</h4>");
    }
  });
});


// Sends updated entry to the server, shows updated entry on the website
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
      success: function (data) {
        // console.log(data);
        if (data.redirect !== undefined && data.redirect) {
          setTimeout(function() {
            window.location.href = data.redirect_url;
          }, 1200);
        };
        $('#messages').html("<h4 class='green'>Record updated successfully.</h4>")
      },
      error: function(jqXhr, textStatus, errorThrown) {
        console.log(errorThrown);
        $('#messages').html("<h4 class='red'>Something went wrong. Try again. Login required.</h4>")
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
        $('#messages').html("<h4 class='green'>Record deleted successfully.</h4>")
      },
      error: function(jqXhr, textStatus, errorThrown) {
        console.log(errorThrown);
        $('#messages').html("<h4 class='red'>Something went wrong. Try again. Login required.</h4>")
      }
    });
  });
});
