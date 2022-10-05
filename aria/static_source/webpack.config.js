const path = require('path');
module.exports = {
  mode: 'production',
  entry: './app/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'site.js',
  },
  module: {
    rules: [
      {
        test: /\.js$/i,
        include: path.resolve(__dirname, 'src'),
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
          },
        },
      },
      {
        test: /\.css$/i,
        include: path.resolve(__dirname, 'app'),
        use: ['style-loader', 'css-loader', 'postcss-loader'],
      },
    ],
  },
  devServer: {
    static: 'dist',
    watchFiles: './app',
  },
};
