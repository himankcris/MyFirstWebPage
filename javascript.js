button = document.querySelector('#connect');

button.addEventListener('mouseover',function(){
    button.innerText = 'Click Me';
})

button.addEventListener('mouseout',function(){
    button.innerText = 'Connect.';
})