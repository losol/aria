document.addEventListener(
  'DOMContentLoaded',
  function () {
    const lightswitch = document.querySelector('#lightswitch');
    lightswitch.addEventListener('click', toggler());
  },
  false
);
