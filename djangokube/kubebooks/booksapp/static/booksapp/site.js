'use strict';

// Removes an entry from the list upon clicking on the cross icon
$('.deleteButton').each(function () {
  $(this).click(function (e) {
    e.preventDefault();
    var entry = $(this).parent().parent();
    var href = $(this).attr("href");
    $.ajax({
      url: href,
      type: "GET",
      success: function (e) {
        entry.fadeOut("fast");
      }
    });
  });
});
