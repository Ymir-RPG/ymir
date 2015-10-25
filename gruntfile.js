/**
 * Created by austin on 6/11/15.
 */

"use strict";


module.exports = function (grunt) {

  grunt.initConfig({

    env: {
      development: {
        NODE_ENV: 'development'
      },
      production: {
        NODE_ENV: 'production'
      }
    },

    run: {
      app: {
        cmd: 'python',
        args: [
          "run.py"
        ]
      }
    },

    concurrent: {
      develop: {
        tasks: ["watch", "start"],
        options: {
          logConcurrentOutput: true
        }
      }
    },

    browserify: {
      options: {
        transform: [
          "reactify"
        ]
      },
      worldlist: {
        src: "components/YmirWorldList.js",
        dest: "components/dist/YmirWorldList.min.js"
      },
      overview: {
        src: "components/YmirOverview.js",
        dest: "components/dist/YmirOverview.min.js"
      },
      character: {
        src: "components/YmirCharacter.js",
        dest: "components/dist/YmirCharacter.min.js"
      },
      search: {
        src: "components/YmirSearch.js",
        dest: "components/dist/YmirSearch.min.js"
      }
    },

    watch: {
      styles: {
        files: 'static/css/**/*.less',
        tasks: ['less']
      },
      channelsScripts: {
        files: ['components/**/*.js'],
        tasks: ['browserify']
      }
    },

    less: {
      development: {
        files: {
          "static/css/app.css": "static/css/app.less"
        }
      }
    }
  });


  grunt.loadNpmTasks("grunt-contrib-watch");
  grunt.loadNpmTasks('grunt-env');
  grunt.loadNpmTasks("grunt-browserify");
  grunt.loadNpmTasks("grunt-contrib-less");
  grunt.loadNpmTasks('grunt-concurrent');
  grunt.loadNpmTasks('grunt-run');


  grunt.registerTask('dist', [
    "env:development",
    "browserify",
    "less"
  ]);

  grunt.registerTask('start', [
    "run"
  ]);

  grunt.registerTask('default', [
    "dist",
    "concurrent:develop"
  ]);
};
