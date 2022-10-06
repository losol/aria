const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const { HotModuleReplacementPlugin } = require('webpack');

module.exports = (env, argv) => {
  return {
    entry: path.join(__dirname, 'app', 'index.js'),
    output: {
      path: path.resolve(__dirname, 'dist'),
      filename: 'site.js',
    },
    plugins: [
      new MiniCssExtractPlugin({
        filename: '[name].site.css',
        chunkFilename: '[id].css',
      }),
      new HotModuleReplacementPlugin(),
    ],
    module: {
      rules: [
        {
          test: /\.(jsx|js)$/,
          include: path.resolve(__dirname, 'app'),
          exclude: /node_modules/,
          use: [
            {
              loader: 'babel-loader',
              options: {
                presets: [['@babel/preset-env']],
              },
            },
          ],
        },
        {
          test: /\.css$/i,
          include: path.resolve(__dirname, 'app'),
          exclude: /node_modules/,
          use: [
            'style-loader',
            {
              loader: MiniCssExtractPlugin.loader,
              options: {
                esModule: false,
              },
            },
            {
              loader: 'css-loader',
            },
            'postcss-loader',
          ],
        },
      ],
    },
    devServer: {
      open: true,
      static: path.join(__dirname, 'dist'),
      hot: true,
    },
  };
};
