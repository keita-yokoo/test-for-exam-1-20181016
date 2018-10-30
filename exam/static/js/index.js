// import Vue from "vue";
//
// import Vuetify from "vuetify";
// import "vuetify/dist/vuetify.min.css";
// import "material-design-icons/iconfont/material-icons.css";

// var vue = require("vue");
// var vuetify = require("vuetify");
// import vue from 'vue';
// import axios from 'axios';
// import vueaxios from 'vue-axios';

var axios = require('axios');
var vueaxios = require('vue-axios');

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

Vue.use(vueaxios, axios)

let params = new URLSearchParams({"test": "test"});

var vu = new Vue({
  el: '#login',
  data: () => ({
     email: 'test',
     password: ''
  }),
  methods: {
       submit () {
        // Native form submission is not yet supported
        axios.post('/', new URLSearchParams({
            "email": this.email,
            "password": this.password
        })).then(response => {
            console.log(response)
        })
    },
    clear () {
      this.$refs.form.reset()
    }
  }
});



// import colors from 'vuetify/es5/util/colors'

// this.$vuetify.theme.primary = '#2196F3'
// this.$vuetify.theme.secondary = '#1565C0'
// this.$vuetify.theme.accent = '#F50057'
//
Vue.use(Vuetify, {
  theme: {
    primary: "#2196F3",
    secondary: "#1565C0",
    accent: "#F50057",
    error: "#f44336",
    warning: "#ffeb3b",
    info: "#2196f3",
    success: "#4caf50"
  }
});
