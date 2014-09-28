$(document).ready(function () {
  $(window).scroll(function () {
    var block = $('.recent_articles_block');

    if ($(window).width() > 970 && $(window).scrollTop() > 1200) {
      if (!block.hasClass('fixed')) {
        block
          .width(block.width())
          .hide()
          .addClass('fixed')
          .fadeIn();
      }
    } else {
      block
        .removeClass('fixed')
        .css('width', 'auto');
    }
  });
});

