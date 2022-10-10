/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme');
module.exports = {
  content: ['dist/*.html'],
  darkMode: 'class',
  theme: {
    fontFamily: {
      sans: ['source-sans-pro', 'sans-serif'],
      serif: ['Georgia', 'serif'],
      mono: ['ui-monospace', 'mono'],
      body: ['Source Sans Pro'],
    },
    extend: {
      container: {
        padding: {
          DEFAULT: '1rem',
          sm: '2rem',
          lg: '4rem',
          xl: '5rem',
          '2xl': '6rem',
        },
      },
    },
  },
  variants: {
    extend: {},
  },
};
