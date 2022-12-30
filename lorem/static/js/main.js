(function () {
    function updateDimensions() 
    {
      try {
        const height = document.height !== undefined 
            ? document.height 
            : document.body.offsetHeight
        if (window.postMessage/* && document.referrer && document.referrer !== ''*/) {
          parent.postMessage(height, '*' /*document.referrer*/)
        }
      } catch (error) {
        console.log('%cError: ', 'color: tomato;', error)
      }
    }
  
    updateDimensions()

    const controls = document.querySelectorAll('input[required], textarea[required')

    for (let i = 0; i < controls.length; i++) {
        controls[i].addEventListener(
            'blur',
            function (event) {
                event.target.classList.remove('invalid')
                if (!event.target.value || !event.target.value.length) {
                    event.target.classList.add('invalid')
                }
            }
        )
    }
  })()