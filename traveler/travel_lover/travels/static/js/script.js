let btnRight = document.querySelector(".btnRight");
let slides = document.getElementsByClassName("picture");

let i = 0;

btnRight.addEventListener("click", function () {
    ++i
    if (i >= slides.length) {
        slides[i - 1].classList.remove("block_slides");
        i = 0;
        slides[i].classList.add("block_slides");
    }
    else {
        slides[i - 1].classList.remove("block_slides");
        slides[i].classList.add("block_slides");
    }
})
