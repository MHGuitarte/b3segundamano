let carouselIndex = 1;
showDivs(carouselIndex);

function plusDivs(n) {
    showDivs(carouselIndex += n);
}

function currentDiv(n) {
    showDivs(carouselIndex = n);
}

function showDivs(n) {
    let i;
    const images = document.getElementsByClassName("details-carousel");
    if (n > images.length) {
        carouselIndex = 1
    }
    if (n < 1) {
        carouselIndex = images.length
    }
    for (i = 0; i < images.length; i++) {
        images[i].style.display = "none";
    }

    images[carouselIndex - 1].style.display = "block";
}