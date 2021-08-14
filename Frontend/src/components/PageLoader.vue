<template>
<!-- animate__animated animate__fadeOut -->
  <div v-if="show" class="page-loader animate__animated animate__fadeOut">  
    <div class="portfolio-text">
      <span>P</span>
      <span>O</span>
      <span>R</span>
      <span>T</span>
      <span>F</span>
      <span>O</span>
      <span>L</span>
      <span>I</span>
      <span>O</span>
    </div>
    <div class="name">
      <h1>NIKITA MIKHAILOV</h1>
    </div>
    <div class="year">
      2021
    </div>
    <!-- <div class="text1">NIKITA MIKHAILOV</div>
    <div class="text2">portfolio</div> -->
  </div>
</template>


<script>
export default {
  data(){
    return{
      show: true,
      // textPopup: false
    }
  },

  mounted(){
    this.showes()
  },

  methods: {
    showes(){
      setTimeout(() => {
        this.show = false
      }, 3000);
    }
  },
}
</script>

<style lang="sass" scoped>
  .portfolio-text
    display: flex
    flex-wrap: wrap
    align-items: center
    justify-content: center
    width: 400px
    animation: bounceIn 2.0s forwards
    span
      text-align: center
      color: white
      flex-basis: 33.333%
      margin-bottom: 20px
      font-size: 90px 

  .name
    margin-top: 100px
    animation: bounceIn 2.0s forwards
    h1
      color: white
      letter-spacing: 10px  
      font-weight: 300

  .year
    animation: bounceIn 2.0s forwards
    color: white
    margin-top: 20px
    letter-spacing: 10px  
    font-weight: 300

  // .text1
  //   color: white
  //   font-size: 30px
  //   animation: bounceIn 2s forwards
  
  // .text2
  //   color: white
  //   font-size: 15px
  //   // animation: bounceIn2 2s forwards

  @keyframes bounceIn
    0%
      transform: translateX(-200px)
      opacity: 0
    20%
      transform: scale(1.2)
      opacity: 1
    80%
      transform: scale(1.2)
      opacity: 1
    100%
      transform: translateX(200px)
      opacity: 0

  // @keyframes bounceIn2
  //   0%
  //     transform: translateX(200px)
  //     opacity: 0
  //   30%
  //     transform: scale(1.2)
  //     opacity: 1
  //   70%
  //     transform: scale(1.2)
  //     opacity: 1
  //   100%
  //     transform: translateX(-200px)
  //     opacity: 0

  .page-loader
    display: flex
    justify-content: center
    flex-direction: column
    align-items: center
    position: absolute
    top: 0
    left: 0
    width: 100vw
    height: 100vh
    background-color: black
    z-index: 999
    animation-delay: 2s

</style>