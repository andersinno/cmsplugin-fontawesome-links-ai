var gulp = require("gulp");
var concat = require("gulp-concat");
var uglify = require("gulp-uglify");
var plumber = require("gulp-plumber");

var STATIC_SRC_PATH = "cmsplugin_fontawesome_links_ai/static_src/";
var STATIC_DEST_PATH = "cmsplugin_fontawesome_links_ai/static/cmsplugin_fontawesome_links_ai/";
var BOWER_PATH = "bower_components/";

gulp.task("js", function() {
    return gulp.src([
        STATIC_SRC_PATH + "js/initialize.js",
        BOWER_PATH + "select2/dist/js/select2.full.js"
    ])
        .pipe(plumber({}))
        .pipe(concat("cmsplugin_fontawesome_links_ai.min.js"))
        .pipe(uglify())
        .pipe(gulp.dest(STATIC_DEST_PATH + "js/"));
});

gulp.task("js:watch", ["js"], function() {
    gulp.watch([STATIC_SRC_PATH + "js/initialize.js"], ["js"]);
});

gulp.task("copy_css", function() {
    return gulp.src([
        BOWER_PATH + "select2/dist/css/select2.min.css",
        BOWER_PATH + "font-awesome/css/font-awesome.min.css"
    ]).pipe(gulp.dest(STATIC_DEST_PATH + "css/"));
});

gulp.task("copy_fonts", function() {
    return gulp.src([
        BOWER_PATH + "font-awesome/fonts/*"
    ]).pipe(gulp.dest(STATIC_DEST_PATH + "fonts/"));
});

gulp.task("default", ["js", "copy_fonts", "copy_css"]);

gulp.task("watch", ["js:watch"]);
