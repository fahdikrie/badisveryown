function animateCSS(element, animationName, callback) {
    const node = document.querySelector(element)
    node.classList.add('animated', animationName)

}

const element =  document.querySelector('h1')
element.addEventListener('click', animateCSS(element, 'slideInUp'))
