module.exports = {
    configureWebpack: {
    // other webpack options to merge in ...
    },
    // devServer options dont belong into `configureWebpack`
    devServer: {
        host: "0.0.0.0",
        hot: true,
        disableHostCheck: true,      
    },
    
}