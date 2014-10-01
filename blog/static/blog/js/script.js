$(document).ready(function () {
  $(window).scroll(function () {
    var block = $('.recent_articles_block');

    if ($(window).width() > 970 && $(window).scrollTop() > 1400) {
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

  $('.article .like.active button').click(function () {
    var like = $(this).parent();
    var csrf = like.find('input');
    var button = like.find('button');
    var count = like.find('.count');

    var data = {};
    data[csrf.attr('name')] = csrf.attr('value');

    $.post(like.data('url'), data, function (data) {
      button.attr('class', data.active ? 'active' : '');
      count.text(data.likes_count);
    });
  });
});

