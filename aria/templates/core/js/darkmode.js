// Save user preference in local storage
if (!('darkmode' in localStorage)) {
  localStorage.darkmode = parseInt(
    window.matchMedia('(prefers-color-scheme: dark)').matches
  );
}
// Set mode
const setMode = () => {
  if (localStorage.darkmode == 1) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
};
// Toggle
const toggler = () => {
  if (localStorage.darkmode == 1) {
    localStorage.darkmode = 0;
    setMode();
  } else {
    localStorage.darkmode = 1;
    setMode();
  }
};
setMode();
