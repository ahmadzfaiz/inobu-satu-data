const copyButton = [...document.getElementsByClassName('copy-button')]

let previous = null

copyButton.forEach(btn => btn.addEventListener('click', ()=>{
    const dataUrl = btn.getAttribute('data-url')
    navigator.clipboard.writeText(dataUrl)
    if(previous){
        previous.textContent = 'Copy'
    }
    previous = btn
    btn.textContent = 'Copied'
}))