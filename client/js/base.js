'use strict';

var $ = require('jquery');

global.jQuery = $;
window.jQuery = window.$ = $;

var Tether = require('tether');
window.Tether = Tether;
global.Tether = Tether;

require('bootstrap');

$(document).ready(function() {

 function logPosition(position) {
    // position will be between 0 and 100

    var minp = 0;
    var maxp = 300;

    // The result should be between 0 an 300
    var minv = Math.log(0.1);
    var maxv = Math.log(300);

    // calculate adjustment factor
    var scale = (maxv-minv) / (maxp-minp);
    console.log( (Math.log(position)-minv) / scale + minp);

    // return Math.exp(minv + scale*(position-minp));
  }

  function rotateSheets(initial) {
    var windowWidth = $(window).width();
    if ( windowWidth > 1300 && windowWidth < 1600 || initial === true && windowWidth > 1300 ) {
      $('.t-card').each(function(index,el){
        var step = $(el).attr('data-degree') / 300;
        var distance = windowWidth - 1300;
        if (initial && windowWidth >= 1600) {
          var distance = 300;
        }
        var rotation = step * distance;
        $(el).css({
          'transform': 'rotate(' + rotation  + 'deg)',
          'webkitTransform': 'rotate(' + rotation  + 'deg)',
          'mozTransform': 'rotate(' + rotation  + 'deg)',
          'msTransform': 'rotate(' + rotation  + 'deg)',
          'oTransform': 'rotate(' + rotation  + 'deg)'
        });
      });
    }
  }

  function positionSheets(initial) {

    var animationDistance = 300;
    var windowWidth = $(window).width();
    var windowHeight = $(window).innerHeight();
    var pageWidth = 1300;
    var maxPageWidth = 1900;

    $('.t-card').each(function(index,el){
      var x = windowWidth / 2;
      var orientation = $(el).attr('data-orientation');
      var destX = parseInt($(el).attr('data-posx'));
      var destY = parseInt($(el).attr('data-posy'));
      var distance = (windowWidth - pageWidth) / 2;
      var elWidth = $(el).width()/2;

      if (initial) {

        if ( windowWidth > pageWidth ) {
          if ( orientation === 'left' ) {
            $(el).css({
              'left': destX + 'px',
              'top': destY + 'px'
            });
          } else if ( orientation === 'right' ) {
            $(el).css({
              'right': destX + 'px',
              'top': destY + 'px'
            });
          }
        } else {
          if ( orientation === 'left' ) {
            $(el).css({
              'left': 0 + 'px',
              'top': destY + 'px'
            });
          } else if ( orientation === 'right' ) {
            $(el).css({
              'right': pageWidth + 'px',
              'top': destY + 'px'
            });
          }
        }

      } else {

        if ( windowWidth > pageWidth ) {

          if ( orientation === 'left' ) {
            if (windowWidth >= maxPageWidth) {
              var posX = destX;
            } else {
              var path = destX;
              var stepX = path / animationDistance;
              var posX = destX + path - stepX * distance;
            }
            $(el).css({
              'left': posX + 'px',
              'top': destY + 'px'
            });
          } else if ( orientation === 'right' ) {
            if (windowWidth >= maxPageWidth) {
              var posX = destX;
            } else {
              var path = destX;
              var stepX = path / animationDistance;
              var posX = destX + path - stepX * distance;
            }
            $(el).css({
              'right': posX + 'px',
              'top': destY + 'px'
            });
          }

        } else {
          if ( orientation === 'left' ) {
            $(el).css({
              'left': 0 + 'px',
              'top': destY + 'px'
            });
          } else if ( orientation === 'right' ) {
            $(el).css({
              'right': 0 + 'px',
              'top': destY + 'px'
            });
          }
        }
      }
    });
  }

  function rotateSponsorshipCards() {
    $('.sponsorship-card').each(function(index, el) {
        var rotation = Math.floor(Math.random() * 16) - 8;
        $(el).css({
          'transform': 'rotate(' + rotation  + 'deg)',
          'webkitTransform': 'rotate(' + rotation  + 'deg)',
          'mozTransform': 'rotate(' + rotation  + 'deg)',
          'msTransform': 'rotate(' + rotation  + 'deg)',
          'oTransform': 'rotate(' + rotation  + 'deg)'
        });
    });
  }



  $(window).resize(function(e) {
    rotateSheets();
    positionSheets();
  });

  rotateSheets(true);
  rotateSponsorshipCards()
  positionSheets(true);

  window.onload = function() {
    $('body').removeClass('loading');
  }
});