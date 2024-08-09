var i = 0, opacity = 50, susOpacity = 0, hideAudio, beginning, clickedBeginning, audio, video, amongiygas, sus, susText, susImage, dotTimer, tooManyDots, susImages = [
  "SUS1.jpg", "SUS2.png", "SUS3.png", "SUS4.png", "SUS5.png", "SUS6.png", "SUS7.png", "SUS8.png",
  "SUS9.png", "SUS10.png", "SUS11.png", "SUS12.jpg", "SUS13.jpg", "SUS14.png", "SUS15.png", "SUS16.jpg",
  "SUS17.jpg", "SUS18.png", "SUS19.png", "SUS20.png", "SUS21.png", "SUS22.png", "SUS23.jpg", "SUS24.png"
];

window.addEventListener('load', () => {
  beginning = document.getElementsByClassName("beginning")[0];
  audio = document.getElementById("audio");
  video = document.getElementById("video");
  amongiygas = document.getElementsByClassName("amongiygas")[0];
  sus = document.getElementsByClassName("sus");
  susText = document.getElementsByClassName("sus-text");
  susImage = document.getElementById("sus-image");

  dotTimer = setInterval(function() {
      if (beginning.innerHTML.length == 10) {
          tooManyDots = true;
          beginning.innerHTML = "";
      }
      beginning.innerHTML += tooManyDots ? '\u2B24' : '.';
  }, 500);

  setTimeout(function() {
      document.onmousemove = moveAudio;
      document.onmouseup = moveAudio;
  }, 1500);

  setInterval(function() {
      if (tooManyDots)
          beginning.style.transform = "translate(0%, " + (Math.random() * 50 - 25) + "%)";
      if (!hideAudio)
          return;

      document.title = zalgo.generate("AMOGUS");
      let intensity = (Math.sin(i * 4 / 360) / 2 + .5) * 100, intensity_p = (Math.sin(i * 4 / 360 + 45) / 2 + .5) * 150;
      amongiygas.style.filter = "saturate(" + (intensity / 2 + 50) + "%) contrast(" + (intensity / 2 + 100) + "%) brightness(" + (intensity_p + 100) + "%)";
      amongiygas.style.backgroundSize = ((Math.sin(i * 2 / 360) / 2 + .5) * 80 + 20) + "vmin " + ((Math.cos(i * 2 / 360) / 2 + .5) * 80 + 20) + "vmin";
      amongiygas.style.backgroundPosition = (Math.sin(i * 4 / 360) * 500 + 500) + "% " + (Math.cos(i * 4 / 360) * 500 + 500) + "%";

      let text = document.getElementsByClassName("ruined")[0];
      text.style.transform = "translate(" + -(Math.random() * 2 + 49) + "%, " + -(Math.random() * 2 + 49) + "%)";

      let lum = Math.round(Math.random() * 0x7F + 0x80), rgb = "rgb(255, " + lum + ", " + lum + ")";
      text.style.color = rgb;

      let shadow = "0px 0px 8px rgb(0, 0, 0)";
      rgb = "rgb(95, " + lum * 0.375 + ", " + lum * 0.375 + ")";
      text.style.textShadow = "2px 2px " + rgb + ", -2px -2px " + rgb + ", " + shadow;

      for (let j = 0; j < sus.length; j++) {
          if (!(i % 32)) {
              sus[j].style.left = (Math.random() * (document.body.clientWidth - sus[j].offsetWidth)) + "px";
              sus[j].style.top = (Math.random() * (document.body.clientHeight - sus[j].offsetHeight)) + "px";
          } else {
              const rect = sus[j].getBoundingClientRect();
              sus[j].style.left = (Math.random() * 60 - 30 + rect.left) + "px";
              sus[j].style.top = (Math.random() * 60 - 30 + rect.top) + "px";
          }
      }

      for (let j = 0; j < susText.length; j++) {
          susText[j].innerHTML = zalgo.generate("sus!") + ' ' + String.fromCodePoint(0x1F633);
          if (!((i + 8) % 64)) {
              const rect = susText[j].getBoundingClientRect();
              susText[j].style.left = (Math.random() * (document.body.clientWidth - susText[j].offsetWidth)) + "px";
              susText[j].style.top = (Math.random() * (document.body.clientHeight - susText[j].offsetHeight)) + "px";
              susText[j].style.fontSize = (Math.random() * 18 + 2) + "vmin";
          }
      }

      opacity = Math.abs(opacity + Math.random() * 8 - 4);
      video.style.filter = "opacity(" + opacity + "%)";
      while (opacity > 90)
          opacity -= Math.random();

      if (!(i % Math.round(Math.random() * 50 + 250))) {
          susImage.onload = function() { susOpacity = 1; };
          susImage.src = susImages[Math.round(Math.random() * (susImages.length - 1))];
      }
      susImage.style.opacity = susOpacity;
      if (susOpacity > 0)
          susOpacity -= .01;
      if (susOpacity < 0)
          susOpacity = 0;
      i++;
  }, 10);
});

function playSus() {
  let _audio = new Audio("AMOGUS.mp3");
  _audio.loop = true;
  _audio.play();
  video.play();

  audio.style.display = "none";
  hideAudio = true;

  let beginning = document.getElementsByClassName("beginning")[0];
  beginning.style.display = "none";

  let elements = document.getElementsByClassName("hidden-audio");
  for (let j = 0; j < elements.length; j++)
      elements[j].style.display = "inherit";
}

function moveAudio(e) {
  if (hideAudio)
      return;
  tooManyDots = false;
  if (dotTimer != 0) {
      clearInterval(dotTimer);
      dotTimer = 0;
  }

  if (audio.style.display != "inherit") {
      audio.style.display = "inherit";
      beginning.innerHTML = "click it."
  }

  if (e.type == "mousemove") {
      let x = (window.Event) ? e.pageX : event.clientX + (document.documentElement.scrollLeft ? document.documentElement.scrollLeft : document.body.scrollLeft),
          y = (window.Event) ? e.pageY : event.clientY + (document.documentElement.scrollTop ? document.documentElement.scrollTop : document.body.scrollTop);
      audio.style.left = (x - audio.offsetWidth / 2) + "px";
      audio.style.top = (y - audio.offsetHeight / 2) + "px";
  } else if (!clickedBeginning) {
      clickedBeginning = true;
      audio.style.left = (document.body.clientWidth / 2 - audio.offsetWidth / 2) + "px";
      audio.style.top = (document.body.clientHeight / 2 - audio.offsetHeight / 2) + "px";
  }
}

function vh(v) {
  return (v * Math.max(document.documentElement.clientHeight, window.innerHeight || 0)) / 100;
}

function vw(v) {
  return (v * Math.max(document.documentElement.clientWidth, window.innerWidth || 0)) / 100;
}

function vmin(v) {
  return Math.min(vh(v), vw(v));
}