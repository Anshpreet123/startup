// navbar 

const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
const links = document.querySelectorAll(".nav-links li");

hamburger.addEventListener('click', ()=>{
   //Animate Links
    navLinks.classList.toggle("open");
    // links.forEach(link => {
    //     link.classList.toggle("fade");
    // });

    //Hamburger Animation
    hamburger.classList.toggle("toggle");
});

// navbar ends

// carowsel js

 var slide = document.getElementsByClassName("slide");
        var indicator = document.getElementById("indicator");
        var dots = document.getElementsByClassName("dots");
        var autoplay = document.getElementsByClassName("containers")[0].getAttribute("data-autoplay");
        var l = slide.length;
        var interval = 5000;
        var set;

        window.onload = function () {
            initialize();
            slide[0].style.opacity = "1";
            for (var j = 0; j < l; j++) {
                indicator.innerHTML += "<div class='dots' onclick=change(" + j + ")></div>";
            }

            dots[0].style.background = "#696969";

        }

        function initialize() {
            if (autoplay === "true")
                set = setInterval(function () { next(); }, interval);
        }



        function change(index) {
            clearInterval(set);
            count = index;
            for (var j = 0; j < l; j++) {
                slide[j].style.opacity = "0";
                dots[j].style.background = "#bdbdbd";
            }
            slide[count].style.opacity = "1";
            dots[count].style.background = "#696969";


        }

        var count = 0;
        function next() {
            clearInterval(set);
            slide[count].style.opacity = "0";
            count++;
            for (var j = 0; j < l; j++) {
                dots[j].style.background = "#bdbdbd";
            }


            if (count == l) {
                count = 0;
                slide[count].style.opacity = "1";
                dots[count].style.background = "#696969";

            } else {
                slide[count].style.opacity = "1";
                dots[count].style.background = "#696969";
            }
            initialize()
        }


        function prev() {
            clearInterval(set);
            slide[count].style.opacity = "0";
            for (var j = 0; j < l; j++) {
                dots[j].style.background = "#bdbdbd"; 
            }
            count--;

            if (count == -1) {
                count = l - 1;
                slide[count].style.opacity = "1";
                dots[count].style.background = "#696969";

            } else {
                slide[count].style.opacity = "1";
                dots[count].style.background = "#696969";
            }
            initialize()
        }
        // carowsel ends

        // function to appear vid

        function change(){
 document.getElementById("vid_img").style.display = "none";
 document.getElementById("onlyvid").style.display = "block";

}

// jquery for fade
// navbar scroll js

window.onscroll = () => {
  const nav = document.querySelector('#navbar');
  if(this.scrollY <= 10) nav.className = ''; else nav.className = 'scroll';
};