module.exports = {
    devServer: {
        // hosst: 'localhost',
        // port: 8080,
        proxy: {
            '/api': {
                target: 'http://localhost:8000/api',
                changeOrigin: true,
                pathRewrite: {
                    '^/api': '/#/'
                }
            }
        }
    }
};