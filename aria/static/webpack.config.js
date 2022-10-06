const path = require('path');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const { HotModuleReplacementPlugin } = require('webpack');

module.exports = (env, argv) => {
  return {
    mode: argv.mode,
    entry: './app/index.js',
    output: {
      path: path.resolve(__dirname, 'dist/assets'),
      filename: 'js/[name].js',
      publicPath: '/assets/',
      clean: true,
    },
    plugins: [
      new MiniCssExtractPlugin({
        filename: 'css/[name].css',
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
    optimization: {
      minimizer: [new CssMinimizerPlugin()],
    },
    devServer: {
      open: true,
      static: {
        directory: path.join(__dirname, 'dist'),
        watch: true,
      },
      hot: true,
    },
  };
};
