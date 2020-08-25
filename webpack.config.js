const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
    entry: './frontend/Vue/main.js',
    output: {
        filename: 'build.js',
        path: path.resolve(__dirname, './static/js'),
        publicPath: '/static/js'
    },
    module: {
        rules: [
            {
                test: /\.(js)$/,
                exclude: /(node_modules)/,
                use: [
                    { loader: 'babel-loader' }
                ]
            },
            {
                test: /\.(css|scss)/,
                use: [
                    'style-loader'
                ]
            },
            {
                test: /\.vue$/,
                exclude: /node_modules/,
                loader: 'vue-loader'
            }
        ]
    },
    devServer: {
        // contentBase: ponerle la ruta del index de django
        contentBase: path.join(__dirname, 'templates'),
        watchContentBase: true,
        historyApiFallback: true,
        noInfo: true
      },
    plugins: [
        new VueLoaderPlugin()
    ]
}