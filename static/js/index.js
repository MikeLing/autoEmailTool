window.onload = function () {
    new Vue({
      el: '#dashbord',
      delimiters: ['[[', ']]'],
      data: {
        writers: []
      },
      mounted() {
        this.initdashBord();
      },
      methods:{
        initdashBord(){
          axios.get('http://127.0.0.1:5000/getWrites/')
          .then((response) => {this.writers = response.data; console.log(this.writers)})
          .catch(error=>{console.log(error)})
        }
      }
    })
  
  }
  