<template>
  <div class="app">
    <PageLoader />
    <div class="router">
        <template>
          <transition appear name="fade" mode="out-in"
          enter-active-class="animate__animated animate__fadeInLeft"
          leave-active-class="animate__animated animate__zoomOutRight"
          >
            <component :is="currentLayout"> </component>
          </transition>
        </template>
    </div>
  </div>
</template>

<script>
import PageLoader from './components/PageLoader.vue'

export default {
  name: 'AppVue',
  computed: {
    currentLayout() {
      console.log(this.$route.meta);
      return this.$route.meta.layout;
    },
  },
  components: {
    PageLoader
  }
};
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
  *{
    font-family: 'Montserrat', sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body{
    background: white;
  }

  .container{
    /* display: flex; */
    width: 100%;
    max-width: 1436px;
    margin: 0 auto;
    padding-top: 30px!important;
  }

  /* scrollbar */

  ::-webkit-scrollbar{
    width: 15px;
  }
  ::-webkit-scrollbar-track{
    background: black;
  }
  ::-webkit-scrollbar-thumb{
    background: #00B74A;
    border-radius: 8px;
    border: 3px solid black;
  }
  ::-webkit-scrollbar-thumb:hover{
    background: #00973c;
  }



  @media (max-width: 1536px) {
    .container{
      max-width: none;
      padding: 0 50px;
    }
  }

</style>