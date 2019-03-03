function openInNewTab(url) {
    var win = window.open(url, '_blank');
    win.focus();
}

function play {

  var video=document.getElementById("autoplay");

  if(video.muted){
    video.muted = false;
  } else {
    video.muted = true;
  }

}